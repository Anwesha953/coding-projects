import pandas as pd
import random
import os

# Get current folder path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "loan_data.csv")

# Reproducible results
random.seed(42)

data = []

for _ in range(300):
    gender = random.choice(["Male", "Female"])
    married = random.choice(["Yes", "No"])
    education = random.choice(["Graduate", "Not Graduate"])
    self_employed = random.choice(["Yes", "No"])
    applicant_income = random.randint(1500, 10000)
    loan_amount = random.randint(50, 300)
    credit_history = random.choice([0, 1])
    property_area = random.choice(["Urban", "Rural", "Semiurban"])

    # Approval logic
    if credit_history == 1 and applicant_income > 3500 and loan_amount < 220:
        loan_status = "Approved"
    elif credit_history == 1 and applicant_income > 6000:
        loan_status = "Approved"
    else:
        loan_status = "Not Approved"

    data.append([
        gender, married, education, self_employed,
        applicant_income, loan_amount, credit_history,
        property_area, loan_status
    ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "Gender", "Married", "Education", "Self_Employed",
    "ApplicantIncome", "LoanAmount", "Credit_History",
    "Property_Area", "Loan_Status"
])

# Save CSV
df.to_csv(csv_path, index=False)

print("loan_data.csv generated successfully!")
print(f"Saved at: {csv_path}")
print(f"Total rows: {len(df)}")