import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("UberDataset.csv")
dataset.head()

dataset.shape

dataset.info()

dataset['PURPOSE'].fillna("NOT", inplace=True)

dataset['START_DATE'] = pd.to_datetime(dataset['START_DATE'], errors='coerce')
dataset['END_DATE'] = pd.to_datetime(dataset['END_DATE'], errors='coerce')

from datetime import datetime

dataset['date'] = pd.DatetimeIndex(dataset['START_DATE']).date
dataset['time'] = pd.DatetimeIndex(dataset['START_DATE']).hour

# changing into categories of day and night
dataset['day-night'] = pd.cut(x=dataset['time'], bins=[0, 10, 15, 19, 24],
                              labels=['Morning','Afternoon','Evening','Night'])

dataset.dropna(inplace=True)
dataset.drop_duplicates(inplace=True)

obj = (dataset.dtypes == 'object')
object_cols = list(obj[obj].index)
unique_values = {}
for col in object_cols:
    unique_values[col] = dataset[col].unique().size
unique_values

# First subplot
ax1 = plt.subplot(1, 2, 1)
sns.countplot(x='CATEGORY', data=dataset, ax=ax1, palette='viridis')
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=90)
# Second subplot
ax2 = plt.subplot(1, 2, 2)
sns.countplot(x='PURPOSE', data=dataset, ax=ax2, palette='coolwarm')
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=90)
# Show the plot
plt.tight_layout()  # Adjusts layout to prevent overlap
plt.show()

# Create a figure for the plot
plt.figure(figsize=(8, 5))
# Create a single subplot
ax1 = plt.subplot(1, 1, 1)
# Use seaborn countplot with the specified palette
sns.countplot(x='day-night', data=dataset, ax=ax1, palette='viridis')
# Rotate x-axis labels for better readability
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=90)
# Show the plot
plt.tight_layout()
plt.show()

plt.figure(figsize=(15, 5))
sns.countplot(data=dataset, x='PURPOSE', hue='CATEGORY')
plt.xticks(rotation=90)
plt.show()