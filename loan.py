import streamlit as st

# Function to calculate mortgage
def calculate_mortgage(principal, annual_rate, years):
    r = annual_rate / 12 / 100
    n = years * 12
    if r == 0:
        return principal / n
    monthly_payment = principal * (r * (1 + r)**n) / ((1 + r)**n - 1)
    return monthly_payment

# Streamlit App UI
st.title("🏡 Simple Mortgage Calculator")

# Inputs
principal = st.number_input("Loan Amount ($)", min_value=0.0, value=300000.0, step=1000.0)
annual_rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, value=6.5, step=0.1)
years = st.slider("Loan Term (Years)", min_value=1, max_value=40, value=30)

# Calculate on button click
if st.button("Calculate Monthly Payment"):
    monthly = calculate_mortgage(principal, annual_rate, years)
    st.success(f"💰 Your Monthly Payment: **${monthly:,.2f}**")
