import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sqlalchemy import create_engine
from sklearn.preprocessing import LabelEncoder


# create an engine
engine = create_engine('sqlite:///my_databse.db')

# Load the data
data = pd.read_sql_table("df", engine)

print(data)

# transform string from dataset to floats
le = LabelEncoder()
data['Job Type'] = le.fit_transform(data['Job Type'])
data['Marital Status'] = le.fit_transform(data['Marital Status'])

# Split the data into features and target variable
X = data.drop(columns=['Default'], axis=1)
y = data['Default']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Define the model
model = RandomForestClassifier()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)
print(predictions)

# Evaluate the model
print("Model Accuracy: ", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))
