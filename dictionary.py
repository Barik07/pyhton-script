student = {
           "name":"hari",
           "roll_no":99,
           "class":"9",
           "sec":"A"
           }
print(student)
# print(type(student))
# print(len(student))
# print(student["name"])
# print(student.keys())

student["name"] = "kausik"
print(student)

student["blood_group"]= "O+"
print(student)

# student.popitem()
# print(student)

student.pop("roll_no")
print(student)

for x in student.items():
    print(x)



# student.clear()
# print(student)