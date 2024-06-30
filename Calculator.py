
# Define a function for addition
def add(x, y):
    return x + y

# Define a function for subtraction
def sub(x, y):
    return x - y

# Define a function for multiplication
def mul(x, y):
    return x * y

# Define a function for division
def div(x, y):
    return x / y

print("Please select operation -\n"
      "1. Add\n"
      "2.ß Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")

# Take input from the user
select = int(input("Select operations from 1, 2, 3, 4 :"))

x = int(input("Enter first number: "))
y = int(input("Select second number: "))

if select == 1:
    print(add(x, y))

elif select == 2:
    print(sub(x, y))

elif select == 3:
    print(mul(x, y))

elif select == 4:
    print(div(x, y))

else:
    print("Invalid input")