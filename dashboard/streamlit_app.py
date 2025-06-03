import pandas as pd
import streamlit as st

# Load processed data
df = pd.read_csv("../processed/prescription_summary.csv")

st.title("💊 NHS Prescription Summary (By Region & Chapter)")

st.markdown("View total NIC (cost) by region and BNF chapter.")

# Filters
region = st.selectbox("Select Region", df["REGION_NAME"].unique())
filtered = df[df["REGION_NAME"] == region]

# Display results
st.dataframe(filtered.sort_values("NIC", ascending=False))

st.bar_chart(filtered.set_index("BNF_CHAPTER")["NIC"])

