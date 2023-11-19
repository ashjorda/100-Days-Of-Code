from art import logo

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Divide
def divide(n1, n2):
  return n1 / n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

operations = {
  "+": add,
  "-": subtract, 
  "/": divide, 
  "*": multiply
}

def calculator():
  print(logo)
  num1 = float(input("what's the first number?: "))
  for operation in operations:
    print(operation)
  
  keep_going = True
  while keep_going:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    result = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")
    user_choice = input(f"Type 'y' to continue calcuating with {result}, or type 'n' to start a new calculation: ")
  
    if user_choice == 'y':
      num1 = result
    elif user_choice == 'n':
      keep_going = False
      calculator()

calculator()