try:
  num1,num2=eval(input("Enter two numbers with a comma between: \n"))
  result=num1/num2
  print("The result is:",result)

except ZeroDivisionError:
  print("Division by zero is error !!")
except SyntaxError:
  print("Numbers are wrong. Print like this: 3,8 ")
except:
  print("Wrong Input")
else:
    print("No exceptions")

finally:
    print("This will execute no matter what")


