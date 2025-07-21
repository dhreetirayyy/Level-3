num = int(input("Enter a number: "))
def check_number(num):
    if num<0:
        print("Negative Number. Stopping function")
        return num 
    else:
        print(f"The number {num} is positive.")
check_number(num)