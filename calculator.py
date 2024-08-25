def calculator():
    print("Welcome to the Python Calculator")
    print("Enter 'exit' to quit")
    while True:
        num = input("Enter the first number: ")

        if num.lower() == 'exit':
            print("Goodbye!")
            exit()

        if num.replace('.', '', 1).isdigit():
            num = float(num)
        else:
            print("Invalid input. Please enter a valid number.")
            continue
        
        
        operation = input("Enter the operation (+, -, *, /): ")
        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Please try valid operations.")
            continue

        num2 = input("Enter the Second number: ")
        if num2.replace('.', '', 1).isdigit():
            num2= float(num2)
        else:
            print("Invalid input. Please enter a valid number.")
            continue

        if operation == '+':
            result = num + num2
        elif operation == '-':
            result = num - num2
        elif operation == '*':
            result = num * num2
        elif operation == '/':
            if num2 != 0:
                result = num / num2
            else:
                print("Error: Division by zero.")
                continue

        print(f"The result of {num} {operation} {num2} is: {result}")

if __name__ == "__main__":
    calculator()

