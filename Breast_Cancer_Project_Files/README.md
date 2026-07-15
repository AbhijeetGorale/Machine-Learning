🩺 Breast Cancer Classification using Decision Tree
A machine learning project that classifies breast tumors as malignant or benign using the Breast Cancer Wisconsin dataset and a Decision Tree Classifier built with Scikit-learn.
📌 Overview
This project demonstrates an end-to-end classical ML workflow — from raw data to a trained, evaluated model — applied to a real-world medical diagnosis problem. Early and accurate detection of breast cancer is critical, and this project shows how a simple, interpretable model can achieve strong predictive performance.
📊 Dataset
Source: Breast Cancer Wisconsin (Diagnostic) Dataset
Shape: 569 samples × 31 columns (30 features + 1 target)
Features: Computed from digitized images of a breast mass, describing characteristics of cell nuclei — e.g. mean radius, mean texture, mean perimeter, worst symmetry, worst fractal dimension
Target: 0 = malignant, 1 = benign
⚙️ Workflow
Load the dataset — read the CSV into a Pandas DataFrame
Separate features and labels — split into X (features) and Y (target)
Train/test split — 80/20 split with random_state=42 for reproducibility
Model training — DecisionTreeClassifier from Scikit-learn
Evaluation — accuracy score and confusion matrix
🛠️ Tech Stack
Python
Pandas
Scikit-learn (train_test_split, DecisionTreeClassifier, accuracy_score, confusion_matrix, classification_report)
📈 Results
Metric
Score
Accuracy
94.74%
Confusion Matrix

Predicted Malignant
Predicted Benign
Actual Malignant
40
3
Actual Benign
3
68
The model correctly classified 108 out of 114 test samples, with a balanced number of false positives and false negatives.
🚀 How to Run
Bash
📂 Project Structure
Code
🔮 Future Improvements
Compare Decision Tree against Logistic Regression, Random Forest, and SVM
Add hyperparameter tuning (GridSearchCV) to reduce overfitting
Add feature importance visualization
Add cross-validation for more robust performance estimates
👤 Author
Abhijeet Gorale
GitHub: AbhijeetGorale
