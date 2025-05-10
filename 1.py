import pandas as pd

# Load data
df1 = pd.read_csv('facebook_metrics1.csv')
df2 = pd.read_csv('facebook_metrics2.csv')

# a. Subset
subset = df1[['Type', 'Total Reach', 'Total Engagement']]

# b. Merge (on 'Type') and c. Sort by 'Total Reach'
merged = pd.merge(df1, df2, on='Type', how='inner').sort_values('Total Reach', ascending=False)

# d. Transpose
transposed = merged.T

# e. Shape and Reshape
print("Shape:", merged.shape)
reshaped = pd.melt(merged, id_vars=['Type'], value_vars=['Total Reach', 'Total Engagement'])

# Output samples
print(subset.head(), transposed.head(), reshaped.head(), sep='\n\n')
