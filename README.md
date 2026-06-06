<div align="center">

# 🔢 Handwritten Digit Classifier

### Deep Learning · Computer Vision · TensorFlow/Keras · Deployed on HuggingFace Spaces

[![HuggingFace](https://img.shields.io/badge/🤗%20Live%20Demo-HuggingFace%20Spaces-FFD21E?style=for-the-badge)](https://huggingface.co/spaces/tharunika19/digit-classifier1)
[![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)

<br/>

> **Draw any digit (0–9) on the canvas. The model tells you what it thinks — in real time.**

<br/>

![accuracy](https://img.shields.io/badge/Test%20Accuracy-98.28%25-brightgreen?style=flat-square)
![dataset](https://img.shields.io/badge/Dataset-MNIST%2070K%20images-blue?style=flat-square)
![status](https://img.shields.io/badge/Status-Live-success?style=flat-square)

</div>

---

## ✨ What It Does

A neural network trained from scratch on the MNIST dataset that classifies handwritten digits with **98.28% test accuracy**. The live demo lets anyone draw a digit on an interactive canvas and get an instant prediction with confidence score.

---

## 🧠 Model Architecture

```
Input (784)  →  Dense(128, ReLU)  →  Dropout(0.2)  →  Dense(64, ReLU)  →  Dense(10, Softmax)
```

| Layer | Details |
|---|---|
| Input | 784 neurons (28×28 flattened) |
| Hidden Layer 1 | Dense(128) + ReLU activation |
| Regularization | Dropout(0.2) to prevent overfitting |
| Hidden Layer 2 | Dense(64) + ReLU activation |
| Output | Dense(10) + Softmax (one per digit class) |

---

## 📊 Results

| Metric | Value |
|---|---|
| **Test Accuracy** | **98.28%** |
| Optimizer | Adam |
| Loss Function | Sparse Categorical Crossentropy |
| Epochs | 10 |
| Training Samples | 60,000 |
| Test Samples | 10,000 |

<img width="1366" height="876" alt="image" src="https://github.com/user-attachments/assets/5f668b4b-9f79-4136-8d84-5b8fc5395fcd" />
<img width="1197" height="816" alt="image" src="https://github.com/user-attachments/assets/7f122e07-7af7-433b-84b1-b47f472e9c09" />



---

## 🗂️ Dataset

**MNIST** — Modified National Institute of Standards and Technology database

- 70,000 grayscale images of handwritten digits (0–9)
- Image size: 28 × 28 pixels
- 60,000 training / 10,000 test split
- Pixel values normalized to [0, 1]

---

## 🚀 Try It Live

👉 **[Open the Live Demo](https://tharunika19-digit-classifier1.hf.space/)**

1. Draw a digit on the canvas
2. Click **Predict**
3. See the predicted digit + confidence score instantly

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| TensorFlow / Keras | Model building & training |
| NumPy | Data preprocessing |
| Matplotlib | Accuracy/loss visualization |
| Streamlit | Interactive web app |
| HuggingFace Spaces | Cloud deployment |
| Google Colab | Training environment |

---

## 📁 Project Structure

```
digit-classifier/
├── app.py               # Streamlit app with drawable canvas
├── model.h5             # Trained Keras model
├── train.ipynb          # Google Colab training notebook
├── requirements.txt     # Dependencies
└── README.md
```

---

## 💻 Run Locally

```bash
git clone https://github.com/tharunika-19/digit-classifier
cd digit-classifier
pip install -r requirements.txt
streamlit run app.py
```

---

## 📚 Concepts Demonstrated

- **Neural Network design** — layer stacking, activation functions
- **Regularization** — Dropout to reduce overfitting
- **Training pipeline** — compile → fit → evaluate
- **Model serialization** — saving and loading `.h5` files
- **ML deployment** — Streamlit frontend on HuggingFace Spaces

---

<div align="center">

Built by [Tharunika](https://github.com/tharunika-19) · B.Tech CSE (AIML) · JNTUH

⭐ Star this repo if you found it useful!

</div>
