from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)  

# Create individual weak classifier (Decision Tree)
weak_classifier = DecisionTreeClassifier(max_depth=1)  

# Create AdaBoost classifier
adaboost_classifier = AdaBoostClassifier(estimator=weak_classifier, n_estimators=50, algorithm='SAMME', random_state=42)  

# Train classifiers
weak_classifier.fit(X_train, y_train)
adaboost_classifier.fit(X_train, y_train)  

# Make predictions
y_pred_weak = weak_classifier.predict(X_test)  
y_pred_adaboost = adaboost_classifier.predict(X_test)  

# Evaluate accuracy
accuracy_weak = accuracy_score(y_test, y_pred_weak)
accuracy_adaboost = accuracy_score(y_test, y_pred_adaboost)

print(f"Weak Classifier Accuracy: {accuracy_weak}")
print(f"AdaBoost Classifier Accuracy: {accuracy_adaboost}")