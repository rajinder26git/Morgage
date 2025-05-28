import streamlit as st

# Function to calculate mortgage (loan EMI)
def calculate_emi(principal, annual_rate, years):
    r = annual_rate / 12 / 100  # Monthly interest rate
    n = years * 12  # Total number of months
    if r == 0:
        return principal / n
    emi = principal * r * (1 + r)**n / ((1 + r)**n - 1)
    return emi

# Format INR with commas (lakhs/crores)
def format_inr(amount):
    return "₹{:,.0f}".format(amount).replace(",", ",")

# Streamlit App
st.title("🏦 Loan EMI Calculator")

# Inputs
principal = st.number_input("Loan Amount (₹)", min_value=0.0, value=300000.0, step=1000.0)
annual_rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, value=6.5, step=0.1)
years = st.slider("Loan Term (Years)", min_value=1, max_value=40, value=5)

# Calculate on button click
if st.button("Calculate Monthly Payment"):
    monthly = calculate_emi(principal, annual_rate, years)
    st.success(f"💰 Your Monthly Payment: **₹{monthly:,.2f}**")
