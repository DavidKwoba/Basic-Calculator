# Numbers inputted by the client
num1 = input("Enter first number: ")
num1 = float(num1)
num2 = input("Enter the second number: ")
num2 = float(num2)

# The operation to be perfomed
sign = input("Enter the operand: ")
result = 0

# Check if the sign was valid
valid = 0

# Operations
if sign == "+":
    result = num1 + num2
elif sign == "-":
    result = num1 - num2
elif sign == "*":
    result = num1 * num2
elif sign == "/":
    result = num1 / num2
elif sign == "pow":
    result = pow(num1, num2)
else:
    valid = -1
    print("Invalid operand, please put in a valid value. ")

# Print if the sign was valid
if valid == 0:
    print("The answer is " + str(result))