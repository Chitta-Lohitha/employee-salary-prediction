from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model
with open('salary_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the dataset to ensure correct label encoding
df = pd.read_csv('Salary Data.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        # Get form data
        age = int(request.form['age'])
        gender = request.form['gender']
        education = request.form['education']
        job = request.form['job']
        experience = float(request.form['experience'])

        # Create dataframe for prediction
        input_df = pd.DataFrame([{
            'Age': age,
            'Gender': gender,
            'Education Level': education,
            'Job Title': job,
            'Years of Experience': experience
        }])

        # Make prediction
        prediction = model.predict(input_df)[0]

    # For dropdowns
    genders = sorted(df['Gender'].dropna().unique())
    educations = sorted(df['Education Level'].dropna().unique())
    jobs = sorted(df['Job Title'].dropna().unique())

    return render_template('index.html', prediction=prediction,
                           genders=genders, educations=educations, jobs=jobs)

if __name__ == '__main__':
    app.run(debug=True)
