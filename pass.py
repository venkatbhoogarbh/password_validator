import secrets
import string

def passchecker(password):
    length = len(password)
    if length <= 8:
        return "Weak password. Try again"
    elif length <= 12:
        strength = "Medium"
    else:
        strength = "Strong"

    hasupper = haslower = hasnum = hasspec = 0

    for char in password:
        if char.isupper():
            hasupper = 1
        elif char.islower():
            haslower = 1
        elif char.isdigit():
            hasnum = 1
        elif not char.isalnum():
            hasspec = 1

    missing = ""
    if hasupper == 0:
        missing += " Uppercase"
    if haslower == 0:
        missing += " Lowercase"
    if hasnum == 0:
        missing += " Number"
    if hasspec == 0:
        missing += " Special"

    if len(missing) > 0:
        return f"{strength} - Missing:{missing}"
    else:
        return f"{strength} Perfect"

def randompass(length):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(secrets.choice(chars) for _ in range(length))
    return password

while True:
    print("\n=== PASSWORD TOOLS ===")
    print("1. Check Password Strength")
    print("2. Generate Random Password") 
    print("3. Exit")
    
    choice = input("Choose (1-3): ")
    
    if choice == "1":
        password = input("Enter password: ")
        result = passchecker(password)
        print("RESULT: " + result)
        
    elif choice == "2":
        length_str = input("Enter length (8-50): ")
        try:
            length = int(length_str)
            if 8 <= length <= 50:
                password = randompass(length)
                print("PASSWORD: " + password)
            else:
                print("ERROR: Length must be 8-50")
        except:
            print("ERROR: Enter valid number")
            
    elif choice == "3":
        print("Bye!")
        break
    else:
        print("ERROR: Choose 1, 2, or 3")
