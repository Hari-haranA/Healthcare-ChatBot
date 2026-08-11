# app.py
from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the dataset into a DataFrame
data = pd.read_csv('transformed_data.csv')

# Function to predict the disease based on symptoms
def predict_disease(symptoms):
    # Split user-input symptoms into a list
    user_symptoms = [symptom.strip() for symptom in symptoms.split(',')]

    # Initialize a list to store matching diseases
    matching_diseases = []

    # Iterate through each row in the dataset
    for index, row in data.iterrows():
        disease = row['Diseases']
        dataset_symptoms = [symptom.strip() for symptom, value in row.items() if symptom != 'Diseases' and value.lower() == 'yes']

        # Check if all user's symptoms are present in the dataset symptoms
        if all(symptom in dataset_symptoms for symptom in user_symptoms):
            matching_diseases.append(disease)

    # Return matching diseases as a string
    if matching_diseases:
        return ', '.join(matching_diseases)
    else:
        return "I couldn't find a matching disease."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    user_input = request.form['user_input']
    disease_prediction = predict_disease(user_input)
    return jsonify({'bot_response': disease_prediction})

if __name__ == "__main__":
    app.run(debug=True)
