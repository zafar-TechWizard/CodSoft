from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return "Error! Division by zero."
    else:
        return result

def display_operations():
    print(Fore.YELLOW + "Operations:")
    print("1. " + Fore.GREEN + "Addition " + Fore.YELLOW + "(+)")
    print("2. " + Fore.GREEN + "Subtraction " + Fore.YELLOW + "(-)")
    print("3. " + Fore.GREEN + "Multiplication " + Fore.YELLOW + "(*)")
    print("4. " + Fore.GREEN + "Division " + Fore.YELLOW + "(/)")
    print("5. " + Fore.GREEN + "Exit")

# ASCII art for decoration
print(Fore.CYAN + "Welcome to Simple Calculator")
print(Fore.CYAN + "=============================")

while True:
    display_operations()

    try:
        choice = int(input(Fore.MAGENTA + "Enter the number corresponding to the desired operation: " + Fore.WHITE))
        if choice == 5:
            print(Fore.YELLOW + "Exiting the calculator. Goodbye!")
            break
        elif choice not in [1, 2, 3, 4]:
            raise ValueError
    except ValueError:
        print(Fore.RED + "Invalid input. Please select a valid operation.")
    else:
        num1 = float(input(Fore.MAGENTA + "Enter the first number: " + Fore.WHITE))
        num2 = float(input(Fore.MAGENTA + "Enter the second number: " + Fore.WHITE))

        print("-----------------------------")
        if choice == 1:
            print(Fore.YELLOW + "Result: " + Fore.GREEN + f"{num1} + {num2} =", add(num1, num2))
        elif choice == 2:
            print(Fore.YELLOW + "Result: " + Fore.GREEN + f"{num1} - {num2} =", subtract(num1, num2))
        elif choice == 3:
            print(Fore.YELLOW + "Result: " + Fore.GREEN + f"{num1} * {num2} =", multiply(num1, num2))
        elif choice == 4:
            result = divide(num1, num2)
            if isinstance(result, str):
                print(Fore.RED + "Error: " + result)
            else:
                print(Fore.YELLOW + "Result: " + Fore.GREEN + f"{num1} / {num2} =", result)
        print("-----------------------------")
