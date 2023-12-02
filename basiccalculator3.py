def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b  

def divide(a, b):
    return a / b

print("Select operation:")
print("1. Add") 
print("2. Subtract") 
print("3. Multiply")
print("4. Divide")

prev_result = 0
continue_calc = 'y'

while continue_calc == 'y':

    if prev_result != 0:
        print("Previous Result: ", prev_result)

    choice = input("Operation (1/2/3/4): ")

    if prev_result != 0:
        num1 = prev_result  
        num2 = float(input("Next Number: "))
    else:
        num1 = float(input("Number 1: "))
        num2 = float(input("Number 2: "))

    if choice == '1': 
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    else:
        result = 0

    prev_result = result

    print("Result =",result)
    continue_calc = input("\nContinue? (y/n) ")

print("Bye!")