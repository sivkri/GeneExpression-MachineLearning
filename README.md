# Supervised Learning for Gene Expression Analysis

This repository showcases the application of **Logistic Regression** and **Random Forest** for gene expression analysis. It automates data processing, model training, and evaluation.

## 🚀 Features
- **Preprocessing**: Formats gene expression data
- **Machine Learning**: Uses Logistic Regression & Random Forest
- **Evaluation**: Generates accuracy reports and confusion matrices
- **Automation**: Includes a shell script & GitHub Actions

## 📂 Repository Structure
```
📂 **ml_gene_expression_project**  
 ┣ 📂 **data/**               → Stores gene expression data  
 ┣ 📂 **results/**            → Model reports and visualizations  
 ┣ 📜 **preprocess.py**       → Data processing script  
 ┣ 📜 **train.py**            → Model training script  
 ┣ 📜 **evaluate.py**         → Model evaluation with visualization  
 ┣ 📜 **run_pipeline.sh**     → Shell script to automate pipeline execution  
 ┣ 📜 **run_pipeline.yml**    → GitHub Actions workflow  
 ┣ 📜 **app.py**              → Streamlit app for interactive visualization  
 ┣ 📜 **README.md**           → Project documentation  
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
   cd GeneExpression-MachineLearning
   ```
3. Run the pipeline:  
   ```bash
   bash run_pipeline.sh
   ```

## To launch the Streamlit app for interactive visualization:

   ```bash
   streamlit run app.py
   ```

### 🔥 Key Enhancements:  
✔ **Streamlit app is properly emphasized**  
✔ **Instructions for running the app are added**  
✔ **Clear explanation of app features**  

This version **sells** your **ML + Streamlit** project effectively. Let me know if you need further refinements! 🚀



## Results & Findings
- Identified top genes differentiating wild-type (WT) vs knockout (KO) conditions
- Evaluated the impact of Eltrombopag (E20) treatment
- Achieved 75% accuracy with the Random Forest classifier



# Project Overview  
This project applies **machine learning** techniques to analyze **gene expression data** under different experimental conditions. Using **logistic regression** and **random forest classifiers**, we identify genes differentially expressed due to **HuR knockout (ELAVL1 deletion)** and **Eltrombopag (E20) drug treatment**.

Additionally, a **Streamlit web application** is integrated to provide an **interactive visualization** of the results.  

## Citation  
If you use this dataset or findings, please cite the following study:  
📖 **DOI:** [10.1186/s12915-025-02131-z](https://doi.org/10.1186/s12915-025-02131-z)

---

## **Experimental Design**  

This study investigates how **HuR knockout (KO)** and **Eltrombopag (E20) treatment** influence gene expression compared to wild-type (WT) and mock treatment (DMSO).

### **Sample Groups**  
The dataset consists of the following experimental conditions:

| Sample Group | Description |
|-------------|-------------|
| **WT-DMSO** | Wild-type (WT) cells treated with mock (DMSO) |
| **WT-E20**  | Wild-type (WT) cells treated with Eltrombopag (E20) |
| **KO-DMSO** | HuR knockout (KO) cells treated with mock (DMSO) |
| **KO-E20**  | HuR knockout (KO) cells treated with Eltrombopag (E20) |

Each sample contains gene expression data across thousands of genes. **HuR (ELAVL1)** is a key **RNA-binding protein**, and its knockout may significantly alter gene expression. **Eltrombopag** is a thrombopoietin receptor agonist that may influence transcriptional programs.

---

## **Comparisons & Research Questions**  

I have performed **three key comparisons** using **supervised learning** to classify gene expression profiles.

### **1️⃣ Effect of HuR Knockout (KO vs. WT)**
- **Comparison:** **WT-DMSO vs. KO-DMSO**  
- **Objective:** Identify genes affected by HuR deletion.  
- **Machine Learning Approach:**  
  - Features: Gene expression levels  
  - Labels: WT-DMSO (class 0) vs. KO-DMSO (class 1)  

### **2️⃣ Effect of Eltrombopag in Wild-Type Cells**
- **Comparison:** **WT-DMSO vs. WT-E20**  
- **Objective:** Determine gene expression changes due to Eltrombopag in normal cells.  
- **Machine Learning Approach:**  
  - Features: Gene expression levels  
  - Labels: WT-DMSO (class 0) vs. WT-E20 (class 1)  

### **3️⃣ Effect of Eltrombopag in HuR Knockout Cells**
- **Comparison:** **KO-DMSO vs. KO-E20**  
- **Objective:** Understand the **HuR-dependent** response to Eltrombopag.  
- **Machine Learning Approach:**  
  - Features: Gene expression levels  
  - Labels: KO-DMSO (class 0) vs. KO-E20 (class 1)  

---

## **Data Processing & Machine Learning Workflow**  

1. **Preprocessing:**  
   - Normalize expression data  
   - Convert into a machine-learning-ready format  

2. **Model Training & Feature Selection:**  
   - Train **logistic regression** and **random forest** classifiers  
   - Perform **Principal Component Analysis (PCA)**  

3. **Evaluation:**  
   - Compute **accuracy, confusion matrices, classification reports**  
   - Identify **top differentially expressed genes**  

4. **Visualization & Reporting:**  
   - Generate **PCA scatter plots**  
   - Save **model performance metrics**  

---

## 📧 Contact
For queries, feel free to reach out! 🚀

---


