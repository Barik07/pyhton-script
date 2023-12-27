"""x = int(input("enter the value of x :"))
if(x<0):
    print("Enter the value is Negetive")
else:
    print("Enter the value is Positive")"""



"""x = int(input("enter the number:"))
if(x%2==0):
    print("Enter the number is even")
else:
    print("Enter the number is odd")"""


'''cost_price = int(input("enter the cost price:"))
sell_price = int(input("enter the sell price :"))
if(sell_price > cost_price):
    print("seller has made profit:", sell_price - cost_price,"Rupees")
elif(sell_price < cost_price):
    print("seller has made loss",cost_price - sell_price ,"Rupees" )
elif(sell_price == cost_price):
    print("seller has made no profit no loss")'''


"""mark = int(input("enter the student mark:"))
if(mark > 80):
    print("verry good")
elif(mark > 60):
    print("good")
elif(mark > 40):
    print("Average")
elif(mark <= 40 ):
   print("Fail")"""



# eng_marks = int(input("Enter the English mark of riya:"))
# math_marks = int(input("Enter the Math mark of riya:"))
# if(eng_marks > 80 and math_marks > 80):
#     print("Riya is a A grade student")
# elif(eng_marks > 80 or math_marks > 80):
#     print("Riya is a B grade student")
# else:
#     print("C grade")



# number = int(input("Enter the number:"))
# if(number >= 1000 and number <= 9999):
#     print("its a 4 digit number")
# else:
#     print("its not a 4 digit number")



# n1 = int(input("Enter 1st number:"))
# n2 = int(input("Enter 2nd number:"))
# n3 = int(input("Enter 3rd number:"))
# if(n1>n2 and n1>n3):
#     print("The grater number is",n1)
# elif(n2>n1 and n2>n3):
#     print("The grater number is",n2)
# else:
#     print("The grater number is",n3)



# Nested if-else

# n1 = int(input("Enter 1st number:"))
# n2 = int(input("Enter 2nd number:"))
# n3 = int(input("Enter 3rd number:"))
# if(n1>n2):
#     if(n1>n3):
#         print(n1,"is grater")
#     else:
#         print(n3,"is grater")
# else:
#     if(n2>n3):
#         print(n2,"is grater")
#     else:
#         print(n3,"is grater")



n = int(input("Enter the number:"))
if(n % 15 ==0):
    print("it is divisible by 15")
else:
    if(n % 3 == 0 or n % 5 ==0):
        print("its divisible by 3 or 5")
    else:
        print("its nither divisible by 3 nor 5")






















