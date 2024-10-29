def calculator():
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))
  operation = input("Enter operation (+, -, *, /): ")
  if operation == '+':
    print(num1 + num2)
  elif operation == '-':
    print(num1 - num2)
  elif operation=="*":
    print(num1*num2)  
  elif operation == '/':
    if num2 != 0:
      print(num1 / num2)
    else:
      print("Cannot divide by zero")
  else:
    print("Invalid operation")
def calculator2():
  expression = input("Enter an expression: ")
  result = eval(expression)
  print(result)
print("Welcome to the calculator! Here are 2 calculators, one takes separate arguments and the other takes an expression like '2+2'. Try to learn more.\n")
while True:
  ask = input("Which calculator do you want to use? (calculator1 or calculator2 (1 / 2). Press 'q' to quit.): ")
  if ask == '1':
    calculator()
  elif ask == '2':
    calculator2()
  elif ask == 'q':
    break
  else:
    print("Please enter a valid option.")
print("Thanks for using Calculator")