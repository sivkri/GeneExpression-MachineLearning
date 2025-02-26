import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load preprocessed dataset
df = pd.read_csv("data/processed_counts.csv", index_col=0)
X = df.values
y = np.array([0, 0, 1, 1, 2, 2, 3, 3])  # Labels

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.5, random_state=42, stratify=y)

# Train models
logistic_model = LogisticRegression(max_iter=1000, multi_class="multinomial", solver="lbfgs")
random_forest_model = RandomForestClassifier(n_estimators=100, random_state=42)

logistic_model.fit(X_train, y_train)
random_forest_model.fit(X_train, y_train)

# Save models
joblib.dump(logistic_model, "results/logistic_model.pkl")
joblib.dump(random_forest_model, "results/random_forest_model.pkl")
print("Training complete. Models saved in results/")
