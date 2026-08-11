import pandas as pd

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

# Main function to run the chatbot
def main():
    print("Welcome, My name is Abhirami. I am an AI healthcare assistant.")
    print("Kindly tell your symptoms, separated by commas, for disease diagnosis. Type 'exit' to quit.")

    while True:
        user_input = input("Your Symptoms: ")
        if user_input.lower() == 'exit':
            break
        disease_prediction = predict_disease(user_input)
        print("Predicted Disease(s):", disease_prediction)

if __name__ == "__main__":
    main()