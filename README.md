#💳 Credit Card Fraud Detection

A machine learning project to detect fraudulent credit card transactions using Python, scikit-learn, and Streamlit. The project handles data preprocessing, class imbalance (undersampling & SMOTE), model training, evaluation, and deployment as a web app.

Key Points:

- Preprocessing: Scaling Amount, dropping Time, removing duplicates.

- Imbalanced Data Handling: Undersampling and SMOTE oversampling.

- Models: Logistic Regression and Decision Tree Classifier.

- Evaluation: Accuracy, Precision, Recall, F1-score.

- Deployment: Streamlit app that predicts fraud for input values (V1–V28 + Amount).

Final Model: Decision Tree trained on SMOTE-oversampled data.

Technologies: Python, pandas, numpy, scikit-learn, imbalanced-learn, Streamlit, Joblib.
