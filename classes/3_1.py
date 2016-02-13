#
# Weak 3
#
import pandas
from sklearn.svm import SVC


# Load data
data = pandas.read_csv("../svm-data.csv",  header=None)
X = data.drop(data.columns[0], axis=1)
y = data[0]

# Build model
classifier = SVC(C=100000, random_state=241, kernel='linear')
classifier.fit(X, y)
print classifier.support_


