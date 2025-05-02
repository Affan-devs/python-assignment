import re 
import random
random_number = random.randint(1, 5)
random_special = random.choice(['!', '@', '#', '$', '%', '^', '&', '*'])
def check_password_strength(password):
    score = 0
    
    if len(password) >= 8:
        score += 1
    else:
        print("❌ Password should be at least 8 characters long.")


    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        print("❌ Include both uppercase and lowercase letters.")
    

    if re.search(r"\d", password):
        score += 1
    else:
        print("❌ Add at least one number (0-9).")
        result = password + str(random_number)
        print(f"You can have password like this {result}")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        print("❌ Include at least one special character (!@#$%^&*).")
        result = password[:1] + str(random_special)
        print(f"You can have password like this {result}")
    
    if score == 4:
        print("✅ Strong Password!")
        print(password)
    elif score == 3:
        print("⚠️ Moderate Password - Consider adding more security features.")
    else:
        print("❌ Weak Password - Improve it using the suggestions above.")
        error =password = 'password123'
        print(f"You can't have password like this {error}")
password = input("Enter your password: ")
check_password_strength(password)