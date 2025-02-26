# GeneExpression-MachineLearning
Supervised Machine Learning for Gene Expression Analysis
# Supervised Machine Learning for Gene Expression Analysis

This repository showcases the application of **Logistic Regression** and **Random Forest** for gene expression analysis. It automates data processing, model training, and evaluation.

## 🚀 Features
- **Preprocessing**: Formats gene expression data
- **Machine Learning**: Uses Logistic Regression & Random Forest
- **Evaluation**: Generates accuracy reports and confusion matrices
- **Automation**: Includes a shell script & GitHub Actions

## 📂 Repository Structure
```
📦 ml_gene_expression_project
 ┣ 📂 data               # Stores gene expression data
 ┣ 📂 results            # Model reports and images
 ┣ 📜 preprocess.py      # Data processing script
 ┣ 📜 train.py           # Model training
 ┣ 📜 evaluate.py        # Model evaluation with visualization
 ┣ 📜 run_pipeline.sh    # Shell script to execute the full pipeline
 ┣ 📜 run_pipeline.yml   # GitHub Actions workflow
 ┣ 📜 app.py             # Streamlit app for visualization
 ┣ 📜 README.md          # Project documentation
```

## 🏃 Run the Pipeline
```bash
bash run_pipeline.sh
```

## 🖼️ Sample Outputs
- Model Accuracy Reports in `results/`
- Confusion Matrices saved as images

## 🤖 GitHub Actions
This repository supports **automatic execution** when new data is pushed.

## 📌 How to Use
1. Clone the repository:  
   ```bash
   git clone https://github.com/sivkri/GeneExpression-MachineLearning.git
   ```
2. Navigate to the directory:  
   ```bash
   cd ml_gene_expression_project
   ```
3. Run the pipeline:  
   ```bash
   bash run_pipeline.sh
   ```

## 📧 Contact
For queries, feel free to reach out! 🚀
