import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
import warnings
from sklearn.exceptions import DataConversionWarning
warnings.filterwarnings(action='ignore', category=UserWarning)


# Load the dataset
data = pd.read_csv('Cars.csv')

# One-hot encoding for the 'Color', 'Type', and 'Origin' columns
data = pd.get_dummies(data, columns=['Color', 'Type', 'Origin'], drop_first=True)

# Convert the 'Stolen?' column to binary (1 for Yes, 0 for No)
data['Stolen?'] = data['Stolen?'].map({'Yes': 1, 'No': 0})

# Split the dataset into features (X) and the target variable (y)
X = data.drop('Stolen?', axis=1)
y = data['Stolen?']

# Initialize the Gaussian Naive Bayes classifier
clf = GaussianNB()

# Train the classifier using the entire dataset 
clf.fit(X, y)

# Prepare the data for the red domestic SUV
# Color_Yellow (0), Type_SUV (1), Type_Sports (0), Origin_Imported (0)
new_data = np.array([[0, 1, 0, 0]])

# Make a prediction
prediction = clf.predict(new_data)

if prediction[0] == 1:
    print("The red domestic SUV is predicted to be stolen.")
else:
    print("The red domestic SUV is predicted not to be stolen.")
