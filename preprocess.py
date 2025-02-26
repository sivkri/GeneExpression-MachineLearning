import pandas as pd

# Load dataset
df = pd.read_csv("data/raw_counts.txt", sep="\t", index_col=0)

# Transpose for ML models (samples as rows, genes as columns)
df = df.T

# Save processed data
df.to_csv("data/processed_counts.csv")
print("Data preprocessing complete. Saved as data/processed_counts.csv.")
