num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter an operation: ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2

too = open("вывод.txt", "w")

too.write(str(result))

too.close()
