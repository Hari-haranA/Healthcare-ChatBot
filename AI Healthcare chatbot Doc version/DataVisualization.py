import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data into a DataFrame
df = pd.read_csv('DatasetWithSymptomsCleaned.csv')  # Replace 'your_data.csv' with your actual data file

# Step 1: Understand the Data
# Display basic information about the DataFrame
print(df.info())

# Display summary statistics for numeric columns
print(df.describe())

# Check for missing values in each column
print(df.isnull().sum())

# Handle missing values (e.g., drop rows with missing data)
df = df.dropna()

# Step 2: Visualize Symptoms Distribution (Histograms)

# Specify the columns representing symptoms you want to visualize
symptoms_columns = [
     'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering',
    'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue',
    'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_urination',
    'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings',
    'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level',
    'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration',
    'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite',
    'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea',
    'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload',
    'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision',
    'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose',
    'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate',
    'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
    'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity',
    'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid',
    'brittle_nails', 'swollen_extremities', 'excessive_hunger', 'extra_marital_contacts',
    'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain',
    'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness',
    'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side',
    'loss_of_smell', 'bladder_discomfort', 'foul_smell_of_urine', 'continuous_feel_of_urine',
    'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability',
    'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
    'abnormal_menstruation', 'dischromic_patches', 'watering_from_eyes', 'increased_appetite',
    'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration',
    'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections',
    'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption',
    'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking',
    'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting',
    'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose',
    'yellow_crust_ooze', 'dischromic _patches', 'spotting_ urination', 'swollen_extremeties',
    'foul_smell_of urine'
    # Add more symptom columns here
]

# Calculate the number of subplots needed
num_columns = len(symptoms_columns)
num_rows = (num_columns + 2) // 3  # 3 subplots per row

# Create subplots for symptoms histograms
fig, axes = plt.subplots(num_rows, 3, figsize=(15, num_rows * 3))

for i, column in enumerate(symptoms_columns):
    row_index = i // 3
    col_index = i % 3
    ax = axes[row_index, col_index]
    sns.histplot(data=df, x=column, bins=20, ax=ax)
    ax.set_title(f'Histogram of {column}')
    ax.set_xlabel(column)
    ax.set_ylabel('Frequency')

# Remove empty subplots
for i in range(num_columns, num_rows * 3):
    row_index = i // 3
    col_index = i % 3
    fig.delaxes(axes[row_index, col_index])

plt.tight_layout()
plt.show()

# Step 3: Visualize Disease Distribution (Bar Chart)

# Plot a countplot for the 'Diseases' column
plt.figure(figsize=(12, 6))
sns.countplot(x='Diseases', data=df, order=df['Diseases'].value_counts().index)
plt.xlabel('Disease')
plt.ylabel('Count')
plt.title('Count of Diseases')
plt.xticks(rotation=90)
plt.show()
