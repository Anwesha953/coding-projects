import streamlit as st
import pickle
import pandas as pd
import os

# -----------------------------
# Load model and columns
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "model.pkl")
columns_path = os.path.join(BASE_DIR, "columns.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(columns_path, "rb") as f:
    training_columns = pickle.load(f)

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦",
    layout="wide"
)

# -----------------------------
# Custom CSS Styling
# -----------------------------
st.markdown("""
    <style>
        .main-title {
            font-size: 2.3rem;
            font-weight: 700;
            color: #1f4e79;
            margin-bottom: 0.2rem;
        }
        .sub-text {
            font-size: 1rem;
            color: #555;
            margin-bottom: 1.5rem;
        }
        .result-card {
            padding: 1.2rem;
            border-radius: 12px;
            margin-top: 1rem;
            margin-bottom: 1rem;
            border: 1px solid #ddd;
            background-color: #f8f9fa;
        }
        .approved {
            color: #1b8a3d;
            font-weight: bold;
            font-size: 1.4rem;
        }
        .not-approved {
            color: #c62828;
            font-weight: bold;
            font-size: 1.4rem;
        }
        .chance-high {
            color: #1b8a3d;
            font-weight: bold;
            font-size: 1.1rem;
        }
        .chance-medium {
            color: #d17b00;
            font-weight: bold;
            font-size: 1.1rem;
        }
        .chance-low {
            color: #c62828;
            font-weight: bold;
            font-size: 1.1rem;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown('<div class="main-title">🏦 Loan Approval Prediction System</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-text">Enter applicant details below to estimate whether the loan is likely to be approved.</div>',
    unsafe_allow_html=True
)

# -----------------------------
# Input Form (2-column layout)
# -----------------------------
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        married = st.selectbox("Married", ["Yes", "No"])
        education = st.selectbox("Education", ["Graduate", "Not Graduate"])
        self_employed = st.selectbox("Self Employed", ["Yes", "No"])

    with col2:
        applicant_income = st.number_input("Applicant Income", min_value=0, value=5000, step=500)
        loan_amount = st.number_input("Loan Amount", min_value=0, value=150, step=10)
        credit_history = st.selectbox("Credit History", [1, 0], help="1 = Good credit history, 0 = Poor/No credit history")
        property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# -----------------------------
# Prediction Button
# -----------------------------
if st.button("🔍 Predict Loan Status", use_container_width=True):
    input_data = {
        "ApplicantIncome": applicant_income,
        "LoanAmount": loan_amount,
        "Credit_History": credit_history,
        "Gender_Female": 1 if gender == "Female" else 0,
        "Gender_Male": 1 if gender == "Male" else 0,
        "Married_No": 1 if married == "No" else 0,
        "Married_Yes": 1 if married == "Yes" else 0,
        "Education_Graduate": 1 if education == "Graduate" else 0,
        "Education_Not Graduate": 1 if education == "Not Graduate" else 0,
        "Self_Employed_No": 1 if self_employed == "No" else 0,
        "Self_Employed_Yes": 1 if self_employed == "Yes" else 0,
        "Property_Area_Rural": 1 if property_area == "Rural" else 0,
        "Property_Area_Semiurban": 1 if property_area == "Semiurban" else 0,
        "Property_Area_Urban": 1 if property_area == "Urban" else 0
    }

    input_df = pd.DataFrame([input_data])

    # Match training columns exactly
    input_df = input_df.reindex(columns=training_columns, fill_value=0)

    # Prediction
    prediction = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]

    # Find probability of "Approved"
    approved_index = list(model.classes_).index("Approved")
    approval_probability = probabilities[approved_index] * 100

    # Approval chance category
    if approval_probability >= 75:
        chance_label = "High Approval Chance"
        chance_class = "chance-high"
    elif approval_probability >= 45:
        chance_label = "Medium Approval Chance"
        chance_class = "chance-medium"
    else:
        chance_label = "Low Approval Chance"
        chance_class = "chance-low"

    # Result display
    st.markdown('<div class="result-card">', unsafe_allow_html=True)

    st.subheader("Prediction Result")

    if prediction == "Approved":
        st.markdown('<div class="approved">✅ Loan Likely to be Approved</div>', unsafe_allow_html=True)
        st.balloons()
    else:
        st.markdown('<div class="not-approved">❌ Loan Likely to be Not Approved</div>', unsafe_allow_html=True)

    st.write(f"**Approval Probability:** {approval_probability:.2f}%")
    st.markdown(f'<div class="{chance_class}">{chance_label}</div>', unsafe_allow_html=True)

    st.progress(min(int(approval_probability), 100))

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Footer note
# -----------------------------
st.markdown("---")
st.caption("Built with Streamlit + Scikit-learn | Project 9")