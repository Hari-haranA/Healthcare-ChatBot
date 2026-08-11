import pandas as pd
from flask import Flask, render_template, request, session, url_for

app = Flask(__name__)

# Load the dataset into a DataFrame
data = pd.read_csv('transformed_data.csv')

# Function to predict the disease based on symptoms
def predict_disease(symptoms):
    user_symptoms = [symptom.strip() for symptom in symptoms.split(',')]
    matching_diseases = []

    for index, row in data.iterrows():
        disease = row['Diseases']
        dataset_symptoms = [symptom.strip() for symptom, value in row.items() if symptom != 'Diseases' and value.lower() == 'yes']
        
        if all(symptom in dataset_symptoms for symptom in user_symptoms):
            matching_diseases.append(disease)

    if matching_diseases:
        return [{'disease': disease} for disease in matching_diseases]
    else:
        return "I couldn't find a matching disease. Please provide correct symptoms."

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['age'] = request.form['age']
        return render_template('chat.html', name=session['name'], age=session['age'])

    return render_template('index.html')

# Route for the chat page
@app.route('/chat')
def chat():
    name = session.get('name')
    age = session.get('age')
    return render_template('chat.html', name=name, age=age)

# Route for handling the user input and displaying the prediction
@app.route('/send_query', methods=['POST'])
def send_query():
    name = session.get('name', 'Guest')
    age = session.get('age', '')
    user_query = request.form['user_query']

    disease_predictions = predict_disease(user_query)

    if isinstance(disease_predictions, list) and len(disease_predictions) > 0:
        # Assume the first disease in the list for simplicity
        disease_name = disease_predictions[0]['disease']
        bot_message = f"Dear {name}, your symptoms: {user_query}.\nPredicted disease: {disease_name}.\nDo you have any other symptoms from the list?"
    else:
        bot_message = "I couldn't find a matching disease. Please provide correct symptoms."

    return render_template('chat.html', name=name, age=age, user_query=user_query, bot_message=bot_message)
# Route for handling the closure of the chat window
@app.route('/chat_closed')
def chat_closed():
    return render_template('chat_closed.html')

if __name__ == "__main__":
    app.run(debug=True)
