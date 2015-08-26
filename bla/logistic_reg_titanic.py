'''
Sample python code to run a simple classification using logistic regression
Data used is from the Titanic contest in Kaggle
by  EuniceHS on 25 Aug 2015
'''
#Start by importing pandas and other machie learnign toolkits from python library
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from pylab import scatter, show, legend, xlabel, ylabel
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
import scipy.optimize as optim

#read input file for training
data=pd.read_csv('C:/EuniceSelfTests/Titanic_train.csv')
data_header= data.head()
data_descript = data.describe()

#Generate test data set from training pool using croos validation
variables = data[['Pclass', 'SibSp', 'Parch', 'Fare']]
output = data[['Survived']]
variables_train, variables_test, output_train, output_test = train_test_split(variables, output, test_size=0.5, random_state=1)

#can also create a plot to visualize how survival/death related to class and SibSP variables
survived = data[data.Survived== 1]
died = data[data.Survived==0]
plt.figure()
plt.scatter(survived.Pclass, survived.SibSp, alpha=0.5, marker ='o', c='b')
plt.scatter(died.Pclass, died.SibSp, alpha = 0.5, marker ='x', c='r')
#xlabel('Survived Crash')
#ylabel('Died during Crash')
plt.legend(('Titanic Survival', 'Titanic death'), loc='upper right')
show()

# convert to 2D tabular format (dataframes) to keep it clean
testSet = pd.DataFrame(data = variables_test, columns =['Pclass', 'SibSp', 'Parch', 'Fare'])
testSet['Target'] = output_test

trainingSet = pd.DataFrame(data = variables_train, columns =['Pclass', 'SibSp', 'Parch', 'Fare'])
trainingSet['Target'] = output_train

#logistic regression - train

lreg = LogisticRegression()
lreg.fit(trainingSet[['Pclass']], output_train)
B1=lreg.coef_[0][0]
B0=lreg.intercept_[0]
lreg_exp=np.exp(B1)

#prediction - test
testSet['predicted_survived']= lreg.predict(testSet[['Pclass']])
accuracy=100*sum(testSet.predicted_survived==testSet.Target)/float(len(testSet.Target))

print accuracy


