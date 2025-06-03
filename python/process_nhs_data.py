import pandas as pd
import os

# Load data
df = pd.read_csv(os.path.join("raw", "nhs_prescriptions.csv"))

# Group by region and BNF chapter to get total cost
summary = df.groupby(["REGION_NAME", "BNF_CHAPTER"])["NIC"].sum().reset_index()

# Save the summary
output_path = os.path.join("processed", "prescription_summary.csv")
summary.to_csv(output_path, index=False)

print(f" Processed data saved to: {output_path}")

