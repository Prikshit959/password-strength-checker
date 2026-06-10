import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from colorama import Fore, Style, init
init()

# ================================
# BUILT-IN DATASET
# ================================
emails = [
    # PHISHING EMAILS
    ("Urgent! Your account has been suspended. Click here to verify your credentials immediately.", 1),
    ("Your bank account has been compromised. Login now to secure your account.", 1),
    ("Congratulations! You have won $1,000,000. Click here to claim your prize now.", 1),
    ("Alert: Unusual login detected. Verify your identity immediately or account will be locked.", 1),
    ("Your PayPal account is limited. Please confirm your information to restore access.", 1),
    ("URGENT: Your password expires today. Click here to update your password immediately.", 1),
    ("Dear customer, your account will be terminated. Verify now to avoid suspension.", 1),
    ("You have a pending payment. Click here to confirm your bank details.", 1),
    ("Security alert: Someone tried to access your account. Verify your identity now.", 1),
    ("Your Netflix subscription has expired. Update your payment details to continue.", 1),
    ("Win a free iPhone! Click here to claim your reward before it expires.", 1),
    ("Action required: Confirm your email address or lose access to your account.", 1),
    ("Your Amazon order cannot be delivered. Update your address details immediately.", 1),
    ("IRS Notice: You owe back taxes. Pay immediately to avoid legal action.", 1),
    ("Your Google account was accessed from a new device. Verify now.", 1),
    ("Congratulations! You are selected for a cash reward. Provide your details.", 1),
    ("WARNING: Your computer has a virus. Call our support number immediately.", 1),
    ("Your credit card has been charged. If not you, click here to dispute.", 1),
    ("Verify your account within 24 hours or it will be permanently deleted.", 1),
    ("You have unclaimed funds. Provide your bank details to receive transfer.", 1),
    ("Dear user, click here to reset your password before account expires.", 1),
    ("Your package is on hold. Pay the customs fee to release your delivery.", 1),
    ("Login attempt from unknown device. Confirm your identity immediately.", 1),
    ("Your account has been hacked. Change your password now by clicking here.", 1),
    ("Free gift card! Complete a survey to claim your $500 Amazon gift card.", 1),

    # SAFE EMAILS
    ("Hi team, please find attached the minutes from today's meeting.", 0),
    ("Reminder: Project deadline is next Friday. Please submit your reports.", 0),
    ("Good morning! Just checking in to see how the project is progressing.", 0),
    ("Please review the attached document and share your feedback by Thursday.", 0),
    ("Team lunch is scheduled for tomorrow at 1 PM in the conference room.", 0),
    ("Happy birthday! Wishing you a wonderful day filled with joy.", 0),
    ("The quarterly report has been uploaded to the shared drive for review.", 0),
    ("Can we schedule a call this week to discuss the project requirements?", 0),
    ("I have attached the invoice for last month services. Please process it.", 0),
    ("Thank you for your help with the presentation. It went really well!", 0),
    ("Just a reminder about our weekly standup meeting tomorrow at 10 AM.", 0),
    ("Please find attached the updated project timeline for your reference.", 0),
    ("The training session next week has been moved to the afternoon slot.", 0),
    ("Hope you are doing well! Let us catch up over coffee this week.", 0),
    ("Your leave request has been approved for the dates you requested.", 0),
    ("The new office guidelines have been updated. Please read and acknowledge.", 0),
    ("Congratulations on your promotion! Well deserved and looking forward to working together.", 0),
    ("The system maintenance is scheduled for Sunday between 2 AM and 4 AM.", 0),
    ("Please confirm your attendance for the annual company picnic next Saturday.", 0),
    ("Your expense report has been approved and will be reimbursed this Friday.", 0),
    ("Meeting agenda for tomorrow has been shared on the team calendar.", 0),
    ("The new software update is ready. IT will deploy it tonight after hours.", 0),
    ("Welcome to the team! We are excited to have you on board.", 0),
    ("Please submit your timesheet by end of day Friday for payroll processing.", 0),
    ("The client presentation went well. They are happy with the proposal.", 0),
]

# ================================
# STEP 1 - Prepare data
# ================================
print(Fore.CYAN + "\n=== Phishing Email Detector ===" + Style.RESET_ALL)
print(Fore.CYAN + "=== MITRE ATT&CK: T1566 Phishing ===" + Style.RESET_ALL)

df = pd.DataFrame(emails, columns=['email', 'label'])
print(f"\nDataset loaded!")
print(f"Total emails   : {len(df)}")
print(f"Phishing emails: {len(df[df['label']==1])}")
print(f"Safe emails    : {len(df[df['label']==0])}")

# ================================
# STEP 2 - Train model
# ================================
print(Fore.YELLOW + "\nTraining model..." + Style.RESET_ALL)

X = df['email']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer(stop_words='english', lowercase=True)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_vec, y_train)

# ================================
# STEP 3 - Show accuracy
# ================================
y_pred = model.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred) * 100

print(Fore.GREEN + f"Model trained successfully!" + Style.RESET_ALL)
print(f"Accuracy: {Fore.GREEN}{accuracy:.1f}%{Style.RESET_ALL}")

# ================================
# STEP 4 - Predict new emails
# ================================
def predict_email(email_text):
    vec = vectorizer.transform([email_text])
    prediction = model.predict(vec)[0]
    probability = model.predict_proba(vec)[0]

    if prediction == 1:
        confidence = probability[1] * 100
        print(Fore.RED + f"\n⚠ PHISHING DETECTED! Confidence: {confidence:.1f}%" + Style.RESET_ALL)
        print(Fore.RED + "  Do NOT click any links in this email!" + Style.RESET_ALL)
        print(Fore.YELLOW + "\n  MITRE ATT&CK: T1566 - Phishing" + Style.RESET_ALL)
        print(Fore.YELLOW + "  More info: https://attack.mitre.org/techniques/T1566/" + Style.RESET_ALL)
    else:
        confidence = probability[0] * 100
        print(Fore.GREEN + f"\n✓ SAFE EMAIL. Confidence: {confidence:.1f}%" + Style.RESET_ALL)
        print(Fore.GREEN + "  This email appears legitimate." + Style.RESET_ALL)

# ================================
# STEP 5 - Menu
# ================================
print(Fore.CYAN + "\n=== Email Checker Ready ===" + Style.RESET_ALL)

while True:
    print(Fore.YELLOW + "\n1. Check an email" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. Exit" + Style.RESET_ALL)
    choice = input("\nEnter choice (1-2): ").strip()

    if choice == "1":
        print("\nPaste your email text below and press Enter twice:")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        email_text = " ".join(lines)
        if email_text:
            predict_email(email_text)
    elif choice == "2":
        print(Fore.CYAN + "\nGoodbye!" + Style.RESET_ALL)
        break
    else:
        print(Fore.RED + "Enter 1 or 2 only" + Style.RESET_ALL)