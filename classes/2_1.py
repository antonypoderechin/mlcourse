#
# First homework of Week 2
#

from __future__ import division
import pandas
import sklearn
from sklearn import cross_validation
from sklearn.cross_validation import KFold
from sklearn.neighbors import KNeighborsClassifier


# Read data
data = pandas.read_csv('../wine.csv', header=None)
X = data.drop(data.columns[0], axis=1)
y = data[0]

# Cross validation generator
k_folds = KFold(len(X), n_folds=5, shuffle=True, random_state=42)


def score(k):
    classifier = KNeighborsClassifier(n_neighbors=k)
    return [k, cross_validation.cross_val_score(classifier, X, y, cv=k_folds, scoring="accuracy").mean()]


def max_scr(a, b):
    if a[1] >= b[1]:
        return a
    else:
        return b


# Find optimal
scores = map(score, range(1, 50))
max_score = reduce(max_scr, scores)
print "Best score:", max_score

# Normalize
X = sklearn.preprocessing.scale(X)
scores = map(score, range(1, 50))
max_score = reduce(max_scr, scores)
print "Best normalized score:", max_score
