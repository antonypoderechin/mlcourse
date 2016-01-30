from __future__ import division
import pandas


# Read data
data = pandas.read_csv('../titanic.csv', index_col='PassengerId')

# Count man and woman
sex_data = data['Sex'].value_counts()
print 'Male and female:', sex_data['male'], sex_data['female']

# Total count
total = len(data)

# Survived percent
survived_data = data['Survived'].value_counts()
print 'Survived:', survived_data[1] / (survived_data[0] + survived_data[1])

# First class
first_class_count = data['Pclass'].value_counts()[1]
print 'First class:', first_class_count / total

# Mean and median age
age_series = data['Age'].dropna()
mean = age_series.mean()
median = age_series.median()
print 'Mean and median age:', mean, median

# Correlation
sib = data['SibSp']
parch = data['Parch']
print 'Correlation', parch.corr(sib)

# Most common female name
