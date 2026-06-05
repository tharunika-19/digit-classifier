# 🔢 Handwritten Digit Classifier

A Machine Learning web application that recognizes handwritten digits (0–9) using a neural network trained on the MNIST dataset.

## 📌 Overview

This project uses TensorFlow/Keras to train a digit classification model and Streamlit to provide an interactive user interface where users can draw digits and receive real-time predictions.

## 🚀 Features

* Draw digits directly on a canvas
* Real-time digit prediction
* Confidence score display
* Probability distribution visualization
* Interactive Streamlit interface
* TensorFlow/Keras neural network model

## 🛠️ Tech Stack

* Python
* TensorFlow / Keras
* NumPy
* Streamlit
* Pillow
* streamlit-drawable-canvas

## 📊 Dataset

The model is trained on the MNIST dataset containing:

* 60,000 training images
* 10,000 test images
* Grayscale images of size 28×28 pixels
* Digits from 0 to 9

## 🧠 Model Architecture

Input Layer:

* 784 input features (28×28 flattened image)

Hidden Layers:

* Dense Layer (128 neurons, ReLU)
* Dropout Layer (0.2)
* Dense Layer (64 neurons, ReLU)

Output Layer:

* Dense Layer (10 neurons, Softmax)

## 📈 Performance

* Optimizer: Adam
* Loss Function: Sparse Categorical Crossentropy
* Accuracy: ~98% on the MNIST test dataset

## ▶️ Running Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📂 Project Structure

```text
digit-classifier/
│
├── app.py
├── digit_classifier.keras
├── requirements.txt
└── README.md
```

## 🎯 Learning Outcomes

Through this project, I gained hands-on experience with:

* Neural Networks
* Image Classification
* TensorFlow/Keras
* Model Deployment
* Streamlit Web Applications
* Data Preprocessing

## 👩‍💻 Author

**Tharunika Bodasu**

B.Tech Artificial Intelligence & Machine Learning
Jawaharlal Nehru Technological University Hyderabad

GitHub: https://github.com/tharunika-19
LinkedIn: https://linkedin.com/in/tharunikabodasu
