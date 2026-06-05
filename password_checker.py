from colorama import Fore, Style, init
init()

def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z)")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9)")

    special = "!@#$%^&*()_+-=[]{}|;':,./<>?"
    if any(c in special for c in password):
        score += 1
    else:
        feedback.append("Add a special character like !@#$")

    return score, feedback


password = input("Enter a password to check: ")
score, feedback = check_password(password)

if score <= 1:
    strength = "WEAK"
    color = Fore.RED
elif score <= 3:
    strength = "MEDIUM"
    color = Fore.YELLOW
else:
    strength = "STRONG"
    color = Fore.GREEN

print("\n--- Password Strength ---")
print("Score:", score, "/ 4")
print("Strength:", color + strength + Style.RESET_ALL)

if feedback:
    print("\nHow to improve:")
    for tip in feedback:
        print(" -", tip)
else:
    print(Fore.GREEN + "\nGreat password! No improvements needed." + Style.RESET_ALL)