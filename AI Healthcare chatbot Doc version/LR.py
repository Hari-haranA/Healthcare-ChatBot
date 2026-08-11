import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder

# Load the dataset
data = pd.read_csv('DataTrainingModel.csv')

# Encode the target variable to numerical labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(data['Diseases'])

# Split the data into features (X) and target (y)
X = data.drop(columns=['Diseases'])
y = label_encoder.transform(data['Diseases'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4921)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate coefficients and intercept
coefficients = model.coef_
intercept = model.intercept_

# Calculate residuals
residuals = y_test - y_pred

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)

# Calculate Root Mean Squared Error (RMSE)
rmse = np.sqrt(mse)

# Calculate R-squared (R2) score
r2 = r2_score(y_test, y_pred)

# Calculate adjusted R-squared
n = len(y_test)
k = X_test.shape[1]
adj_r2 = 1 - ((1 - r2) * (n - 1) / (n - k - 1))

# Perform cross-validation and get cross-validation scores
cv_scores = cross_val_score(model, X, y, cv=5)

# Create a scatter plot of actual vs. predicted values
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(y_test, y_pred, color='blue')
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.title('Linear Regression Scatter Plot (Actual vs. Predicted)')

# Create a residual plot
plt.subplot(1, 2, 2)
plt.scatter(y_pred, residuals, color='green')
plt.xlabel('Predictions')
plt.ylabel('Residuals')
plt.title('Residual Plot')

# Save the scatter plot and residual plot
scatter_image_path = os.path.join('Evaluation Output', 'scatter_plot.jpg')
residual_plot_path = os.path.join('Evaluation Output', 'residual_plot.jpg')
plt.savefig(scatter_image_path, dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.savefig(residual_plot_path, dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.close()

# Create an image for the Linear Regression report
plt.figure(figsize=(8, 12))
plt.title('Linear Regression Report', pad=20)  # Add padding to the title

# Include file descriptions in the report
report_description = f'''
File Descriptions:
- scatter_plot.jpg: Scatter plot showing the relationship between actual and predicted values.
- residual_plot.jpg: Residual plot showing the distribution of residuals.
- coefficients.csv: CSV file containing the coefficients for each feature in the linear regression model.
- linear_regression_report.jpg: Report containing information about the model, including coefficients, plots, and scores.
'''

# Display metrics on the report
report_metrics = f'''
Metrics:
- Mean Squared Error (MSE): {mse:.4f}
- Root Mean Squared Error (RMSE): {rmse:.4f}
- R-squared (R2): {r2:.4f}
- Adjusted R-squared: {adj_r2:.4f}
- Cross-Validation Scores: {cv_scores}
'''

plt.text(0, 0.5, report_description + '\n' + report_metrics, fontsize=12, ha='left', va='center')

# Save the linear regression report as an image
report_image_path = os.path.join('Evaluation Output', 'linear_regression_report.jpg')
plt.savefig(report_image_path, dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.close()

print(f'Scatter Plot saved as: {scatter_image_path}')
print(f'Residual Plot saved as: {residual_plot_path}')
print(f'Linear Regression Report saved as: {report_image_path}')
