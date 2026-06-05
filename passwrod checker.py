from colorama import Fore, Style, init
init()

common_passwords = [
    "password", "123456", "password123", "admin", "letmein",
    "welcome", "monkey", "dragon", "master", "sunshine",
    "princess", "abc123", "qwerty", "111111", "iloveyou",
    "1234567", "12345678", "123456789", "1234567890", "000000",
    "superman", "batman", "football", "shadow", "michael",
    "jessica", "letmein1", "passw0rd", "hello123", "admin123",
    "root", "toor", "pass", "test", "guest", "login",
    "changeme", "secret", "baseball", "soccer", "hockey",
    "killer", "george", "jordan", "harley", "ranger",
    "daniel", "master1", "jennifer", "thomas", "1q2w3e",
    "zxcvbnm", "asdfgh", "qazwsx", "trustno1", "password1",
    "password12", "pass123", "abc1234", "welcome1", "monkey1",
    "sunshine1", "princess1", "dragon1", "access", "matrix",
    "whatever", "donald", "charlie", "andrew", "mustang",
    "jessica1", "pepper", "shadow1", "superman1", "batman1",
    "starwars", "hello", "freedom", "computer", "tigger",
    "ginger", "cheese", "butter", "chicken", "hammer",
    "summer", "winter", "spring", "autumn", "flower",
    "guitar", "purple", "orange", "yellow", "silver",
    "golden", "crystal", "diamond", "rainbow", "thunder",
    "lightning", "tornado", "cyclone", "phoenix", "falcon"
]

mitre_techniques = {
    "length": {
        "id": "T1110.001",
        "name": "Password Guessing",
        "detail": "Short passwords are easily guessed by attackers"
    },
    "uppercase": {
        "id": "T1110.003",
        "name": "Password Spraying",
        "detail": "Simple passwords are used in spraying attacks"
    },
    "number": {
        "id": "T1110",
        "name": "Brute Force",
        "detail": "Passwords without numbers are cracked faster"
    },
    "special": {
        "id": "T1589.001",
        "name": "Credential Stuffing",
        "detail": "Weak passwords appear in leaked credential databases"
    }
}

def check_password(password):
    score = 0
    feedback = []
    attacks = []

    if password.lower() in common_passwords:
        print(Fore.RED + "\n[!] DANGER - This is one of the most common passwords!" + Style.RESET_ALL)
        print(Fore.RED + "    Attackers try these first. Change it immediately." + Style.RESET_ALL)
        print(Fore.YELLOW + "\n    MITRE ATT&CK: T1110.002 - Password Cracking" + Style.RESET_ALL)
        print(Fore.YELLOW + "    More info: https://attack.mitre.org/techniques/T1110/002/" + Style.RESET_ALL)

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")
        attacks.append("length")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z)")
        attacks.append("uppercase")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9)")
        attacks.append("number")

    special = "!@#$%^&*()_+-=[]{}|;':,./<>?"
    if any(c in special for c in password):
        score += 1
    else:
        feedback.append("Add a special character like !@#$")
        attacks.append("special")

    return score, feedback, attacks


password = input("Enter a password to check: ").strip()
password = input("Enter a password to check: ").strip()
print("You typed:", repr(password))
score, feedback, attacks = check_password(password)

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

if attacks:
    print(Fore.RED + "\n--- MITRE ATT&CK Techniques Your Password is Vulnerable To ---" + Style.RESET_ALL)
    for key in attacks:
        t = mitre_techniques[key]
        print(f"\n {t['id']} - {t['name']}")
        print(f"  {t['detail']}")
        print(f"  More info: https://attack.mitre.org/techniques/{t['id'].replace('.', '/')}/")