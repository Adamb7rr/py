import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

data_train = pd.read_csv(r'F:\py\Titanic\train.csv')
data_test = pd.read_csv(r'F:\py\Titanic\test.csv')

def clean(d):
    d.drop(['Name', 'Cabin', 'Ticket', 'Fare', 'Embarked'], axis=1, inplace=True)
    d['Age'] = d['Age'].fillna(d['Age'].median())
    d.dropna()
    return d

clean(data_train)
clean(data_test)

# sns.heatmap(data_test.isnull())


data_train['Sex'].value_counts().plot.pie(autopct='%1.1f%%')
plt.show()