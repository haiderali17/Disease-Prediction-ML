import streamlit as st
import pickle
import numpy as np

# -------------------- Page Config --------------------
st.set_page_config(
    page_title="Diabetes Prediction System",
    page_icon="🩺",
    layout="centered"
)

# -------------------- Load Model --------------------
model = pickle.load(open("model.pkl", "rb"))

# -------------------- Sidebar --------------------
st.sidebar.title("🩺 Diabetes Prediction")
st.sidebar.info(
    """
This application predicts whether a patient is likely
to have diabetes using a trained Machine Learning model.
"""
)

# -------------------- Title --------------------
st.title("🩺 Diabetes Prediction System")
st.markdown(
    "Enter the patient's medical information below and click **Predict**."
)

st.divider()

# -------------------- Input Fields --------------------
preg = st.number_input(
    "Pregnancies",
    min_value=0,
    max_value=20,
    value=1,
    step=1,
)

glucose = st.number_input(
    "Glucose",
    min_value=0,
    max_value=300,
    value=120,
    step=1,
)

bp = st.number_input(
    "Blood Pressure",
    min_value=0,
    max_value=200,
    value=70,
    step=1,
)

skin = st.number_input(
    "Skin Thickness",
    min_value=0,
    max_value=100,
    value=20,
    step=1,
)

insulin = st.number_input(
    "Insulin",
    min_value=0,
    max_value=900,
    value=80,
    step=1,
)

bmi = st.number_input(
    "BMI",
    min_value=0.0,
    max_value=70.0,
    value=25.0,
    step=0.1,
    format="%.1f",
)

dpf = st.number_input(
    "Diabetes Pedigree Function",
    min_value=0.0,
    max_value=3.0,
    value=0.50,
    step=0.01,
    format="%.2f",
)

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=30,
    step=1,
)

st.divider()

# -------------------- Prediction --------------------
if st.button("🔍 Predict", use_container_width=True):

    data = np.array([[preg, glucose, bp, skin,
                      insulin, bmi, dpf, age]])

    prediction = model.predict(data)[0]

    # Probability (if supported)
    try:
        probability = model.predict_proba(data)[0][1] * 100
    except:
        probability = None

    if prediction == 1:
        st.error("⚠️ Patient is likely to have Diabetes.")
    else:
        st.success("✅ Patient is unlikely to have Diabetes.")

    if probability is not None:
        st.metric(
            label="Prediction Confidence",
            value=f"{probability:.2f}%"
        )

st.divider()

st.caption("Developed using Python • Streamlit • Scikit-learn")