try:
    num1, num2=eval(input("enter the number,seperated by comma: "))
    result=num1/num2
    print("Result is: ", result)
except ZeroDivisionError:
    print("Division by zero is error!!")
except SyntaxError:
    print("comma is missing enter the number seperately like this 1,2")
except:
    print("wrong input")
else:
    print("no exception")
finally:
    print("no error")
