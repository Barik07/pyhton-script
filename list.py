car = ["jaguar","tata","suzuki","mahindra"]
print(car)
print(type(car))
print(len(car))
print(car[2])
print(car[-1])
car.append("audi")
print(car)
car.insert(1,"mercidis")
print(car)
car2= ["thur","hawai"]
car.extend(car2)
print(car)
car.remove("mahindra")
print(car)
car.pop(4)
print(car)

# if "suzuki" in car:
#  print("this is avalable in car") 
# else:
#  print("this is not avalable in car")