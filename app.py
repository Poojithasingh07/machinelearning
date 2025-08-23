import os
import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.datasets import fetch_california_housing  # modern dataset (Boston is deprecated)

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model.pkl")

# If model.pkl does not exist → train and save
if not os.path.exists(model_path):
    print("⚠️ model.pkl not found → training new model...")

    # Load California Housing dataset (no CSV needed)
    data = fetch_california_housing(as_frame=True)
    df = data.frame
    X = df.drop("MedHouseVal", axis=1)
    y = df["MedHouseVal"]

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Pipeline (scaler + model)
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", LinearRegression())
    ])

    pipeline.fit(X_train, y_train)

    # Save trained pipeline
    with open(model_path, "wb") as f:
        pickle.dump(pipeline, f)

    print("✅ model.pkl trained and saved.")

# Load trained model
model = pickle.load(open(model_path, "rb"))

# Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        features_array = np.array(features).reshape(1, -1)
        prediction = model.predict(features_array)[0]
        return render_template("home.html",
                               prediction_text=f"🏡 Predicted House Price: ${prediction:.2f}")
    except Exception as e:
        return render_template("home.html", prediction_text=f"⚠️ Error: {str(e)}")


if __name__ == "__main__":
    print("🚀 Your app is running at: http://127.0.0.1:8000")
    app.run(debug=True, port=8000)


