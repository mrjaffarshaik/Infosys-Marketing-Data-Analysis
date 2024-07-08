# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 20:36:11 2024

@author: HP
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Read the CSV file
file_path = (r"C:\Users\HP\Downloads\Rocketium EIR Internship Assignment - Twitter posts.csv")
df = pd.read_csv(file_path)
# Print the first few lines of the CSV file
print(df.head())


# Step 3: Data Cleaning and Preprocessing
# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Fill missing values with 0
df.fillna(0, inplace=True)

# Step 4: Define the performance metrics 
metrics = ['views', 'likes', 'comments', 'shares', 'total engagements', 'engagement rate %']

# Step 5: Display summary statistics for the performance metrics
print(df[metrics].describe())

# Step 6: Visualize the distribution of performance metrics
plt.figure(figsize=(15, 10))
plt.figure(figsize=(15, 10))
for i, metric in enumerate(metrics, 1):
    plt.subplot(2, 3, i)
    sns.histplot(df[metric], kde=True)
    plt.title(f'Distribution of {metric}')
plt.tight_layout()
plt.show()

# Step 7: Investigate the relationship between creative attributes and performance metrics
# Group by 'company name' and 'post topic' and calculate the mean of performance metrics
grouped = df.groupby(['company name', 'post topic'])[metrics].mean().reset_index()

# Step 8: Visualize the relationship between 'company name' and performance metrics
plt.figure(figsize=(15, 10))
for i, metric in enumerate(metrics, 1):
    plt.subplot(2, 3, i)
    sns.barplot(x='company name', y=metric, data=grouped)
    plt.title(f'{metric} by Company Name')
    plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 9: Visualize the relationship between 'post topic' and performance metrics
plt.figure(figsize=(15, 10))
for i, metric in enumerate(metrics, 1):
    plt.subplot(2, 3, i)
    sns.barplot(x='post topic', y=metric, data=grouped)
    plt.title(f'{metric} by Post Topic')
    plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 10: Investigate the influence of logos and number of persons on engagement
# Create a new column 'has_logo' to indicate the presence of logos
df['has_logo'] = df['logos'].apply(lambda x: 1 if x != 0 else 0)

# Group by 'has_logo' and calculate the mean of performance metrics
grouped_logos = df.groupby('has_logo')[metrics].mean().reset_index()

# Group by 'number of persons' and calculate the mean of performance metrics
grouped_persons = df.groupby('number of persons')[metrics].mean().reset_index()

# Step 11: Visualize the influence of logos on performance metrics
plt.figure(figsize=(15, 10))
for i, metric in enumerate(metrics, 1):
    plt.subplot(2, 3, i)
    sns.barplot(x='has_logo', y=metric, data=grouped_logos)
    plt.title(f'{metric} by Presence of Logos')
plt.tight_layout()
plt.show()

# Step 12: Visualize the influence of number of persons on performance metrics
plt.figure(figsize=(15, 10))
for i, metric in enumerate(metrics, 1):
    plt.subplot(2, 3, i)
    sns.barplot(x='number of persons', y=metric, data=grouped_persons)
    plt.title(f'{metric} by Number of Persons')
plt.tight_layout()
plt.show()
