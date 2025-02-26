import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Streamlit app title
st.title("Gene Expression Analysis App")

# File uploader
uploaded_file = st.file_uploader("Upload Gene Expression Data (CSV or TXT)", type=["csv", "txt"])

if uploaded_file is not None:
    # Load dataset
    count_data = pd.read_csv(uploaded_file, sep="\t", index_col=0)
    st.write("### Preview of Data:")
    st.write(count_data.head())

    # Transpose and scale the data
    X = count_data.T.values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # PCA
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    # Define sample labels (Modify as needed)
    labels = ["WT-DMSO", "KO-DMSO", "WT-E20", "KO-E20"] * (X.shape[0] // 4)

    # PCA Plot
    fig, ax = plt.subplots()
    sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=labels, palette='viridis', ax=ax)
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.title("PCA of Gene Expression Data")
    st.pyplot(fig)

    # Model training
    y = np.array([0, 0, 1, 1, 2, 2, 3, 3])  # Modify labels accordingly
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.5, random_state=42, stratify=y)

    # Logistic Regression
    log_model = LogisticRegression()
    log_model.fit(X_train, y_train)
    y_pred_log = log_model.predict(X_test)

    # Random Forest
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    y_pred_rf = rf_model.predict(X_test)

    # Model Results
    st.write("## Model Evaluation")
    st.write("### Logistic Regression")
    st.write("Accuracy:", accuracy_score(y_test, y_pred_log))
    st.write("Confusion Matrix:")
    st.write(confusion_matrix(y_test, y_pred_log))
    st.write("Classification Report:")
    st.text(classification_report(y_test, y_pred_log))

    st.write("### Random Forest")
    st.write("Accuracy:", accuracy_score(y_test, y_pred_rf))
    st.write("Confusion Matrix:")
    st.write(confusion_matrix(y_test, y_pred_rf))
    st.write("Classification Report:")
    st.text(classification_report(y_test, y_pred_rf))
