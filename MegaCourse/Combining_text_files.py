
#1. Consider using the glob2  third party library to generate a
# list of filenames to iterate through.


#2. Use a with  statement to create a new text file and
# then iterate through the file list inside that with  statement
# and open and read existing file contents in each iteration and write
# them to new text file.

import glob2
from datetime import datetime

filenames = glob2.glob("*.txt")
with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt", 'w') as file:
    for filename in filenames:
        with open(filename, "r") as f:
            file.write(f.read() + "\n")