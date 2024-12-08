import pandas as pd
import numpy as np

file_path = r"C:\Users\ASUS\Downloads\myexcel.xlsx"
df = pd.read_excel(file_path)

# Replace 'height' column values with random integers between 150 and 180
df['height'] = np.random.randint(150, 181, df.shape[0])

df.info()
print(df.head())
import matplotlib.pyplot as plt

# Distribution of employees across each team
team_distribution = df['Team'].value_counts()
team_percentage = (team_distribution / df.shape[0]) * 100

# Print team distribution and percentage
print("Team Distribution:\n", team_distribution)
print("\nTeam Percentage:\n", team_percentage)

# Plot the distribution
plt.figure(figsize=(8, 6))
team_distribution.plot(kind='bar', color='skyblue')
plt.title("Distribution of Employees by Team")
plt.xlabel("Team")
plt.ylabel("Number of Employees")
plt.show()

# Distribution of employees by position
position_distribution = df['Position'].value_counts()
print("Position Distribution:\n", position_distribution)

# Plot the distribution
plt.figure(figsize=(8, 6))
position_distribution.plot(kind='bar', color='lightgreen')
plt.title("Distribution of Employees by Position")
plt.xlabel("Position")
plt.ylabel("Number of Employees")
plt.show()

# Define age bins and labels
age_bins = [20, 30, 40, 50, 60]
age_labels = ['20-29', '30-39', '40-49', '50-59']
df['age_group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)

# Count the number of employees in each age group
age_group_distribution = df['age_group'].value_counts().sort_index()
print("Age Group Distribution:\n", age_group_distribution)

# Plot the age group distribution
plt.figure(figsize=(8, 6))
age_group_distribution.plot(kind='bar', color='orange')
plt.title("Age Group Distribution")
plt.xlabel("Age Group")
plt.ylabel("Number of Employees")
plt.show()

# Total salary expenditure by team
team_salary_expenditure = df.groupby('Team')['Salary'].sum()
highest_salary_team = team_salary_expenditure.idxmax()
print("Highest Salary Expenditure by Team:", highest_salary_team)

# Total salary expenditure by position
position_salary_expenditure = df.groupby('Position')['Salary'].sum()
highest_salary_position = position_salary_expenditure.idxmax()
print("Highest Salary Expenditure by Position:", highest_salary_position)

# Plot salary expenditure by team and position
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

team_salary_expenditure.plot(kind='bar', color='purple', ax=axs[0])
axs[0].set_title("Salary Expenditure by Team")
axs[0].set_xlabel("Team")
axs[0].set_ylabel("Total Salary")

position_salary_expenditure.plot(kind='bar', color='teal', ax=axs[1])
axs[1].set_title("Salary Expenditure by Position")
axs[1].set_xlabel("Position")
axs[1].set_ylabel("Total Salary")

plt.tight_layout()
plt.show()

import seaborn as sns

# Calculate correlation
correlation = df[['Age', 'Salary']].corr().iloc[0, 1]
print(f"Correlation between Age and Salary: {correlation}")

# Scatter plot of age vs salary
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Age', y='Salary', data=df)
plt.title("Correlation between Age and Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

# Insights for Team Distribution
print("\n1. Team Distribution Insights:")
print("The team distribution shows that the New Orleans Pelicans and Memphis Grizzlies have the highest representation in this dataset with 4.1% and 3.9% of employees, respectively.")
print("Overall, most teams have an even distribution of around 3.3% of the workforce each.")

# Insights for Position Distribution
print("\n2. Position Distribution Insights:")
print("The most common positions are Shooting Guard (SG) and Power Forward (PF), which together make up a significant portion of the workforce.")
print("Center (C) is the least represented position, which may indicate a higher demand for guards and forwards or their higher retention in teams.")

# Insights for Age Group Distribution
print("\n3. Age Group Distribution Insights:")
print("Most employees (346) are in the 20-29 age group, followed by 91 in the 30-39 range.")
print("This reflects a younger workforce typical for high-performance roles like professional athletes, as no employees are aged 40 or older.")

# Insights for Salary Expenditure by Team and Position
print("\n4. Salary Expenditure Insights:")
print("The team with the highest salary expenditure is the Cleveland Cavaliers, suggesting they may prioritize investing in high-value players.")
print("Among positions, Centers (C) have the highest total salary expenditure, likely due to the demand for this specific skill set.")

# Insights for Correlation between Age and Salary
print("\n5. Correlation between Age and Salary Insight:")
print(f"The correlation between age and salary is {correlation:.2f}, which shows a weak positive relationship.")
print("This indicates that salary tends to increase slightly with age, but age alone is not a strong predictor of salary. Performance, experience, and position likely play a larger role.")

