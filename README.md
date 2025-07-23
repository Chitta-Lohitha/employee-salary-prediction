# 🧠 Employee Salary Prediction

A simple ML web app using **Flask** to predict employee salaries based on user input like age, gender, education, job title & experience.

---

## 🚀 Features

- 🧮 Predict salary using a trained ML model
- 🎯 Real-time input via web form
- 🖥️ Built with Flask, HTML, CSS, and scikit-learn

---

## 🧰 Tech Stack

🐍 Python • 🧪 scikit-learn • 🌐 Flask • 🧾 Pandas • 🎨 HTML & CSS

---

## 📦 Project Structure

employee-salary-prediction/

│
├── app/

│   ├── app.py                  # Flask application

│   ├── templates/

│   │   └── index.html          # Frontend form

│   ├── encoders.pkl            # Encoded categorical feature mappings

│   ├── Salary Data.csv         # Dataset

│   ├── salary_model.pkl        # Trained ML model

│   └── train_model.py          # Model training script

│

├── src/

│   ├── data_preprocessing.py   # Data cleaning & encoding

│   └── model.py                # Model functions

│

├── .gitignore

├── requirements.txt

└── README.md


---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.8+
- pip
- Git

### 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Chitta-Lohitha/employee-salary-prediction.git
   cd employee-salary-prediction

---

🧠 Model Details
Algorithm: Linear Regression / Random Forest (customizable)

*Features:

  *Age

  *Gender

  *Education Level

  *Job Title

  *Years of Experience

*Target: Salary (numeric)

