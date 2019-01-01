import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def para(s): 
    if s == "PassengerId":
        return 0
    if s == "Survived":
        return 1
    if s == "Pclass":
        return 2
    if s == "Name":
        return 3
    if s == "Sex":
        return 4
    if s == "Age":
        return 5
    if s == "SibSp":
        return 6
    if s == "Parch":
        return 7
    if s == "Ticket":
        return 8
    if s == "Fare":
        return 9
    if s == "Cabin":
        return 10
    if s == "Embarked":
        return 11

data = pd.read_csv("train.csv")
data = data.T

def count(s, o, status = None):
    c = 0
    if status == None:
        for i in range (0, data.shape[1]):
            if(data[i][para(s)] == o):
                c += 1
    else:
        for i in range (0, data.shape[1]):
            if(data[i][para(s)] == o and data[i][para("Survived")]):
                c += 1
    return c
survived = count("Survived", 1)
passanger = data.shape[1]
died = passanger - survived
print("Number of People Survived:", survived)
print("Number of People Died:", died)

labels = 'Died', 'Survived'
sizes = [died, survived]
explode = (0, 0.09)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
plt.savefig('1.png')
male = count("Sex", "male")
female = count("Sex", "female")

male_survived = count("Sex", "male", 1)
female_survived = count("Sex", "female", 1)

labels = 'Male Survived', 'Male Died','Female Survived', 'Female Died'
sizes = [male_survived, male - male_survived, female_survived, female - female_survived]
explode = (0, 0, 0, 0)
# colors = [(0.9, 0, 0), (0, 0.5, 0)]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

labels = 'Female Survived', 'Female Died'
sizes = [female_survived, female - female_survived]
explode = (0, 0.09)
# colors = [(0.9, 0, 0), (0, 0.5, 0)]
fig2, ax2 = plt.subplots()
ax2.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
plt.savefig('2.png')

labels = 'Male Survived', 'Male Died'
sizes = [male_survived, male - male_survived]
explode = (0, 0.09)
# colors = [(0.9, 0, 0), (0, 0.5, 0)]
fig3, ax3 = plt.subplots()
ax3.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

print("Number of Male:", male)
print("Number of Male Survived:", male_survived)
print("Number of Female:", female)
print("Number of Female Survived", female_survived)

plt.show()
plt.savefig('3.png')

child = 0
adult = 0
old = 0
child_survived = 0
adult_survived = 0
old_survived = 0
child_male = 0
adult_male = 0
old_male = 0
child_male_survived = 0
adult_male_survived = 0
old_male_survived = 0
for i in range(0, passanger):
    if data[i][para("Age")]<=18:
        child += 1
        if data[i][para("Survived")] == 1:
            child_survived += 1
        if data[i][para("Sex")] == 'male':
            child_male += 1
            if data[i][para("Survived")] == 1:
                child_male_survived += 1
        
    elif data[i][para("Age")]<=60:
        adult += 1
        if data[i][para("Survived")] == 1:
            adult_survived += 1
        if data[i][para("Sex")] == 'male':
            adult_male += 1
            if data[i][para("Survived")] == 1:
                adult_male_survived += 1
    else:
        old += 1
        if data[i][para("Survived")] == 1:
            old_survived += 1
        if data[i][para("Sex")] == 'male':
            old_male += 1
            if data[i][para("Survived")] == 1:
                old_male_survived += 1

labels = 'Child', 'Adult', 'Old'
sizes = [child, adult, old]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

labels = 'Child Survived', 'Child Died', 'Adult Survived', 'Adult Died', 'Old Survived', 'Old Died'
sizes = [child_survived, child - child_survived, adult_survived, adult - adult_survived, old_survived, old - old_survived]
fig2, ax2 = plt.subplots()
ax2.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
plt.savefig('4.png')

labels = 'Child Male Survived', 'Child Female Survived'
sizes = [child_male_survived, child_male - child_male_survived]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
plt.savefig('5.png')

labels = 'Adult Male Survived', 'Adult Female Survived'
sizes = [adult_male_survived, adult_male - adult_male_survived]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
plt.savefig('6.png')

labels = 'Old Male Survived', 'Old Female Survived'
sizes = [old_male_survived, old_male - old_male_survived]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
plt.savefig('7.png')

c1 = 0
c2 = 0
c3 = 0
c1_survived = 0
c2_survived = 0
c3_survived = 0
c1_male = 0
c2_male = 0
c3_male = 0
c1_male_survived = 0
c2_male_survived = 0
c3_male_survived = 0
c_c1 = 0
q_c1 = 0
s_c1 = 0
for i in range(0, passanger):
    if data[i][para("Pclass")] == 1:
        c1 += 1
        if data[i][para("Survived")] == 1:
            c1_survived += 1
        if data[i][para("Sex")] == "male":
            c1_male += 1
            if data[i][para("Survived")] == 1:
                c1_male_survived += 1
        if data[i][para("Embarked")] == "C":
            c_c1 += 1
    elif data[i][para("Pclass")] == 2:
        c2 += 1
        if data[i][para("Survived")] == 1:
            c2_survived += 1
        if data[i][para("Sex")] == "male":
            c2_male += 1
            if data[i][para("Survived")] == 1:
                c2_male_survived += 1
        if data[i][para("Embarked")] == "Q":
            q_c1 += 1
    else:
        c3 += 1
        if data[i][para("Survived")] == 1:
            c3_survived += 1
        if data[i][para("Sex")] == "male":
            c3_male += 1
            if data[i][para("Survived")] == 1:
                c3_male_survived += 1
        if data[i][para("Embarked")] == "S":
            s_c1 += 1

labels = 'First Class Passanger', 'Second Class Passanger', 'Third Class Passanger'
sizes = [c1, c2, c3]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
plt.savefig('8.png')

labels = 'First Class Passanger Survived', 'Second Class Passanger Survived', 'Third Class Passanger Survived'
sizes = [c1_survived, c2_survived, c3_survived]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
plt.savefig('9.png')

# In[195]:


labels = 'First Class Passanger Survived', 'First Class Passanger Died'
sizes = [c1_survived, c1 - c1_survived]
fig3, ax3 = plt.subplots()
ax3.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
plt.savefig('10.png')

# In[196]:


labels = 'Second Class Passanger Survived', 'Second Class Passanger Died'
sizes = [c2_survived, c2 - c2_survived]
fig3, ax3 = plt.subplots()
ax3.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
plt.savefig('11.png')

# In[197]:


labels = 'Third Class Passanger Survived', 'Third Class Passanger Died'
sizes = [c3_survived, c3 - c3_survived]
fig4, ax4 = plt.subplots()
ax4.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
plt.savefig('12.png')

# In[198]:


labels = 'First Class Passanger Male Survived', 'Second Class Passanger Male Survived', 'Third Class Passanger Male Survived'
sizes = [c1_male_survived, c2_male_survived, c3_male_survived]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
plt.savefig('13.png')

# In[199]:


labels = 'First Class Passanger Female Survived', 'Second Class Passanger Female Survived', 'Third Class Passanger Female Survived'
sizes = [c1_survived - c1_male_survived, c2_survived - c2_male_survived, c3_survived - c3_male_survived]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
plt.savefig('14.png')

# In[203]:


c = 0
q = 0
s = 0
c_male = 0
q_male = 0
s_male = 0
c_survived = 0
q_survived = 0
s_survived = 0
for i in range(0, passanger):
    if data[i][para("Embarked")] == 'C':
        c += 1
        if data[i][para("Sex")] == 'male':
            c_male += 1
        if data[i][para("Survived")] == 1:
            c_survived += 1
    elif data[i][para("Embarked")] == 'Q':
        q += 1
        if data[i][para("Sex")] == 'male':
            q_male += 1
        if data[i][para("Survived")] == 1:
            q_survived += 1
    else:
        s += 1
        if data[i][para("Sex")] == 'male':
            s_male += 1
        if data[i][para("Survived")] == 1:
            s_survived += 1

labels = 'Embarked from Cherbourg', 'Embarked from Queenstown', 'Embarked from Southampton'
sizes = [c, q, s]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

labels = 'Male from Cherbourg', 'Female from Cherbourg', 'Male from Queenstown', 'Female from Queenstown', 'Male from Southampton', 'Female from Southampton'
sizes = [c_male,c - c_male, q_male, q - q_male, s_male, s - s_male]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
plt.savefig('15.png')
labels = 'First Class Passanger from Cherbourg', 'First Class Passanger from Queenstown', 'First Class Passanger from Southampton'
sizes = [c_c1, q_c1, s_c1]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
plt.savefig('16.png')
labels = 'First Class Passanger from Cherbourg', 'First Class Passanger from Queenstown', 'First Class Passanger from Southampton'
sizes = [c_c1, q_c1, s_c1]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
plt.savefig('16.png')
labels = 'Survived Passanger from Cherbourg', 'Survived Passanger from Queenstown', 'Survived Passanger from Southampton'
sizes = [c_survived, q_survived, s_survived]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()



