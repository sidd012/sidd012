import math 
def add(x,y):
    return x+y
def substraction(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y
print("select operation.")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
print("5.default value")

while True:
  choice=input("enter choice (1/2/3/4/5):")
  if choice in ('1','2','3','4','5'):
      try:
          num=float(input("enter the first number"))
          num=float(input("enter the second number"))
      except ValueError:
          print("invalid input.please enter a number.")
          continue
      

       if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
       elif choice=='2':
          print(num1, "-" , numm2,"=",subtract(num1,num2))

       elif choice=='3':
          print(num1,"*",num2,"="multiply(num1,num2))
       elif choice=='4':
          print(num1,"/",num2,"=",divide(num1,num2))

          next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")

