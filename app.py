import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl","rb"))

st.title("🩺 Diabetes Prediction System")

preg = st.number_input("Pregnancies")
glucose = st.number_input("Glucose")
bp = st.number_input("Blood Pressure")
skin = st.number_input("Skin Thickness")
insulin = st.number_input("Insulin")
bmi = st.number_input("BMI")
dpf = st.number_input("Diabetes Pedigree Function")
age = st.number_input("Age")

if st.button("Predict"):

    data = np.array([[preg, glucose, bp, skin,
                      insulin, bmi, dpf, age]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Patient is likely to have Diabetes.")
    else:
        st.success("Patient is not likely to have Diabetes.")