# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 17:21:45 2015

@author: Taiga Kuroiwa
I was doing this while I was practicing at 
certain websites, so there are couple of
unnnecessary codes
"""
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import csv
import itertools

df = pd.read_csv('train.csv', header=0)

df.dtypes

df["Age"].mean()

df["Age"].median()

df[ ["Sex", "Pclass", "Age"]]

df[df['Age'] > 60][['Sex', 'Pclass', 'Age', 'Survived']]

df["Gender"] = df["Sex"].map( {'female': 0, "male": 1} ).astype(int)  # 辞書を渡すだけで変換してくれる

df.head(10)

median_ages = np.zeros((2,3)) 

for gi, pi in itertools.product(range(0, 2), range(3)): 
    gender, pclass = gi, pi + 1
    gender_mask = (df["Gender"] == gender)
    pclass_mask = (df["Pclass"] == pclass)
    mask = gender_mask & pclass_mask
    median_ages[gi, pi] = df[mask]["Age"].dropna().median()
    

df["AgeFill"] = df["Age"]
df[ df["Age"].isnull() ][ ["Gender", "Pclass", "Age", "AgeFill"] ].head(10)
df["AgeIsNull"] = pd.isnull(df.Age).astype(int)

df["FamilySize"] = df["SibSp"] + df["Parch"]
df["Age*Class"]  = df["AgeFill"] * df["Pclass"]


df.dtypes[df.dtypes.map(lambda x: x == "object")]


df2 = df.drop(["Name", "Sex", "Ticket", "Cabin", "Embarked"], axis=1)


df2 = df2.drop(["Age"], axis=1)

df3 = df2.dropna()

df3.dtypes

train_data = df3.values

xs = train_data[:, 2:]
y  = train_data[:, 1]  


forest = RandomForestClassifier(n_estimators = 100)


forest = forest.fit(xs, y)


def preprocessing_read(file_path):
  
    df = pd.read_csv(file_path, header=0)
    df["Gender"] = df["Sex"].map( {'female': 0, "male": 1} ).astype(int)
    df["AgeFill"] = df["Age"]

   
    for gi, pi in itertools.product(range(2), range(3)): 
        gender = gi
        pclass = pi + 1
        gender_mask = (df["Gender"] == gender)
        pclass_mask = (df["Pclass"] == pclass)
        age_mask    = df["Age"].isnull()
        mask = gender_mask & pclass_mask & age_mask
        df.ix[mask, "AgeFill"] = median_ages[gi,pi]

    
    df["AgeIsNull"] = pd.isnull(df.Age).astype(int)
    
    df["FamilySize"] = df["SibSp"] + df["Parch"]
    df["Age*Class"]  = df["AgeFill"] * df["Pclass"]
    df = df.drop(["Age", "Name", "Sex", "Ticket", "Cabin", "Embarked"], axis=1)
    df = df.dropna()
    return df

test_df = preprocessing_read("test.csv")
test_df.dtypes

test_data = test_df.values
xs_test = test_data[:, 1:]
output = forest.predict(xs_test)

print (len(test_data[:,0]), len(output))
print (zip(test_data[:,0].astype(int), output.astype(int)))

with open("testingmodel.csv", "w") as f:
    writer = csv.writer(f)
    row = ["PassengerID", "Survived"]
    for i in row:
        writer.writerow(i)
    for pid, survived in zip(test_data[:,0].astype(int), output.astype(int)):
        writer.writerow([pid, survived])
        
mask = (df.Pclass == 3) & (df.Embarked == "S")
df.ix[mask, ["Pclass", "Embarked", "Fare"]]

df.ix[mask, "Fare"].describe()

def preprocessing_read2(file_path):
    df = pd.read_csv(file_path, header=0)
    df["Gender"] = df["Sex"].map( {'female': 0, "male": 1} ).astype(int)
    df["AgeFill"] = df["Age"]

    for gi, pi in itertools.product(range(2), range(3)):
        gender = gi
        pclass = pi + 1
        gender_mask = (df["Gender"] == gender)
        pclass_mask = (df["Pclass"] == pclass)
        age_mask    = df["Age"].isnull()
        mask = gender_mask & pclass_mask & age_mask
        df.ix[mask, "AgeFill"] = median_ages[gi,pi]

    df["AgeIsNull"] = pd.isnull(df.Age).astype(int)    
    df["FamilySize"] = df["SibSp"] + df["Parch"]
    df["Age*Class"]  = df["AgeFill"] * df["Pclass"]
    df = df.drop(["Age", "Name", "Sex", "Ticket", "Cabin", "Embarked"], axis=1)
    
    
    df.ix[df["Fare"].isnull(), "Fare"] = 8.05
    df = df.dropna()
    return df

test_df = preprocessing_read2("test.csv")
test_df.dtypes


test_data = test_df.values
xs_test = test_data[:, 1:]
output = forest.predict(xs_test)

# file entering
with open("taiga_titanmodel.csv", "w") as f:
    writer = csv.writer(f)    
    row = [["PassengerID"], ["Survived"]]
    for i in row:
        writer.writerow(i)
    for pid, survived in zip(test_data[:,0].astype(int), output.astype(int)):
        writer.writerow([pid, survived])
        
        