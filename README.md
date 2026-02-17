# 🔒 Advanced Password Strength Checker

A real-time, visual web application built with **Python** and **Streamlit**. This tool evaluates the security of passwords by analyzing character types and providing immediate, color-coded feedback.



## 🚀 Live Demo
https://password-strength-checker-npyty5lnsxdjypidrq4dc4.streamlit.app

## ✨ Features
* **Live Analysis:** Evaluates strength instantly as the user types.
* **Visual Progress Bar:** Dynamic bar that shifts from Red (Weak) to Blue (Strong).
* **Detailed Metrics:** Shows the exact count of:
  * Lowercase & Uppercase letters
  * Numerical digits
  * Whitespaces
  * Special characters (@, #, $, etc.)
* **Smart Hints:** Provides clear instructions on how to make the password harder to crack.

## 🛠️ Tech Stack
* **Language:** Python 3.11.5
* **Framework:** Streamlit (Web UI)
* **Library:** `string` (for character classification)



## 📥 Installation & Local Setup

Follow these steps to get the project running on your local machine:

1. **Clone the repo**
   ```bash
   git clone [https://github.com/Kavee-Dilshani/password-strength-checker.git](https://github.com/Kavee-Dilshani/password-strength-checker.git)
   cd password-strength-checker

2. **Install dependencies**
   pip install -r requirements.txt

3. **Run the App**
   streamlit run app.py
