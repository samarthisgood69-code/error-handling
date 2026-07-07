try:
    v=int(input("enter a number: "))
    print("the number entered is",v)
except ValueError as ex:
    print("Exception:", ex)