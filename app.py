import streamlit as st
import pickle
import numpy as np

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Diabetes Prediction System",
    page_icon="🩺",
    layout="wide"
)

st.markdown("""
<style>

.main{
    background-color:#f7f9fc;
}

.block-container{
    padding-top:5rem;
    padding-bottom:2rem;
}
            
.stButton > button{
    width:100%;
    background-color:#2563EB !important;
    color:white !important;
    border:none !important;
    border-radius:12px;
    height:55px;
    font-size:18px;
    font-weight:600;
    transition:0.3s;
}

.stButton > button:hover{
    background-color:#1D4ED8 !important;
    color:white !important;
}

.metric-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.1);
}

.success-box{
    background:linear-gradient(135deg,#166534,#22C55E);
    color:white;
    padding:20px;
    border-radius:15px;
}

.danger-box{
    background:linear-gradient(135deg,#991B1B,#EF4444);
    color:white;
    padding:20px;
    border-radius:15px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:50px;
}

</style>
""",unsafe_allow_html=True)



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
st.write(
"Predict whether a patient is likely to have diabetes using a Machine Learning model."
)
st.write("Fill in the patient's details below and click **Predict Diabetes**.")

st.divider()

# ---------------- Input Layout ----------------
col1, col2 = st.columns(2)

with col1:

    preg = st.number_input(
        "🤰 Pregnancies",
        min_value=0,
        max_value=20,
        value=1,
        step=1,
        help="Number of times the patient has been pregnant."
    )
    st.caption("Typical range: 0–10")

    glucose = st.number_input(
        "🩸 Glucose (mg/dL)",
        min_value=0,
        max_value=300,
        value=120,
        step=1,
        help="Plasma glucose concentration after a glucose tolerance test."
    )
    st.caption("Normal fasting glucose: **70–100 mg/dL**")

    bp = st.number_input(
        "💓 Blood Pressure (mmHg)",
        min_value=0,
        max_value=200,
        value=80,
        step=1,
        help="Diastolic blood pressure in mmHg."
    )
    st.caption("Healthy range: **80–120 mmHg**")

    skin = st.number_input(
        "📏 Skin Thickness (mm)",
        min_value=0,
        max_value=100,
        value=20,
        step=1,
        help="Triceps skin fold thickness."
    )
    st.caption("Typical range: **10–50 mm**")

with col2:

    insulin = st.number_input(
        "💉 Insulin (mu U/ml)",
        min_value=0,
        max_value=900,
        value=80,
        step=1,
        help="2-Hour serum insulin level."
    )
    st.caption("Typical range: **16–166 mu U/ml**")

    bmi = st.number_input(
        "⚖️ Body Mass Index (BMI)",
        min_value=0.0,
        max_value=70.0,
        value=25.0,
        step=0.1,
        format="%.1f",
        help="Body Mass Index = Weight / Height²."
    )
    st.caption("Healthy BMI: **18.5–24.9**")

    dpf = st.number_input(
        "🧬 Diabetes Pedigree Function",
        min_value=0.0,
        max_value=3.0,
        value=0.50,
        step=0.01,
        format="%.2f",
        help="Indicates hereditary risk of diabetes."
    )
    st.caption("Higher value = Higher genetic risk")

    age = st.number_input(
        "🎂 Age (Years)",
        min_value=1,
        max_value=120,
        value=30,
        step=1,
        help="Patient's current age."
    )
    st.caption("Enter age in completed years.")
st.divider()


# ---------------- Prediction ----------------

if st.button("🔍 Predict Diabetes", use_container_width=True):

    data = np.array([[
        preg,
        glucose,
        bp,
        skin,
        insulin,
        bmi,
        dpf,
        age
    ]])

    prediction = model.predict(data)[0]

    probability = None
    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(data)[0][1] * 100

    st.divider()
    st.subheader("🩺 Prediction Result")

    if prediction == 1:

        st.markdown("""
        <div class="danger-box">
        <h2>⚠️ High Risk Detected</h2>
        <p>The patient is likely to have <b>Diabetes</b>.</p>
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div class="success-box">
        <h2>✅ Low Risk</h2>
        <p>The patient is unlikely to have <b>Diabetes</b>.</p>
        </div>
        """, unsafe_allow_html=True)

    # ---------------- Probability ----------------

    if probability is not None:

        st.subheader("📊 Prediction Confidence")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Diabetes Risk",
                f"{probability:.2f}%"
            )

        with col2:
            st.metric(
                "Prediction",
                "Positive" if prediction == 1 else "Negative"
            )

        st.progress(min(int(probability), 100))

        st.caption(f"Model Confidence: {probability:.2f}%")

    # ---------------- Input Summary ----------------

    st.divider()

    st.subheader("📋 Patient Input Summary")

    summary = {
        "Feature": [
            "Pregnancies",
            "Glucose",
            "Blood Pressure",
            "Skin Thickness",
            "Insulin",
            "BMI",
            "Diabetes Pedigree Function",
            "Age"
        ],
        "Value": [
            preg,
            glucose,
            bp,
            skin,
            insulin,
            bmi,
            dpf,
            age
        ]
    }

    st.table(summary)

    st.info(
        "This prediction is generated using a Machine Learning model and is intended for educational purposes only. It should not replace professional medical advice."
    )

st.divider()

st.markdown("""
<div class="footer">

<b>Developed by Haider Ali</b><br>

Python • Streamlit • Scikit-Learn

</div>
""", unsafe_allow_html=True)