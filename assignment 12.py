
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create customer churn dataset
data = {
    'Age': [25, 34, 45, np.nan, 29, 52, 41, 36, np.nan, 48],
    'MonthlyCharges': [50, 80, 65, 90, np.nan, 100, 70, 85, 95, 60],
    'Tenure': [2, 12, 36, 5, 8, 48, 24, np.nan, 3, 60],
    'Contract': ['Monthly', 'Yearly', 'Two Year', 'Monthly',
                 'Monthly', 'Two Year', 'Yearly', 'Monthly',
                 'Monthly', 'Two Year'],
    'Churn': ['Yes', 'No', 'No', 'Yes', 'Yes', 'No',
              'No', 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)

print("Original Dataset:\n", df)

# 1. Check missing values
print("\nMissing Values:\n", df.isnull().sum())

# 2. Handle missing values using median
for col in ['Age', 'MonthlyCharges', 'Tenure']:
    df[col] = df[col].fillna(df[col].median())

# 3. Remove duplicate records
df.drop_duplicates(inplace=True)

print("\nCleaned Dataset:\n", df)

# 4. Summary statistics
print("\nSummary Statistics:\n", df.describe())

print("\nMean:\n", df[['Age', 'MonthlyCharges', 'Tenure']].mean())
print("\nMedian:\n", df[['Age', 'MonthlyCharges', 'Tenure']].median())
print("\nMinimum:\n", df[['Age', 'MonthlyCharges', 'Tenure']].min())
print("\nMaximum:\n", df[['Age', 'MonthlyCharges', 'Tenure']].max())

# 5. Analyze customer churn
print("\nChurn Count:\n", df['Churn'].value_counts())
print("\nChurn by Contract:\n", pd.crosstab(df['Contract'], df['Churn']))

# 6. Visualize results
df['Churn'].value_counts().plot(kind='bar', title='Customer Churn')
plt.xlabel('Churn')
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.show()

df.groupby('Churn')['MonthlyCharges'].mean().plot(
    kind='bar', title='Average Monthly Charges by Churn'
)
plt.ylabel('Average Charges')
plt.tight_layout()
plt.show()

pd.crosstab(df['Contract'], df['Churn']).plot(
    kind='bar', title='Churn by Contract Type'
)
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.show()
