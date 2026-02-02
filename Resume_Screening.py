import os
import mysql.connector  
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score,mean_absolute_error, accuracy_score, auc, classification_report, confusion_matrix, roc_curve, RocCurveDisplay

df = pd.read_csv('AI_Resume_Screening.csv')
print(df.head())
print(df.tail())

print(df.info())
print(df.shape)

#print(df.isnull().sum())
#Data cleaning
df['Certifications'] = df['Certifications'].fillna('No Certifications')

print(df.isnull().sum())
print(df.nunique())
print(df.columns.to_list())

'''df['Recruiter Decision'] = df['Recruiter Decision'].replace({'Reject': 0, 'Hire': 1})
df['Recruiter Decision'].value_counts()
'''

df['Recruiter_Decision_Encoded'] = df['Recruiter Decision'].replace({'Reject': 0, 'Hire': 1})
# Save back to CSV
df.to_csv("AI_Resume_Screening.csv", index=False)
print(df['Recruiter_Decision_Encoded'].value_counts())


print(df.columns)


#EDA Analysis

#Univariate Analysis
#Numerical
'''sns.histplot(data=df,x='AI Score (0-100)',palette='Set2')
plt.title("Distribution of AI Scores")
plt.show()'''

'''sns.histplot(data=df,x='Experience (Years)',palette='Set1')
plt.title("Distribution of Experience")
plt.show()'''

'''sns.histplot(data=df,x='Projects Count',palette='colorblind')
plt.title("Distribution of Projects Count")
plt.show()'''

#Categorical
'''sns.countplot(data=df,x='Recruiter_Decision_Encoded',palette='muted')
plt.title("Distribution of Recruiter Decisions")
plt.show()'''

'''sns.histplot(data=df,x='Education',palette='pastel')
plt.title('EDUCATION LEVEL DISTRIBUTION')
plt.show()'''

'''sns.countplot(data=df,x='Job Role',palette='pastel')
plt.title('JOB ROLE DISTRIBUTION')
plt.show()'''

#bivariate Analysis

'''plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="AI Score (0-100)", y="Recruiter_Decision_Encoded",  palette="Set2")

plt.title("AI Score vs. Recruiter Decision")
plt.xlabel("AI Score (0-100)")
plt.ylabel("Recruiter Decision (0: Reject, 1: Hire)")
#plt.tight_layout()
plt.show()'''


'''plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Experience (Years)", y="Projects Count",  palette="Set2")

plt.title("Experience (Years) vs. Projects Count")
plt.xlabel("Experience (Years)")
plt.ylabel("Projects Count")
#plt.tight_layout()
plt.show()'''

'''plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Experience (Years)", y="AI Score (0-100)",  palette="Set2")

plt.title("Experience (Years) vs. AI Score (0-100)")
plt.xlabel("Experience (Years)")
plt.ylabel("AI Score (0-100)")
#plt.tight_layout()
plt.show()'''



'''Heatmap
Correlation between Experience, AI Score, Projects, Salary'''

corelation = df[["Experience (Years)","AI Score (0-100)","Projects Count","Salary Expectation ($)","Recruiter_Decision_Encoded"]].corr()
plt.figure(figsize=(6, 4))
sns.heatmap(corelation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()


#Linear Regression Model
''''X = df[['Experience (Years)', 'Projects Count', 'AI Score (0-100)']]
y = df['Recruiter_Decision_Encoded']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
#print(f"Intercept: {model.intercept_}")
#print(f"Coefficients: {model.coef_}")

y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)

print(f"R-squared: {r2:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"MAE: {mae:.2f}")
'''
 

#Logistic Regression Model

'''X = df[['Experience (Years)',
        'Projects Count',
        'AI Score (0-100)',
        'Salary Expectation ($)']]
y = df['Recruiter_Decision_Encoded']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:,1]

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# ROC curve
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

plt.plot(fpr, tpr, label=f"ROC (AUC={roc_auc:.2f})")
plt.plot([0,1], [0,1], 'k--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Example 1")
plt.legend()
plt.show()'''









#MySql Connection and Database Creation

'''db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Anjali@sql'
)
mycursor = db.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS Resume")
db.close()'''



#import mysql.connector

# Connect to MySQL
'''db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anjali@sql",
    database="Resume"
)

if db.is_connected():
    print("✅ Connected to MySQL successfully")

db.close()
'''

'''import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anjali@sql",
    database="Resume"
)

cursor = db.cursor()

cursor.execute("SELECT * FROM Resume_Screening")

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
db.commit()
db.close()
'''

import csv

'''with open("AI_Resume_Screening.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
'''


import csv
import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anjali@sql",
    database="Resume"
)

cursor = db.cursor()

sql =''' 
INSERT INTO Resume_Screening
(Resume_ID, Name, Skills, `Experience (Years)`, Education,
 Certifications, `Job Role`, `Recruiter Decision`,
 `Salary Expectation ($)`, `Projects Count`, `AI Score (0-100)`,
 Recruiter_Decision_Encoded)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

with open("AI_Resume_Screening.csv", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # skip header

    for row in reader:
        cursor.execute(sql, row)

db.commit()
cursor.close()
db.close()

print(" CSV data inserted into MySQL successfully!")


