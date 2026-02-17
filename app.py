import streamlit as st
import string

# --- THE LOGIC (Adapted from your code) ---
def check_pwd_logic(password):
    lower_count = upper_count = num_count = wspace_count = special_count = 0
    
    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    strength = 0
    if lower_count >= 1: strength += 1
    if upper_count >= 1: strength += 1
    if num_count >= 1: strength += 1
    if wspace_count >= 1: strength += 1
    if special_count >= 1: strength += 1
    
    return strength, lower_count, upper_count, num_count, wspace_count, special_count

# --- THE UI (Streamlit) ---
st.set_page_config(page_title="PWD Checker", page_icon="🔒")
st.title("🔒 Password Strength Checker")
st.write("Enter a password below to see how secure it is.")

password = st.text_input("Enter Password:", type="password")

if password:
    strength, low, up, num, space, spec = check_pwd_logic(password)
    
    # 1. Visual Progress Bar
    # Mapping strength (1-5) to a 0.0 - 1.0 scale for the bar
    st.progress(strength / 5)
    
    # 2. Display Remarks
    remarks = [
        "Empty", 
        "🔴 Very Bad Password!!! Change ASAP", 
        "🟠 Not A Good Password!!! Change ASAP", 
        "🟡 It's a weak password, consider changing", 
        "🟢 It's a hard password, but can be better", 
        "🔵 A very strong password"
    ]
    
    st.subheader(f"Strength Score: {strength}/5")
    st.info(f"**Hint:** {remarks[strength]}")

    # 3. Visual Stats (Columns)
    st.write("### Character Breakdown:")
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Lower", low)
    col2.metric("Upper", up)
    col3.metric("Numbers", num)
    col4.metric("Spaces", space)
    col5.metric("Special", spec)