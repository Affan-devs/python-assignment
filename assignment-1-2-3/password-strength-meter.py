import re
import random
import streamlit as st

# Streamlit UI
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")
st.title("🔐 Password Strength Checker")
st.markdown("Check how strong your password is and get suggestions to improve it.")

def check_password_strength(password):
    score = 0
    suggestions = []

    # Generate random additions for suggestions
    random_number = random.randint(1, 9)
    random_special = random.choice(['!', '@', '#', '$', '%', '^', '&', '*'])

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("🔴 Your password should be **at least 8 characters** long.")

    # Check for uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("🔴 Include **both uppercase and lowercase** letters.")

    # Check for at least one digit
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("🔴 Add **at least one number (0-9)**.")
        suggestions.append(f"💡 Try this: `{password}{random_number}`")

    # Check for at least one special character
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("🔴 Add **at least one special character** (!@#$%^&*).")
        suggestions.append(f"💡 Try this: `{password[:1]}{random_special}{password[1:]}`")

    return score, suggestions



# Input field
password = st.text_input("Enter your password", type="password")

# Button
if st.button("Check Strength"):
    if password:
        score, suggestions = check_password_strength(password)

        # Display feedback
        for tip in suggestions:
            st.write(tip)

        # Final message
        if score == 4:
            st.success("✅ Strong Password!")
            st.code(password)
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider improving it for more security.")
        else:
            st.error("❌ Weak Password - Please improve it using the above suggestions.")
            st.code("Avoid simple passwords like: password123")
    else:
        st.warning("⚠️ Please enter a password to evaluate.")
