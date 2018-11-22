#Having Multiple values in each key
students = {
    "Alice":["ID0001", 26, "A"],
    "Greg":["ID0002", 23, "A-"],
    "Tom":["ID0003", 24, "B"],
    "Bruce":["ID0004", 27, "C"]}

#Fetching those values with slices
print (students["Tom"][0])
print (students["Greg"][2])
print (students["Bruce"][0:])


#Having dictonarys in side of dictonarys for easy access
students = {
    "Alice":{"id":"ID0001", "age":26, "grade":"A"},
    "Greg":{"id":"ID0002", "age":24,"grade":"B"},
    "Tom":{"id":"ID0003", "age":22, "grade":"D"},
    "Bruce":{"id":"ID0004", "age":21, "grade":"E"}}

print (students["Tom"]["age"])