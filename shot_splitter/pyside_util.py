# Extends PySide functionality for Maya 2017
# From Qt.py: https://github.com/mottosso/Qt.py/blob/master/examples/loadUi/baseinstance2.py


'''
try:
    from PySide import QtCore
    from PySide import QtWidgets
except:
    from PyQt5.QtCore import pyqtSlot as Slot
    from PyQt5 import QtCore
    from PyQt5 import QtWidgets
'''
import sys
import os



from Qt import QtCore, QtWidgets, __binding__

class PySideUtil(object):
    @staticmethod
    def load_ui_type(uifile):
        """Pyside equivalent for the loadUiType function in PyQt.
        From the PyQt4 documentation:
            Load a Qt Designer .ui file and return a tuple of the generated form
            class and the Qt base class. These can then be used to create any
            number of instances of the user interface without having to parse the
            .ui file more than once.
        Note:
            Pyside lacks the "loadUiType" command, so we have to convert the ui
            file to py code in-memory first and then execute it in a special frame
            to retrieve the form_class.
        Args:
            uifile (str): Absolute path to .ui file
        Returns:
            tuple: the generated form class, the Qt base class
        """
        try:
            import pysideuic
        except ImportError:
            import pyside2uic #support for qt5 in maya
            pysideuic = pyside2uic
        except:
            raise
        import xml.etree.ElementTree as ElementTree
        from cStringIO import StringIO

        parsed = ElementTree.parse(uifile)
        widget_class = parsed.find('widget').get('class')
        form_class = parsed.find('class').text

        with open(uifile, 'r') as f:
            o = StringIO()
            frame = {}

            pysideuic.compileUi(f, o, indent=0)
            pyc = compile(o.getvalue(), '<string>', 'exec')
            exec (pyc) in frame

            # Fetch the base_class and form class based on their type in
            # the xml from designer
            form_class = frame['Ui_%s' % form_class]
            base_class = eval('QtWidgets.%s' % widget_class)
        return form_class, base_class

    @staticmethod
    def pyside_load_ui(uifile, base_instance=None):
        """Provide PyQt4.uic.loadUi functionality to PySide
        Args:
            uifile (str): Absolute path to .ui file
            base_instance (QWidget): The widget into which UI widgets are loaded
        Note:
            pysideuic is required for this to work with PySide.
            This seems to work correctly in Maya as well as outside of it as
            opposed to other implementations which involve overriding QUiLoader.
        Returns:
            QWidget: the base instance
        """
        form_class, base_class = PySideUtil.load_ui_type(uifile)
        if not base_instance:
            typeName = form_class.__name__
            finalType = type(typeName,
                             (form_class, base_class),
                             {})
            base_instance = finalType()
        else:
            if not isinstance(base_instance, base_class):
                raise RuntimeError(
                    'The base_instance passed to loadUi does not inherit from'
                    ' needed base type (%s)' % type(base_class))
            typeName = type(base_instance).__name__
            base_instance.__class__ = type(typeName,
                                           (form_class, type(base_instance)),
                                           {})
        base_instance.setupUi(base_instance)
        return base_instance

    @staticmethod
    def load_ui_wrapper(uifile, base_instance=None):
        """Load a Qt Designer .ui file and returns an instance of the user interface
        Args:
            uifile (str): Absolute path to .ui file
            base_instance (QWidget): The widget into which UI widgets are loaded
        Returns:
            function: pyside_load_ui or uic.loadUi
        """
        if 'PySide' in __binding__:
            return PySideUtil.pyside_load_ui(uifile, base_instance)
        elif 'PyQt' in __binding__:
            uic = __import__(__binding__ + ".uic").uic
            return uic.loadUi(uifile, base_instance)