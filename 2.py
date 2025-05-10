import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load and clean
air = pd.read_csv('air_quality.csv').drop_duplicates().dropna()
dis = pd.read_csv('diseases.csv').drop_duplicates().fillna(0)

# Fix city names and numeric types
air['City'] = air['City'].str.title().str.strip()
dis['City'] = dis['City'].str.title().str.strip()
for col in ['PM2.5', 'PM10', 'NO2']: air[col] = pd.to_numeric(air[col], errors='coerce')
for col in ['Respiratory Cases', 'Heart Disease Cases']: dis[col] = pd.to_numeric(dis[col], errors='coerce')

# Merge and fix negatives
df = pd.merge(air, dis, on='City')
cols = ['PM2.5', 'PM10', 'NO2', 'Respiratory Cases', 'Heart Disease Cases']
df[cols] = df[cols].clip(lower=0)

# Transform
df[cols] = MinMaxScaler().fit_transform(df[cols])

# Model
X, y = df[['PM2.5', 'PM10', 'NO2']], df['Respiratory Cases']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression().fit(X_train, y_train)
print("MSE:", mean_squared_error(y_test, model.predict(X_test)))
