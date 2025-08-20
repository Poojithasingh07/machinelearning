 Breast-Cancer-Detection-using-Neural-Network
 # Breast Cancer Detection using Neural Networks

This project uses a feedforward neural network built in TensorFlow/Keras to classify whether a tumor is benign or malignant based on the Breast Cancer  dataset.

 🔍 Dataset
Uses the [Breast Cancer Wisconsin (Diagnostic) Dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#breast-cancer-dataset) from `sklearn.datasets`.

 📦 Requirements
 tensorflow>=2.9.0
 scikit-learn
 numpy
 matplotlib
 
 🧠 Model
- 2 Hidden Layers (ReLU)
- Output Layer (Sigmoid)
- Optimizer: Adam
- Loss: Binary Crossentropy

💻 Running the Project
 python main.py
 The trained model is saved in `/content/breast cancer.csv'.

## 📁 Project Structure
data/
├── model/
│   └── breast_cancer_nn_model.h5
├── notebooks/
├── utils/
├── main.py
└── README.md
