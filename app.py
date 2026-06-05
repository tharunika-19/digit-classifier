import streamlit as st
import tensorflow as tf
import numpy as np
from streamlit_drawable_canvas import st_canvas
from PIL import Image

model = tf.keras.models.load_model('digit_classifier.keras')

st.title("🔢 Handwritten Digit Classifier")
st.write("Draw a digit (0–9) in the box below")

canvas = st_canvas(
    fill_color="black",
    stroke_width=20,
    stroke_color="white",
    background_color="black",
    height=280, width=280,
    drawing_mode="freedraw",
    key="canvas"
)

if st.button("Predict"):
    if canvas.image_data is not None:
        img = Image.fromarray(canvas.image_data.astype('uint8'))
        img = img.convert('L').resize((28, 28))
        img_array = np.array(img) / 255.0
        img_array = 1 - img_array
        img_array = img_array.reshape(1, 784)
        
        prediction = model.predict(img_array)
        digit = np.argmax(prediction)
        confidence = prediction[0][digit] * 100
        
        st.success(f"Predicted Digit: **{digit}**")
        st.info(f"Confidence: **{confidence:.2f}%**")
        
        st.bar_chart({str(i): prediction[0][i] for i in range(10)})
