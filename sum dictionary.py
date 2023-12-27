# dict ={
#     'a':100,
#     'b':200,
#     'c':300
# }

# print("The sum of the dictionary value is =",sum(dict.values()))


# input_string = input("Enter string:")
# n = int(input("Enter n:"))

# # creating dictionary for mirror operation
# alphabets = "abcdefghijklmnopqrstuvwxyz"
# reverse_alphabets = alphabets[::-1]
# dict1 = dict(zip(alphabets,reverse_alphabets))

# # finding the part of string on which we will do mirror operation
# prefix = input_string[0:n-1]
# suffix = input_string[n-1:]

# # finding the mirror string

# mirror = ""
# for i in range(0,len(suffix)):
#     mirror = mirror +dict1[suffix[i]]

#  #creating the final string
# res = prefix + mirror
# print("The result is:",res)


n= int(input("Enter n:"))

sum = 0

for i in range(1,n+1):
    sum += i
    print("sum of n is :",sum)
     
