def calculate(operation=input("Enter the operation you want to perform: "),num1=int(input("Enter the first number: ")),num2=int(input("Enter the second number: "))):
   if operation== "multiply":
    return num1*num2
   elif operation=="add":
      return num1+num2
   elif operation=="subtract":
      return num1-num2
   elif operation=="divide":
        return num1/num2
answer=calculate()
print(answer)
