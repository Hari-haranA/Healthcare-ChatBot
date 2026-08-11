import pandas as pd
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import os
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
data = pd.read_csv('DataTrainingModel.csv')

# Split the data into features (X) and target (y)
X = data.drop(columns=['Diseases'])
y = data['Diseases']

# Create the Random Forest Classifier
model = RandomForestClassifier(random_state=4921)

# Implement k-fold cross-validation
kf = KFold(n_splits=5, shuffle=True, random_state=4921)

# Initialize lists to store metrics across folds
precision_list, recall_list, f1_list, accuracy_list = [], [], [], []
confusion_matrices = []

# Perform cross-validation and get the classification report for each fold
cv_reports = []
for i, (train_index, test_index) in enumerate(kf.split(X), 1):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]
    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    report = classification_report(y_test, y_pred, output_dict=True)
    cv_reports.append(report)
    
    # Store metrics for summary
    precision_list.append(report['weighted avg']['precision'])
    recall_list.append(report['weighted avg']['recall'])
    f1_list.append(report['weighted avg']['f1-score'])
    accuracy_list.append(accuracy_score(y_test, y_pred))

    # Save confusion matrix as an image
    confusion_image_path = f'Evaluation Output/confusion_matrix_fold_{i}.jpg'
    confusion = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    im = plt.imshow(confusion, cmap='Blues')
    classes = data['Diseases'].unique()
    plt.xticks(np.arange(len(classes)), classes, rotation=90)
    plt.yticks(np.arange(len(classes)), classes)
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title(f'Confusion Matrix - Fold {i}')
    for a in range(len(classes)):
        for b in range(len(classes)):
            text = plt.text(b, a, confusion[a, b], ha='center', va='center', color='black')
    plt.colorbar(im)
    plt.savefig(confusion_image_path, bbox_inches='tight', pad_inches=0, format='jpg', dpi=300)
    confusion_matrices.append(confusion_image_path)

# Calculate the average precision, recall, and F1-score across all folds
avg_precision = np.mean(precision_list)
avg_recall = np.mean(recall_list)
avg_f1 = np.mean(f1_list)
avg_accuracy = np.mean(accuracy_list)

# Generate a summarized report
summary_report = f"Average Precision: {avg_precision:.4f}\nAverage Recall: {avg_recall:.4f}\nAverage F1 Score: {avg_f1:.4f}\nAverage Accuracy: {avg_accuracy:.4f}"

# Print the classification report for each fold
for i, report in enumerate(cv_reports, 1):
    print(f"Fold {i} Classification Report:\n{report}")

# Print the summarized report
print("Summary Report:")
print(summary_report)

# Display confusion matrix images for each fold
for i, image_path in enumerate(confusion_matrices, 1):
    print(f"Confusion Matrix - Fold {i}: {image_path}")

# Plot model accuracy and differentiation across folds
plt.figure(figsize=(10, 6))

# Plot model accuracy
plt.subplot(1, 2, 1)
plt.bar(range(1, 6), accuracy_list, color='blue')
plt.title('Model Accuracy Across Folds')
plt.xlabel('Fold')
plt.ylabel('Accuracy')
plt.ylim(0, 1)

# Plot differentiation across folds
plt.subplot(1, 2, 2)
plt.plot(range(1, 6), precision_list, label='Precision', marker='o')
plt.plot(range(1, 6), recall_list, label='Recall', marker='o')
plt.plot(range(1, 6), f1_list, label='F1 Score', marker='o')
plt.legend()
plt.title('Differentiation Across Folds')
plt.xlabel('Fold')
plt.ylabel('Score')
plt.ylim(0, 1)

# Save the combined image
combined_image_path = 'Evaluation Output/model_evaluation_combined.jpg'
plt.savefig(combined_image_path, bbox_inches='tight', pad_inches=0.1, format='jpg', dpi=300)
plt.show()

print(f'Summary Report and Visualizations saved as: {combined_image_path}')
