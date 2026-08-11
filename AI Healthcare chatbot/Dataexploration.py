import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Specify the folder to save visualizations
save_folder = 'visualizations'

# Create the folder if it doesn't exist
os.makedirs(save_folder, exist_ok=True)

# Load your CSV data into a DataFrame
df = pd.read_csv('DatasetWithSymptomsCleaned.csv')

# Display basic information about the DataFrame
print(df.info())

# Display summary statistics for numeric columns
print(df.describe())

# Check for missing values in each column
print(df.isnull().sum())

# Handle missing values (e.g., drop rows with missing data)
df = df.dropna()

# Specify the columns you want to explore and visualize
columns_to_visualize = [
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
]

# Calculate the number of subplots needed
num_columns = len(columns_to_visualize)
num_rows = (num_columns + 5) // 6  # 6 subplots per row

# Create subplots
fig, axes = plt.subplots(num_rows, 6, figsize=(18, num_rows * 3))

# Plot histograms for the selected columns and save them as separate files
for i, column in enumerate(columns_to_visualize):
    row_index = i // 6
    col_index = i % 6
    ax = axes[row_index, col_index]
    df[column].plot(kind='hist', bins=20, edgecolor='k', ax=ax)
    ax.set_title(f'Histogram of {column}')
    ax.set_xlabel(column)
    ax.set_ylabel('Frequency')
    
   # Save the histogram in the specified folder
    save_path = os.path.join(save_folder, f'histogram_{column}.png')
    plt.savefig(save_path, bbox_inches='tight')

# Close the figure to prevent displaying it in the notebook
plt.close(fig)

# Plot a countplot for the 'Diseases' column
plt.figure(figsize=(12, 6))
sns.countplot(x='Diseases', data=df, order=df['Diseases'].value_counts().index)
plt.xlabel('Disease')
plt.ylabel('Count')
plt.title('Count of Diseases')
plt.xticks(rotation=90)

# Save the countplot in the specified folder
countplot_save_path = os.path.join(save_folder, 'countplot_diseases.png')
plt.savefig(countplot_save_path, bbox_inches='tight')

# Calculate and display the correlation matrix for numeric columns only
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
numeric_corr_matrix = df[numeric_columns].corr()
plt.figure(figsize=(12, 10))
sns.heatmap(numeric_corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix (Numeric Columns)')

# Save the correlation matrix heatmap in the specified folder
corr_matrix_save_path = os.path.join(save_folder, 'correlation_matrix.png')
plt.savefig(corr_matrix_save_path, bbox_inches='tight')

# Show the plots
plt.show()