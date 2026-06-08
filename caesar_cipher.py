from colorama import Fore, Style, init
init()

def encrypt(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(message, shift):
    return encrypt(message, -shift)

def brute_force(message):
    print(Fore.YELLOW + "\n--- Brute Force Attack --- All 26 possible shifts ---" + Style.RESET_ALL)
    for shift in range(1, 26):
        print(f"Shift {shift:2d} : {encrypt(message, -shift)}")

def menu():
    print(Fore.CYAN + """
=====================================
   CAESAR CIPHER TOOL
   By Prikshit | SJVN Internship
=====================================""" + Style.RESET_ALL)

    while True:
        print(Fore.YELLOW + """
1. Encrypt a message
2. Decrypt a message
3. Brute Force crack a message
4. Exit
""" + Style.RESET_ALL)

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            msg = input("Enter message to encrypt: ")
            shift = int(input("Enter shift number (1-25): "))
            result = encrypt(msg, shift)
            print(Fore.GREEN + f"\nEncrypted: {result}" + Style.RESET_ALL)

        elif choice == "2":
            msg = input("Enter message to decrypt: ")
            shift = int(input("Enter shift number used to encrypt: "))
            result = decrypt(msg, shift)
            print(Fore.GREEN + f"\nDecrypted: {result}" + Style.RESET_ALL)

        elif choice == "3":
            msg = input("Enter encrypted message to brute force: ")
            brute_force(msg)

        elif choice == "4":
            print(Fore.CYAN + "\nGoodbye, Agent!" + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "Invalid choice. Enter 1-4." + Style.RESET_ALL)

menu()