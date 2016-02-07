#
# Week 2
#
from __future__ import division
import pandas
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler


# Read data
train_set = pandas.read_csv('../perceptron_train.csv',  header=None)
test_set = pandas.read_csv('../perceptron_test.csv', header=None)

# Prepare train data
X = train_set.drop(train_set.columns[0], axis=1)
y = train_set[0]

# Prepare test data
X_test = test_set.drop(test_set.columns[0], axis=1)
y_test = test_set[0]

# Train model
classifier = Perceptron(random_state=241)
classifier.fit(X, y)

# Results
results = classifier.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, results)

# Normalization
scaler = StandardScaler()
X_normal = scaler.fit_transform(X)
X_test_normal = scaler.fit_transform(X_test)

# Train model
classifier = Perceptron(random_state=241)
classifier.fit(X_normal, y)

# Results
results_normal = classifier.predict(X_test_normal)

# Accuracy
accuracy_normal = accuracy_score(y_test, results_normal)

print accuracy_normal - accuracy

