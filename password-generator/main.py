import random
import time
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)



def generate_password(length):
    C = "abcdefghijklmnopqrstuvwxyz"
    UC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    D = "0123456789"
    S = "!@#$%^&*()-_+=<>?/.,:;"
    password = ''.join([random.choice(C) for _ in range(length // 4)]+
        [random.choice(UC) for _ in range(length // 4)]+
        [random.choice(D) for _ in range(length // 4)]+
        [random.choice(S) for _ in range(length // 4)]+
        [random.choice(C + UC + D + S) for _ in range(length % 4)]
        )
    
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password

# def generate_password(length):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for _ in range(length))
#     return password

# ASCII art for decoration
print(Fore.CYAN + "Welcome to Password Generator")
print(Fore.CYAN + "=============================")

try:
    length = int(input(Fore.MAGENTA + "Enter the desired length of the password: " + Fore.WHITE))
    if length <= 0:
        raise ValueError
except ValueError:
    print(Fore.RED + "Invalid input. Please enter a positive integer for the length.")
else:
    password = generate_password(length)
    print("-----------------------------")
    # print(Fore.YELLOW + "Generated Password: " + Fore.GREEN + password)
    print(Fore.YELLOW + "Generated Password: ", end = '')
    for chrt in password:
        print(Fore.GREEN + chrt, end ='', flush=True)
        time.sleep(0.03)
    print()
    print("-----------------------------")
