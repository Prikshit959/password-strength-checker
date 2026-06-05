# Password Strength Checker with MITRE ATT&CK Integration

A cybersecurity tool built in Python that analyzes password strength and maps 
weaknesses to real MITRE ATT&CK attack techniques.

## Features
- Checks password strength on 4 parameters
- Color coded output (Red/Yellow/Green)
- Detects 100 most common passwords instantly
- Maps weak passwords to real MITRE ATT&CK techniques
- Gives specific improvement tips

## MITRE ATT&CK Techniques Covered
- T1110 - Brute Force
- T1110.001 - Password Guessing
- T1110.002 - Password Cracking
- T1110.003 - Password Spraying
- T1589.001 - Credential Stuffing

## How to Run

Install required library:
pip install colorama

Run the tool:
python "passwrod checker.py"

## Example Output

Enter a password to check: password123

[!] DANGER - This is one of the most common passwords!
    Attackers try these first. Change it immediately.
    MITRE ATT&CK: T1110.002 - Password Cracking

--- Password Strength ---
Score: 2 / 4
Strength: MEDIUM

How to improve:
 - Add at least one uppercase letter (A-Z)
 - Add a special character like !@#$

## Built By
Name: [prikshit sharma]
Internship: SJVN Limited, Shimla
Stack: Python, Colorama, MITRE ATT&CK Framework