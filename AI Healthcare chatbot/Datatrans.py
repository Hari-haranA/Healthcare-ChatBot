# Step 1: Import necessary libraries
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Step 2: Load your dataset into a DataFrame
df = pd.read_csv('DatasetWithSymptomsCleaned.csv')

# Step 3: Select the target variable (Diseases) and separate it from the features
target = df['Diseases']
features = df.drop(columns=['Diseases'])

# Step 4: Identify and select categorical columns for one-hot encoding
categorical_cols = features.select_dtypes(include=['object']).columns

# Step 5: Perform one-hot encoding for categorical columns
features_encoded = pd.get_dummies(features, columns=categorical_cols)

# Step 6: Initialize the Min-Max scaler
scaler = MinMaxScaler()

# Step 7: Fit and transform the numerical columns using Min-Max scaling
numerical_cols = features_encoded.select_dtypes(include=['float64', 'int64']).columns
features_encoded[numerical_cols] = scaler.fit_transform(features_encoded[numerical_cols])

# Step 8: Combine the target variable (Diseases) and the transformed features
df_transformed = pd.concat([target, features_encoded], axis=1)

# Step 9: Save the transformed DataFrame to a new CSV file
df_transformed.to_csv('transformed_data.csv', index=False)

# The 'df_transformed' DataFrame now contains one-hot encoded categorical columns
# and normalized numerical columns, including the target variable 'Diseases'.
