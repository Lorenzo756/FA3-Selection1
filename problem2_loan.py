# Problem 2: Loan Eligibility Checker

credit_score = int(input("Enter credit score: "))
annual_income = float(input("Enter annual income: "))
years_at_job = int(input("Enter years at current job: "))

# Check if all loan requirements are met
if credit_score >= 700 and annual_income >= 30000 and years_at_job >= 2:
    print("Result: Loan Approved")
else:
    print("Result: Loan Denied")
