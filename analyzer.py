import pandas as pd
import matplotlib.pyplot as plt

# Read ZMap results
df = pd.read_csv("scan_results.csv")

print("===== ZMAP SCAN RESULT ANALYZER =====")

# Find IP column
if "saddr" in df.columns:
    ip_column = "saddr"
else:
    ip_column = df.columns[0]

# Analysis
total_hosts = len(df)
unique_hosts = df[ip_column].nunique()

print("\nTotal Responsive Hosts:", total_hosts)
print("Unique IP Addresses:", unique_hosts)

print("\nResponsive Hosts:")
print(df[ip_column].to_string(index=False))

# Create graph
plt.figure(figsize=(8, 5))
plt.bar(["Responsive Hosts"], [unique_hosts])

plt.title("ZMap Scan Results")
plt.ylabel("Number of Hosts")

plt.savefig("report.png")

print("\nReport saved as report.png")
