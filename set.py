name = {"hari","ram","jadu"}
# print(name)
# print(len(name))
# print(type(name))

# for x in name:
#     print(x)


# if "pami" in name:
#     print("enter name is in set")

# else:
#     print("enter name is not in set")


# name.add("laxmi")
# print(name)

# name_list = ["ksik","tanvi"]
# name.update(name_list)
# print(name)


# name.remove("hari")
# print(name)

# name.discard("sami")
# print(name) #this function will not throw an error if value is not present in set


s1={'a','u','i','y'}
s2 = {'o','i','s'}
# print(s1,s2)

# joining 2 set
# s3 = s1.union(s2)
# print(s3)

# only duplicates while joining
# s1.intersection_update(s2)
# print(s1)


# keep all values excpt duplicate values
s1.symmetric_difference_update(s2)
print(s1)