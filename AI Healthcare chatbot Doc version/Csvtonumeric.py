import pandas as pd

# Read the existing CSV file into a DataFrame
df = pd.read_csv("DiseasesSymptoms.csv")

# Set symptoms to 1 for specific diseases
df.loc[df['Diseases'] == 'Fungal infection', ['itching', 'skin_rash', 'nodal_skin_eruptions', 'dischromic _patches']] = 1
df.loc[df['Diseases'] == 'Allergy', ['continuous_sneezing', 'shivering', 'chills', 'watering_from_eyes']] = 1
df.loc[df['Diseases'] == 'GERD', ['stomach_pain', 'acidity', 'ulcers_on_tongue', 'vomiting', 'cough', 'chest_pain']] = 1
df.loc[df['Diseases'] == 'Chronic cholestasis', ['itching', 'vomiting', 'yellowish_skin', 'nausea', 'loss_of_appetite', 'abdominal_pain', 'yellowing_of_eyes']] = 1
df.loc[df['Diseases'] == 'Drug Reaction', ['itching', 'skin_rash', 'stomach_pain', 'burning_micturition', 'spotting_ urination']] = 1
df.loc[df['Diseases'] == 'Peptic ulcer disease', ['vomiting', 'indigestion', 'loss_of_appetite', 'abdominal_pain', 'passage_of_gases', 'internal_itching']] = 1
df.loc[df['Diseases'] == 'AIDS', ['muscle_wasting', 'patches_in_throat', 'high_fever', 'extra_marital_contacts']] = 1
df.loc[df['Diseases'] == 'Diabetes', ['weight_loss', 'restlessness', 'lethargy', 'irregular_sugar_level', 'blurred_and_distorted_vision', 'obesity', 'excessive_hunger', 'increased_appetite', 'polyuria']] = 1
df.loc[df['Diseases'] == 'Gastroenteritis', ['vomiting', 'sunken_eyes', 'dehydration', 'diarrhoea']] = 1
df.loc[df['Diseases'] == 'Bronchial Asthma', ['fatigue', 'cough', 'high_fever', 'breathlessness', 'family_history', 'mucoid_sputum']] = 1
df.loc[df['Diseases'] == 'Hypertension', ['headache', 'chest_pain', 'dizziness', 'loss_of_balance', 'lack_of_concentration']] = 1
df.loc[df['Diseases'] == 'Migraine', ['acidity', 'indigestion', 'headache', 'blurred_and_distorted_vision', 'excessive_hunger', 'stiff_neck', 'depression', 'irritability', 'visual_disturbances']] = 1
df.loc[df['Diseases'] == 'Cervical spondylosis', ['back_pain', 'weakness_in_limbs', 'neck_pain', 'dizziness', 'loss_of_balance']] = 1
df.loc[df['Diseases'] == 'Paralysis (brain hemorrhage)', ['vomiting', 'headache', 'weakness_of_one_body_side', 'altered_sensorium']] = 1
df.loc[df['Diseases'] == 'Jaundice', ['itching', 'vomiting', 'fatigue', 'weight_loss', 'high_fever', 'yellowish_skin', 'dark_urine', 'abdominal_pain']] = 1
df.loc[df['Diseases'] == 'Malaria', ['chills', 'vomiting', 'high_fever', 'sweating', 'headache', 'nausea', 'diarrhoea', 'muscle_pain']] = 1
df.loc[df['Diseases'] == 'Chicken pox', ['itching', 'skin_rash', 'fatigue', 'lethargy', 'high_fever', 'headache', 'loss_of_appetite', 'mild_fever', 'swelled_lymph_nodes', 'malaise', 'red_spots_over_body']] = 1
df.loc[df['Diseases'] == 'Dengue', ['skin_rash', 'chills', 'joint_pain', 'vomiting', 'fatigue', 'high_fever', 'headache', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'malaise', 'muscle_pain', 'red_spots_over_body']] = 1
df.loc[df['Diseases'] == 'Typhoid', ['chills', 'vomiting', 'fatigue', 'high_fever', 'headache', 'nausea', 'constipation', 'abdominal_pain', 'diarrhoea', 'toxic_look_(typhos)', 'belly_pain']] = 1
df.loc[df['Diseases'] == 'Hepatitis A', ['joint_pain', 'vomiting', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellowing_of_eyes', 'muscle_pain']] = 1
df.loc[df['Diseases'] == 'Hepatitis B', ['itching', 'fatigue', 'lethargy', 'yellowish_skin', 'dark_urine', 'loss_of_appetite', 'abdominal_pain', 'yellow_urine', 'yellowing_of_eyes', 'malaise', 'receiving_blood_transfusion', 'receiving_unsterile_injections']] = 1
df.loc[df['Diseases'] == 'Hepatitis C', ['fatigue', 'yellowish_skin', 'nausea', 'loss_of_appetite', 'yellowing_of_eyes', 'family_history']] = 1
df.loc[df['Diseases'] == 'Hepatitis D', ['joint_pain', 'vomiting', 'fatigue', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'abdominal_pain', 'yellowing_of_eyes']] = 1
df.loc[df['Diseases'] == 'Hepatitis E', ['joint_pain', 'vomiting', 'fatigue', 'high_fever', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'abdominal_pain', 'yellowing_of_eyes', 'acute_liver_failure', 'coma', 'stomach_bleeding']] = 1
df.loc[df['Diseases'] == 'Alcoholic hepatitis', ['vomiting', 'yellowish_skin', 'abdominal_pain', 'swelling_of_stomach', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload']] = 1
df.loc[df['Diseases'] == 'Tuberculosis', ['chills', 'vomiting', 'fatigue', 'weight_loss', 'cough', 'high_fever', 'breathlessness', 'sweating', 'loss_of_appetite', 'mild_fever', 'yellowing_of_eyes', 'swelled_lymph_nodes', 'malaise', 'phlegm', 'chest_pain', 'blood_in_sputum']] = 1
df.loc[df['Diseases'] == 'Common Cold', ['continuous_sneezing', 'chills', 'fatigue', 'cough', 'high_fever', 'headache', 'swelled_lymph_nodes', 'malaise', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'loss_of_smell', 'muscle_pain']] = 1
df.loc[df['Diseases'] == 'Pneumonia', ['chills', 'fatigue', 'cough', 'high_fever', 'breathlessness', 'sweating', 'malaise', 'phlegm', 'chest_pain', 'fast_heart_rate', 'rusty_sputum']] = 1
df.loc[df['Diseases'] == 'Dimorphic hemmorhoids(piles)', ['constipation', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus']] = 1
df.loc[df['Diseases'] == 'Heart attack', ['vomiting', 'breathlessness', 'sweating', 'chest_pain']]
df.loc[df['Diseases'] == 'Varicose veins', ['fatigue', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'prominent_veins_on_calf']] = 1
df.loc[df['Diseases'] == 'Hypothyroidism', ['fatigue', 'weight_gain', 'cold_hands_and_feets', 'mood_swings', 'lethargy', 'dizziness', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'depression', 'irritability', 'abnormal_menstruation']] = 1
df.loc[df['Diseases'] == 'Hyperthyroidism', ['fatigue', 'mood_swings', 'weight_loss', 'restlessness', 'sweating', 'diarrhoea', 'fast_heart_rate', 'excessive_hunger', 'muscle_weakness', 'irritability', 'abnormal_menstruation']] = 1
df.loc[df['Diseases'] == 'Hypoglycemia', ['vomiting', 'fatigue', 'anxiety', 'sweating', 'headache', 'nausea', 'blurred_and_distorted_vision', 'excessive_hunger', 'drying_and_tingling_lips', 'slurred_speech', 'irritability', 'palpitations']] = 1
df.loc[df['Diseases'] == 'Osteoarthristis', ['joint_pain', 'neck_pain', 'knee_pain', 'hip_joint_pain', 'swelling_joints', 'painful_walking']] = 1
df.loc[df['Diseases'] == 'Arthritis', ['muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'painful_walking']] = 1
df.loc[df['Diseases'] == '(vertigo) Paroymsal Positional Vertigo', ['vomiting', 'headache', 'nausea', 'spinning_movements', 'loss_of_balance', 'unsteadiness']] = 1
df.loc[df['Diseases'] == 'Acne', ['skin_rash', 'pus_filled_pimples', 'blackheads', 'scurring']] = 1
df.loc[df['Diseases'] == 'Urinary tract infection', ['burning_micturition', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine']] = 1
df.loc[df['Diseases'] == 'Psoriasis', ['skin_rash', 'joint_pain', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails']] = 1
df.loc[df['Diseases'] == 'Impetigo', ['skin_rash', 'high_fever', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']] = 1
# Continue adding symptoms for the rest of the diseases as per your list
# Save the updated DataFrame as a CSV file
df.to_csv("DiseasesWithSymptoms.csv", index=False)
