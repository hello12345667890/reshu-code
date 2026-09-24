def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b): 
    return a/b
def main():
  try:
    num1=float(input("Enter your first number: "))
    num2=float(input("Enter your second number:"))
    print(add(num1, num2))
    print(subtract(num1, num2))
    print(multiply(num1, num2))
    print(divide(num1, num2))
  except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
  except ValueError:
         print("Error: Please enter valid numbers only!")


main()



