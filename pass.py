import random
import string
import secrets

def passchecker(password):
  length=len(password)
  if length<=8:
    return "Weak password. Try again"
  elif length<=12 and length>8:
    strength="Medium"
  else:
    strength="Strong"
  hasupper=0
  haslower=0
  hasspec=0
  hasnum=0
  i=0
  while i<length:
    char=password[i]
    if ord(char)>=65 and ord(char)<=90:
      hasupper=1
    elif ord(char)<=48 and ord(char)>=57:
      hasnum=1
    elif ord(char)>=97 and ord(char)<=122:
      haslower=1
    elif (ord(char)<=33 and ord(char)>=47) or (ord(char)>=58 and ord(char)<=64) or (ord(char)>=91 and ord(char)<=96) or (ord(char)>=123 and ord(char)<=126):
      hasspec=1
    i+=1
missing=""
if hasupper==0:
  missing+="Uppercase character"
elif haslower==0:
  missing+="Lowercase character"
elif hasnum==0:
  missing+="Number"
else:
  missing+="Special characters"
if len(missing)>0:
  return strength+"- Missing "+missing
else:
  return strength+"Perfect"



def randompass(length):
  character="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"
  password=""
  for _ in range(length):
    password += secrets.choice(chars)
  return password


while True:
    print("=== PASSWORD TOOLS ===")
    print("1. Check Password Strength")
    print("2. Generate Random Password") 
    print("3. Exit")
    
    choice = input("Choose (1-3): ")
    
    if choice == "1":
        password = input("Enter password: ")
        result = check_password_strength(password)
        print("RESULT: " + result)
        
    elif choice == "2":
        length_str = input("Enter length (8-50): ")
        try:
            length = int(length_str)
            if length >= 8 and length <= 50:
                password = generate_password(length)
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
