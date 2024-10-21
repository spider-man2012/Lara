"""
k-Nearest Neighbors (k-NN) is a simple and effective supervised learning algorithm used for classification and regression tasks. It makes predictions based on the proximity of data points in the feature space.

Key Points:
Instance-Based Learning: k-NN is a lazy learner, meaning it doesn’t build a model until a query is made. It stores the entire training dataset.

Distance Measurement: To find the nearest neighbors, k-NN calculates the distance (commonly using Euclidean distance) between the query point and all other points in the dataset.

Choosing k: The parameter 
k determines how many neighbors to consider. A smaller 
k can be sensitive to noise, while a larger 
k smooths out the decision boundary.
Voting Mechanism: For classification, k-NN assigns the class that is most common among the 

k nearest neighbors. For regression, it averages the values of the neighbors.

Applications: k-NN is widely used in recommendation systems, image recognition, and pattern recognition due to its simplicity and effectiveness.
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create KNN classifier with k=5 (you can adjust k)
knn_classifier = KNeighborsClassifier(n_neighbors=5)

# Train the classifier
knn_classifier.fit(X_train, y_train)

# Make predictions on the test data
y_pred = knn_classifier.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")