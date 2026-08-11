import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os

# Load the dataset
data = pd.read_csv('DataTrainingModel.csv')

# Split the data into features (X) and target (y)
X = data.drop(columns=['Diseases'])
y = data['Diseases']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4921)

# Create and train the Random Forest Classifier
model = RandomForestClassifier(random_state=4921)
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model's performance
f1 = f1_score(y_test, y_pred, average='weighted')
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
confusion = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Create a friendly explanation of the classification report
classification_explanation = """
- Precision: The ability of the model to correctly identify positive cases.
- Recall: The ability of the model to find all positive cases.
- F1 Score: The balance between precision and recall.
- Accuracy Score : The percentage of correct predictions.

In simpler terms, Precision tells you how often the model is correct when it predicts the positive class.
Recall tells you how often the model can find all positive cases.

F1 Score combines both Precision and Recall to give a single measure of the model's performance.
"""

print(f'F1 Score: {f1}')
print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
# print(f'Confusion Matrix:\n{confusion}')
print(f'Classification Report:\n{report}')

# Create a folder to save the output
output_folder = 'Evaluation Output'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Create a figure to save the confusion matrix as an image with color variations
fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow(confusion, cmap='YlGnBu')
# Customize the confusion matrix plot
fig, ax = plt.subplots(figsize=(10, 8))
im = ax.imshow(confusion, cmap='Blues')

# Customize the confusion matrix plot
classes = data['Diseases'].unique()
ax.set_xticks(np.arange(len(classes)))
ax.set_yticks(np.arange(len(classes)))
ax.set_xticklabels(classes, rotation=90)
ax.set_yticklabels(classes)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')

# Display the values inside the cells
for i in range(len(classes)):
    for j in range(len(classes)):
        text = ax.text(j, i, confusion[i, j], ha='center', va='center', color='black')

# Save the confusion matrix as an image in the 'evaluation_output' folder
confusion_image_path = os.path.join(output_folder, 'confusion_matrix.jpg')
plt.colorbar(im)
plt.savefig('Evaluation Output/RF Confusion Matrix.jpg', bbox_inches='tight', pad_inches=0, format='jpg', dpi=300)

# Print the location where the image is saved
print(f'Confusion Matrix saved as: {confusion_image_path}')
# # Calculate the correlation matrix for the features
# correlation_matrix = X.corr()

# # Customize the correlation matrix plot
# plt.figure(figsize=(12, 10))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, square=True)
# plt.title('Feature Correlation Matrix')

# # Save the correlation matrix as an image in the 'evaluation_output' folder
# correlation_image_path = os.path.join(output_folder, 'correlation_matrix.jpg')
# plt.savefig('Evaluation Output/Correlation Matrix.jpg', bbox_inches='tight', pad_inches=0, format='jpg', dpi=300)

# # Print the location where the image is saved
# print(f'Correlation Matrix saved as: {correlation_image_path}')
# Create a formatted classification report in table format
formatted_report = f"Classification Report:\n {report}"
metrics_text = f"Random Forest Classifier Report\n\nF1 Score: {f1}\nAccuracy: {accuracy}\nPrecision: {precision}\nRecall: {recall}\n{classification_explanation}\n {formatted_report}"
# Create an image with HTML-formatted text
plt.figure(figsize=(8, 6))
plt.text(0.3, 0.3, metrics_text, fontsize=12, ha='left', va='top', color='black', family='monospace')
plt.axis('off')

# Save the image
plt.savefig('Evaluation Output/RF Report.jpg', dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.show()

