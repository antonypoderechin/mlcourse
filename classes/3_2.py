#
# Weak 3
#
import numpy as np
from sklearn import datasets
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import KFold
from sklearn.svm import SVC


# Load data
newsgroups = datasets.fetch_20newsgroups(subset='all', categories=['alt.atheism', 'sci.space'])
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(newsgroups.data)
y = newsgroups.target

# Build model
grid = {'C': np.power(10.0, np.arange(-5, 6))}
cv = KFold(y.size, n_folds=5, shuffle=True, random_state=241)
clf = SVC(kernel='linear', random_state=241)
gs = GridSearchCV(clf, grid, scoring='accuracy', cv=cv)
gs.fit(X, y)

# Find optimal C
min_score = gs.grid_scores_[0].mean_validation_score
min_c = gs.grid_scores_[0].parameters['C']
for a in gs.grid_scores_:
    if a.mean_validation_score > min_score:
        min_score = a.mean_validation_score
        min_c = a.parameters['C']
    elif a.mean_validation_score == min_score:
        min_c = min(min_c, a.parameters['C'])

clf = SVC(C=min_c, kernel='linear', random_state=241)
clf.fit(X, y)

# Find most popular
print clf.coef_.todense()

