"""
A Decision Tree is a visual model used for classification and regression that resembles a tree structure. It starts with a root node and splits 
into branches based on features, leading to decision nodes and finally to leaf nodes that represent outcomes.

Key Points:
Splitting: Nodes are split based on features that provide the most information gain (using measures like Gini impurity or entropy).
Recursive Process: The tree grows until nodes are pure or a stopping criterion is met.
Pruning: Simplifies the tree to prevent overfitting.
Interpretability: Easy to understand and visualize, making it accessible.
Applications: Used in finance, healthcare, and marketing for decision-making.
 
 """

# Import necessary libraries
import numpy as np
import pandas as pd  # Import Pandas for data loading
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load your dataset from a local file (e.g., CSV)
# Replace 'Iris.csv' with the actual path to your dataset file
data = pd.read_csv('Iris.csv')

# Check the columns and first few rows
print("Columns in the dataset:", data.columns)
print("First few rows of the dataset:")
print(data.head())

# Assuming the target variable is in a column named 'species'
# Adjust 'species' to the actual target variable name based on your dataset
target_variable = 'species'  # Change this based on your dataset

# Split features and target variable
X = data.drop(target_variable, axis=1)
y = data[target_variable]

# Split the dataset into a training set and a testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Decision Tree classifier
clf = DecisionTreeClassifier()

# Fit the classifier to the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Visualize and interpret the generated decision tree
plt.figure(figsize=(12, 8))
plot_tree(clf, filled=True, feature_names=X.columns, class_names=y.unique().astype(str))
plt.title("Decision Tree Visualization")
plt.show()
