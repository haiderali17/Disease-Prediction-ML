![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green)

# 🩺 Diabetes Prediction System

A Machine Learning web application that predicts whether a patient is likely to have diabetes based on medical information. The application is built using **Python**, **Scikit-learn**, and **Streamlit**, and is deployed online for real-time predictions.

## 🚀 Live Demo

🔗 https://diabetes-predictor-ai.streamlit.app

---

## 📌 Features

- Predicts diabetes using a trained Machine Learning model.
- Clean and responsive Streamlit interface.
- User-friendly input form.
- Displays prediction result instantly.
- Shows prediction confidence (probability).
- Displays patient input summary.
- Deployed online using Streamlit Community Cloud.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Pickle

---

## 📊 Dataset

**Pima Indians Diabetes Dataset**

### Input Features

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- Body Mass Index (BMI)
- Diabetes Pedigree Function
- Age

### Target

- **0** → Non-Diabetic
- **1** → Diabetic

---

## 🤖 Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Data Cleaning
4. Feature Selection
5. Model Training
6. Model Evaluation
7. Model Saving using Pickle
8. Web App Development using Streamlit
9. Deployment on Streamlit Community Cloud

---

## 📈 Model Performance

| Model | Accuracy |
|--------|----------|
| Logistic Regression | **75.32%** |
| Random Forest | 74.68% |

**Final Model:** Logistic Regression

---

## 📂 Project Structure

```
Disease-Prediction-ML/
│
├── app.py
├── model.pkl
├── diabetes.csv
├── requirements.txt
├── README.md
└── Diseases_Prediction.ipynb
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/haiderali17/Disease-Prediction-ML.git
```

Go to the project folder:

```bash
cd Disease-Prediction-ML
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---


## ⚠️ Disclaimer

This project is developed for educational purposes only and should not be considered a substitute for professional medical advice or diagnosis.

---

## 👨‍💻 Author

**Haider Ali**

- GitHub: https://github.com/haiderali17

---

⭐ If you found this project useful, consider giving it a star.