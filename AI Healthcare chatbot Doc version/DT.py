import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import os
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Load the dataset
data = pd.read_csv('DataTrainingModel.csv')

# Encode the target variable to numerical labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(data['Diseases'])  # Fit and transform y

# Split the data into features (X) and target (y)
X = data.drop(columns=['Diseases'])
# y = label_encoder.transform(data['Diseases'])  # Remove this line

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4921)

# Create and train the Decision Tree model
model = DecisionTreeClassifier(random_state=4921)
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Generate and display a textual representation of the decision tree
tree_rules = export_text(model, feature_names=X.columns.tolist())
print("Decision Tree Rules:\n", tree_rules)

# Display confusion matrix and classification report
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Display confusion matrix
plt.figure(figsize=(8, 6))
plt.imshow(conf_matrix, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Decision Tree Confusion Matrix')
plt.colorbar()

classes = label_encoder.classes_
tick_marks = np.arange(len(classes))
plt.xticks(tick_marks, classes, rotation=45)
plt.yticks(tick_marks, classes)

plt.xlabel('Predicted Label')
plt.ylabel('True Label')

conf_matrix_image_path = os.path.join('Evaluation Output', 'decision_tree_confusion_matrix.jpg')
plt.savefig(conf_matrix_image_path, dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.close()

# Calculate AUC with 'ovr' strategy for multiclass classification
y_prob = model.predict_proba(X_test)

# Find the index of the positive class
positive_class_label = 'your_positive_class'
positive_class_index = np.where(label_encoder.classes_ == positive_class_label)[0][0]

# Calculate ROC curve with 'ovr' strategy for multiclass classification
fpr, tpr, _ = roc_curve(y_test, y_prob[:, positive_class_index], pos_label=positive_class_index)

# Display AUC
print(f'AUC: {roc_auc_score(y_test, y_prob, multi_class="ovr"):.4f}')

# Save the decision tree rules as an image
plt.figure(figsize=(8, 12))
plt.title('Decision Tree Rules')
plt.text(0, 0.5, tree_rules, fontsize=12, ha='left', va='center')
tree_image_path = os.path.join('Evaluation Output', 'decision_tree_rules.jpg')
plt.savefig(tree_image_path, dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.close()

# Display classification report
plt.figure(figsize=(8, 6))
plt.text(0.1, 0.5, class_report, fontsize=12, ha='left', va='center')
class_report_image_path = os.path.join('Evaluation Output', 'decision_tree_classification_report.jpg')
plt.savefig(class_report_image_path, dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.close()

# Save ROC curve as an image
plt.figure(figsize=(8, 6))
plt.plot([0, 1], [0, 1], linestyle='--', label='Random')
plt.plot(fpr, tpr, marker='.', label='Decision Tree')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()

roc_curve_image_path = os.path.join('Evaluation Output', 'decision_tree_roc_curve.jpg')
plt.savefig(roc_curve_image_path, dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.close()

print(f'Decision Tree Confusion Matrix saved as: {conf_matrix_image_path}')
print(f'Decision Tree Rules saved as: {tree_image_path}')
print(f'Decision Tree Classification Report saved as: {class_report_image_path}')
print(f'Decision Tree AUC Plot saved as: {roc_curve_image_path}')
