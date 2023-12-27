# def printhello():
#     print("Hello world!")

# printhello()


# def add(n1,n2=0):
#     print("n1:",n1)
#     print("n2:",n2)
#     sum = n1+n2
#     return sum
# positional argument
# print("The sum is :",add(6,3))

# keyword argument(named argument)
# print("the sum is :",add(n1=8,n2=9))

# deffault argument
# print("The sum is :",add(6))

# arbitary argument
# def addallnumber(*args):
#     sum = 0
#     for i in args:
#         sum+=i
#     return sum
# output = addallnumber(1,2,3,4,5)
# print("The sum is:",output)


# kwargs(key-word argument)
# def studentinfo(**kwargs):
#     for x,y in kwargs.items():
#         print(x ,"is", y)

# studentinfo(name="Biswajit",age=22,city="Odisha")
# studentinfo(name="Debasish",age=21,city="Delhi")

n= int(input("Enter n:"))
def sumOneton(n):
    sum = 0
    for i in range(1,n+1):
        sum +=i
    return sum
output = sumOneton(n)
print("The sum no is :",output)
n1= int(input("Enter n1:"))
output1 = sumOneton(n1)
print("The sum no is :",output1)




