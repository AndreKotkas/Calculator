from art import logo

def add(n1, n2):
  return n1 + n2

def substract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

Dict = {
  "+": add, 
  "-": substract, 
  "*": multiply, 
  "/": divide
}  
def calculator():
  print(logo)
  
  num1 = float(input("What is the first number?: "))
  for symbol in Dict:
    print(symbol)
  should_continue = True
  
  while should_continue:
    Dict_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))
    calculation_function =Dict[Dict_symbol]
    answer = calculation_function(num1, num2)
  
    print(f"{num1} {Dict_symbol} {num2} = {answer}")
    
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' start new calculation: ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()



    
   


 