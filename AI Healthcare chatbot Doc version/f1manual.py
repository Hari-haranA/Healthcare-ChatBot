import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, accuracy_score

# Load the dataset
data = pd.read_csv('DataTrainingModel.csv')

# Split the data into features (X) and target (y)
X = data.drop(columns=['Diseases'])
y = data['Diseases']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.9, random_state=4921)

# Create and train the Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate True Positives (TP)
TP = sum((y_test == 1) & (y_pred == 1))

# Calculate True Negatives (TN)
TN = sum((y_test == 0) & (y_pred == 0))

# Calculate False Positives (FP)
FP = sum((y_test == 0) & (y_pred == 1))

# Calculate False Negatives (FN)
FN = sum((y_test == 1) & (y_pred == 0))

# Calculate Precision (if TP and FP are not both zero)
if TP + FP > 0:
    precision = TP / (TP + FP)
else:
    precision = 0.0

# Calculate Recall (Sensitivity) (if TP and FN are not both zero)
if TP + FN > 0:
    recall = TP / (TP + FN)
else:
    recall = 0.0

# Calculate F1 Score
if precision + recall > 0:
    f1 = 2 * (precision * recall) / (precision + recall)
else:
    f1 = 0.0

# Calculate Accuracy
accuracy = (TP + TN) / len(y_test)

print(f'True Positives (TP): {TP}')
print(f'True Negatives (TN): {TN}')
print(f'False Positives (FP): {FP}')
print(f'False Negatives (FN): {FN}')
print(f'Precision: {precision}')
print(f'Recall (Sensitivity): {recall}')
print(f'F1 Score: {f1}')
print(f'Accuracy: {accuracy}')
