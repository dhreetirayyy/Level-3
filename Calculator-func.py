def add(A, B):
    return A + B 
def subtract(A, B):
    return  A - B
def multiply(A, B):
    return A * B
def divide(A, B):
    return A/B
print("Select which operation:")
print("a. Add")
print("b. Subtract")
print("c. Mulitply")
print("d. Divide")
choice = input(" Please enter choice (a/b/c/d):")
num1 = int(input("Please enter first number:"))
num2 = int(input("Please enter second number:"))
if choice == 'a':
    print(num1, "+", num2, "=", add(num1,num2))
elif choice == 'b':
    print(num1, "-", num2, "=", subtract(num1,num2))
elif choice == 'c':
    print(num1, "*", num2, "=", multiply(num1,num2))
elif choice == 'd':
    print(num1, "/", num2, "=", divide(num1,num2))
else:
    print("This is an invaild input")