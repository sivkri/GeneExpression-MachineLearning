import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

# Load test data
df = pd.read_csv("data/processed_counts.csv", index_col=0)
X_test = df.values
y_test = np.array([0, 0, 1, 1, 2, 2, 3, 3])  # Labels

# Load models
logistic_model = joblib.load("results/logistic_model.pkl")
random_forest_model = joblib.load("results/random_forest_model.pkl")

# Predictions
logistic_preds = logistic_model.predict(X_test)
rf_preds = random_forest_model.predict(X_test)

# Function to save evaluation results
def save_results(name, y_true, y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    conf_matrix = confusion_matrix(y_true, y_pred)
    class_report = classification_report(y_true, y_pred)

    with open(f"results/{name}_report.txt", "w") as f:
        f.write(f"{name} Model Evaluation\n")
        f.write(f"Accuracy: {accuracy:.2f}\n")
        f.write("Confusion Matrix:\n")
        f.write(np.array2string(conf_matrix) + "\n")
        f.write("Classification Report:\n")
        f.write(class_report + "\n")

    plt.figure(figsize=(6, 4))
    sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=["WT-DMSO", "KO-DMSO", "WT-E20", "KO-E20"], yticklabels=["WT-DMSO", "KO-DMSO", "WT-E20", "KO-E20"])
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title(f"{name} Confusion Matrix")
    plt.savefig(f"results/{name}_confusion_matrix.png")
    plt.close()

# Evaluate and save results
save_results("Logistic_Regression", y_test, logistic_preds)
save_results("Random_Forest", y_test, rf_preds)
print("Evaluation complete. Reports saved in results/")
