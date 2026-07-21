import streamlit as st
import pickle
import numpy as np

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Diabetes Prediction System",
    page_icon="🩺",
    layout="wide"
)

# ---------------- Load Model ----------------
model = pickle.load(open("model.pkl", "rb"))

# ---------------- Sidebar ----------------
st.sidebar.title("🩺 Diabetes Prediction")
st.sidebar.markdown("""
### About
This app predicts whether a patient is likely to have diabetes using a Machine Learning model.

### Input Features
- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age
""")

# ---------------- Title ----------------
st.title("🩺 Diabetes Prediction System")
st.write("Fill in the patient's details below and click **Predict Diabetes**.")

st.divider()

# ---------------- Input Layout ----------------
col1, col2 = st.columns(2)

with col1:

    preg = st.number_input(
        "Pregnancies",
        min_value=0,
        max_value=20,
        value=1,
        step=1
    )

    glucose = st.number_input(
        "Glucose",
        min_value=0,
        max_value=300,
        value=120,
        step=1
    )

    bp = st.number_input(
        "Blood Pressure",
        min_value=0,
        max_value=200,
        value=80,
        step=1
    )

    skin = st.number_input(
        "Skin Thickness",
        min_value=0,
        max_value=100,
        value=20,
        step=1
    )

with col2:

    insulin = st.number_input(
        "Insulin",
        min_value=0,
        max_value=900,
        value=80,
        step=1
    )

    bmi = st.number_input(
        "BMI",
        min_value=0.0,
        max_value=70.0,
        value=25.0,
        step=0.1,
        format="%.1f"
    )

    dpf = st.number_input(
        "Diabetes Pedigree Function",
        min_value=0.0,
        max_value=3.0,
        value=0.50,
        step=0.01,
        format="%.2f"
    )

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=30,
        step=1
    )

st.divider()

# ---------------- Prediction ----------------

if st.button("🔍 Predict Diabetes", use_container_width=True):

    data = np.array([[preg,
                      glucose,
                      bp,
                      skin,
                      insulin,
                      bmi,
                      dpf,
                      age]])

    prediction = model.predict(data)[0]

    probability = None

    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(data)[0][1] * 100

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ The patient is likely to have Diabetes.")
    else:
        st.success("✅ The patient is unlikely to have Diabetes.")

    if probability is not None:

        st.metric(
            "Diabetes Probability",
            f"{probability:.2f}%"
        )

        st.progress(min(int(probability),100))

    st.divider()

    st.subheader("Input Summary")

    st.write(f"**Pregnancies:** {preg}")
    st.write(f"**Glucose:** {glucose}")
    st.write(f"**Blood Pressure:** {bp}")
    st.write(f"**Skin Thickness:** {skin}")
    st.write(f"**Insulin:** {insulin}")
    st.write(f"**BMI:** {bmi}")
    st.write(f"**Diabetes Pedigree Function:** {dpf}")
    st.write(f"**Age:** {age}")

st.divider()

st.caption("Developed using Python • Streamlit • Scikit-learn")