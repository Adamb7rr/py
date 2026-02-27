import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

data_train = pd.read_csv(r'F:\py\Titanic\train.csv')
data_test = pd.read_csv(r'F:\py\Titanic\test.csv')

def clean(d):
    d.drop(['Name', 'Cabin', 'Ticket', 'Fare', 'Embarked'], axis=1, inplace=True)
    d['Age'] = d['Age'].fillna(d['Age'].median())
    d.dropna(inplace=True)
    return d

clean(data_train)
clean(data_test)

data_train.Sex=pd.get_dummies(data_train.Sex, drop_first=True, dtype='uint8')
data_test.Sex=pd.get_dummies(data_test.Sex, drop_first=True, dtype='uint8')

x = data_train.drop(['Survived'], axis=1)

y = data_train['Survived']

x_data_train, x_data_test, y_data_train, y_data_test = train_test_split(x,y,train_size=.8, random_state=42)

accuracies = []
def all(model):
    model.fit(x_data_train, y_data_train)
    pre = model.predict(x_data_test)
    score = accuracy_score(pre,y_data_test)
    accuracies.append(score)
    print(f'Accuracy: {score}')

model1 = LogisticRegression()
all(model1)
model2 = RandomForestClassifier()
all(model2)
model3 = GradientBoostingClassifier()
all(model3)
model4 = DecisionTreeClassifier()
all(model4)
model5 = KNeighborsClassifier()
all(model5)
model6 = GaussianNB()
all(model6)
model7 = SVC()
all(model7)

Algorithms = ['LogisticRegression', 'RandomForestClassifier', 'GradientBoostingClassifier',
            'DecisionTreeClassifier', 'KNeighborsClassifier', 'GaussianNB', 'SVC']

new = pd.DataFrame({'Algorithms': Algorithms, 'accuracies': accuracies})

modelx = RandomForestClassifier()
modelx.fit(x_data_train, y_data_train)

lpre = modelx.predict(data_test)
final = data_test['PassengerId']

new_dataframe = pd.DataFrame({
                            'PassengerId': final,
                            'Survived': lpre
                        })
new_dataframe.to_csv("submission.csv", index=False)
