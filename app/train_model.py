import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

# Load data
df = pd.read_csv('Salary Data.csv')

# Drop missing values
df.dropna(inplace=True)

# Encode categorical features
label_encoders = {}
for col in ['Gender', 'Education Level', 'Job Title']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Features and target
X = df[['Age', 'Gender', 'Education Level', 'Job Title', 'Years of Experience']]
y = df['Salary']

# Save encoders
with open('encoders.pkl', 'wb') as f:
    pickle.dump(label_encoders, f)

# Save data as lookup
df.to_csv('processed_data.csv', index=False)
