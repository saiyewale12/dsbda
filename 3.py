import pandas as pd, seaborn as sns, matplotlib.pyplot as plt

# Load datasets
fire = pd.read_csv('forest_fire.csv')
air = pd.read_csv('air_quality.csv')
heart = pd.read_csv('heart_disease.csv')

# Set style
sns.set(style='whitegrid'); plt.figure(figsize=(15,10))

# Forest Fire - Temperature vs Area
plt.subplot(2,2,1); sns.scatterplot(data=fire, x='temp', y='area').set_title('Forest Fire: Temp vs Area')

# Air Quality - PM2.5 distribution
plt.subplot(2,2,2); sns.histplot(data=air, x='PM2.5', kde=True).set_title('Air Quality: PM2.5')

# Heart Disease - Age vs Cholesterol by Target
plt.subplot(2,2,3); sns.boxplot(data=heart, x='target', y='chol').set_title('Heart Disease: Cholesterol by Target')

# Heart Disease - Correlation Heatmap
plt.subplot(2,2,4); sns.heatmap(heart.corr(), cmap='coolwarm', annot=False).set_title('Heart Disease: Correlation Heatmap')

plt.tight_layout(); plt.show()
