import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_md")

# Define a dictionary mapping diseases to their symptoms
diseases_to_symptoms = {
    "Fungal Infection": ["itching", "skin rash", "nodal skin eruptions", "dischromic patches"],
    "Allergy": ["continuous sneezing", "shivering", "chills", "watering from eyes"],
    "GERD": ["stomach pain", "acidity", "ulcers on tongue", "vomiting", "cough", "chest pain"],
    # Add more diseases and symptoms as needed
}

def extract_symptoms(input_text):
    doc = nlp(input_text)
    symptoms = [token.text.lower() for token in doc if token.text.lower() in diseases_to_symptoms.values()]
    return symptoms if symptoms else []  # Return an empty list if no symptoms are present


def calculate_similarity(input_text, symptoms):
    if symptoms is None:
        return 0.0  # Return 0 if no symptoms are present

    input_doc = nlp(input_text)
    avg_similarity = sum(input_doc.similarity(nlp(symptom)) for symptom in symptoms) / len(symptoms)
    return avg_similarity



def predict_disease(input_text, excluded_symptoms=[]):
    threshold = 0.75  # Adjust the threshold as needed
    max_similarity = 0.0
    possible_diseases = []

    for disease, symptoms in diseases_to_symptoms.items():
        if set(excluded_symptoms).intersection(symptoms):
            continue  # Skip diseases that have excluded symptoms

        similarity = calculate_similarity(input_text, symptoms)
        if similarity >= threshold and similarity > max_similarity:
            max_similarity = similarity
            possible_diseases = [disease]

    return possible_diseases, max_similarity

def get_symptoms_choices(possible_diseases):
    # Get a list of symptoms associated with possible diseases
    all_possible_symptoms = set()
    for disease in possible_diseases:
        all_possible_symptoms.update(diseases_to_symptoms[disease])
    return list(all_possible_symptoms)

def chatbot():
    print("Hello! I'm your healthcare chatbot. Let's figure out what might be causing your symptoms.")
    print("You can type 'quit' at any time to exit the chat.")

    threshold = 0.75  # Define threshold here
    user_symptoms = []

    while True:
        user_input = input("Enter your symptoms: ").lower()

        if user_input in ['quit', 'q', 'exit']:
            print("Goodbye! If you have more questions, feel free to come back.")
            break

        extracted_symptoms = extract_symptoms(user_input)
        user_symptoms.extend(extracted_symptoms)

        # Provide choices for additional symptoms based on previous inputs
        possible_diseases, similarity = predict_disease(" ".join(user_symptoms))
        symptom_choices = get_symptoms_choices(possible_diseases)

        if similarity >= threshold:
            print(f"Based on your symptoms, it seems you might have {possible_diseases[0]}.")
            print("If you have more symptoms to share, feel free to tell me.")
        elif symptom_choices:
            print("I'm not quite sure. Can you provide more details or additional symptoms?")
            print("Possible symptoms based on your input:", ", ".join(symptom_choices))
            print("If you're done, you can type 'quit' to exit the chat.")

if __name__ == "__main__":
    chatbot()
