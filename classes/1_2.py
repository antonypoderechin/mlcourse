#
# Second homework of Week 1
#
from __future__ import division
from sklearn.tree import DecisionTreeClassifier
import pandas


# Read data
data = pandas.read_csv('../titanic.csv', index_col='PassengerId')

# Select columns
train_data = data[['Survived', 'Pclass', 'Fare', 'Age', 'Sex']]

# Prepare data
train_data = train_data.dropna()
train_data = train_data.replace('male', 0).replace('female', 1)
target_result = train_data[['Survived']]
train_data = train_data.drop('Survived', 1)

# Build tree
classifier = DecisionTreeClassifier(random_state=241)
classifier.fit(train_data, target_result)

# Parameters weights
importance = classifier.feature_importances_
print importance
