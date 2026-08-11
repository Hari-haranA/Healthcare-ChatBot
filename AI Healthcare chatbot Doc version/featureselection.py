import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load the dataset (transformed_data.csv)
df = pd.read_csv('transformed_data.csv')

# Encode the target variable (Diseases)
label_encoder = LabelEncoder()
df['Diseases'] = label_encoder.fit_transform(df['Diseases'])

# Split the data into features (X) and target (y)
X = df.drop(columns=['Diseases'])
y = df['Diseases']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize classifiers
rf_classifier = RandomForestClassifier(random_state=42)
svm_classifier = SVC(random_state=42)
gb_classifier = GradientBoostingClassifier(random_state=42)
knn_classifier = KNeighborsClassifier()
nb_classifier = GaussianNB()
dt_classifier = DecisionTreeClassifier(random_state=42)
lr_classifier = LogisticRegression(random_state=42)

classifiers = [rf_classifier, svm_classifier, gb_classifier, knn_classifier, nb_classifier, dt_classifier, lr_classifier]

results = []

for clf in classifiers:
    # Train the classifier
    clf.fit(X_train, y_train)
    
    # Perform cross-validation (adjust cv as needed)
    cv_scores = cross_val_score(clf, X_train, y_train, cv=2, scoring='accuracy')
    
    # Make predictions on the test set
    y_pred = clf.predict(X_test)
    
    # Evaluate performance
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    
    results.append({
        'Classifier': type(clf).__name__,
        'CV_Accuracy': cv_scores.mean(),
        'Test_Accuracy': accuracy,
        'Test_Precision': precision,
        'Test_Recall': recall,
        'Test_F1': f1
    })

# Create a DataFrame to compare results
results_df = pd.DataFrame(results)
print(results_df)
