import os
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "boston_housing.csv")
model_path = os.path.join(BASE_DIR, "model.pkl")

# Load dataset
df = pd.read_csv(csv_path)
X = df.drop("MEDV", axis=1)
y = df["MEDV"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build pipeline (Scaler + Model)
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])

# Train and save
pipeline.fit(X_train, y_train)
with open(model_path, "wb") as f:
    pickle.dump(pipeline, f)

print("✅ model.pkl created at:", model_path)
