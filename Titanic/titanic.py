import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier


train = pd.read_csv(r"Titanic/train.csv")
test = pd.read_csv(r"Titanic/test.csv")


test_passenger_id = test["PassengerId"]

# ---- Extract Title from Name ----
train["Title"] = train["Name"].str.extract(" ([A-Za-z]+)\.", expand=False)
test["Title"] = test["Name"].str.extract(" ([A-Za-z]+)\.", expand=False)

common_titles = ["Mr", "Miss", "Mrs", "Master"]

train["Title"] = train["Title"].apply(lambda x: x if x in common_titles else "Other")
test["Title"] = test["Title"].apply(lambda x: x if x in common_titles else "Other")

title_map = {"Mr":0, "Miss":1, "Mrs":2, "Master":3, "Other":4}

train["Title"] = train["Title"].map(title_map)
test["Title"] = test["Title"].map(title_map)

# ---- Family Features ----
train["FamilySize"] = train["SibSp"] + train["Parch"] + 1
test["FamilySize"] = test["SibSp"] + test["Parch"] + 1

train["IsAlone"] = (train["FamilySize"] == 1).astype(int)
test["IsAlone"] = (test["FamilySize"] == 1).astype(int)

# Drop unnecessary columns
drop_cols = ["Name", "Ticket", "Cabin"]
train.drop(drop_cols, axis=1, inplace=True)
test.drop(drop_cols, axis=1, inplace=True)

# Fill missing values
train["Age"].fillna(train["Age"].median(), inplace=True)
test["Age"].fillna(test["Age"].median(), inplace=True)

train["Embarked"].fillna(train["Embarked"].mode()[0], inplace=True)
test["Embarked"].fillna(test["Embarked"].mode()[0], inplace=True)

test["Fare"].fillna(test["Fare"].median(), inplace=True)

# Convert categorical to numeric
train["Sex"] = train["Sex"].map({"male":1, "female":0})
test["Sex"] = test["Sex"].map({"male":1, "female":0})

train["Embarked"] = train["Embarked"].map({"S":0, "C":1, "Q":2})
test["Embarked"] = test["Embarked"].map({"S":0, "C":1, "Q":2})

X = train.drop("Survived", axis=1)
y = train["Survived"]

X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = RandomForestClassifier(
    n_estimators=300,
    max_depth=7,
    min_samples_split=4,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_valid)

accuracy = accuracy_score(y_valid, predictions)
print("Validation Accuracy:", accuracy)


model.fit(X, y)

test_predictions = model.predict(test)

# =========================
# 7️⃣ Create Submission
# =========================

submission = pd.DataFrame({
    "PassengerId": test_passenger_id,
    "Survived": test_predictions
})

submission.to_csv("submission.csv", index=False)

print("Submission file created successfully!")
