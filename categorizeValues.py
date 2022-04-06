# Categorizing Values

myMixedList = [45, 3.1415, 5j, (0, 0), {
    "Class" : "Cloud Computing",
    "Instructor" : "Steve Robinson"
}, "EDGE UP 2.0"]

for item in myMixedList:
    print(" {} is of the data type {}".format(item, type(item)))