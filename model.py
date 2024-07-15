import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load the dataset
data = pd.read_csv('nutrition_data.csv')

# Features and target
X = data[['calories']]
y_protein = data['protein']
y_fat = data['fat']
y_carbs = data['carbs']

# Split the data into training and testing sets
X_train, X_test, y_train_protein, y_test_protein = train_test_split(X, y_protein, test_size=0.2, random_state=42)
X_train, X_test, y_train_fat, y_test_fat = train_test_split(X, y_fat, test_size=0.2, random_state=42)
X_train, X_test, y_train_carbs, y_test_carbs = train_test_split(X, y_carbs, test_size=0.2, random_state=42)

# Train the models
model_protein = LinearRegression()
model_protein.fit(X_train, y_train_protein)

model_fat = LinearRegression()
model_fat.fit(X_train, y_train_fat)

model_carbs = LinearRegression()
model_carbs.fit(X_train, y_train_carbs)

# Save the models as pickle files
with open('model_protein.pkl', 'wb') as f:
    pickle.dump(model_protein, f)

with open('model_fat.pkl', 'wb') as f:
    pickle.dump(model_fat, f)

with open('model_carbs.pkl', 'wb') as f:
    pickle.dump(model_carbs, f)

print("Models saved as 'model_protein.pkl', 'model_fat.pkl', and 'model_carbs.pkl'")
