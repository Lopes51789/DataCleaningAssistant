# Interactive Data Cleaning Assistant

## 📌 Overview
The **Interactive Data Cleaning Assistant** is an open-source tool designed to automate and streamline the data cleaning process, making it more efficient for **data analysts, data scientists, and business intelligence professionals**. It helps clean, preprocess, and validate datasets with minimal effort, saving valuable time while ensuring data integrity.

## 🚀 Features
### ✅ Data Import & Exploration
- Supports multiple formats: **CSV, Excel, JSON, Parquet, SQL databases**
- Automatic **data profiling**: summary statistics, missing values, data types
- Column-level insights with interactive visualizations

### 🔍 Handling Missing Data
- Automatic detection of missing values
- Suggested imputation techniques:
  - Mean/median/mode imputation
  - Forward-fill / backward-fill
  - Predictive imputation (using ML models)
- Option to remove rows/columns with excessive missing values

### 📝 Detecting & Handling Duplicates
- Identifies **exact** and **near-duplicate** rows
- Rule-based duplicate filtering
- Customizable merging strategies

### 🎨 Data Standardization
- Automatic formatting of:
  - Dates & timestamps
  - Categorical values (e.g., standardizing ‘USA’, ‘U.S.’, ‘United States’)
  - Numerical values (e.g., converting currency formats)
- String normalization (removing special characters, extra spaces)
- Casing standardization (lowercase, uppercase, title case)

### 📊 Outlier Detection & Handling
- Detects outliers using:
  - **IQR (Interquartile Range)**
  - **Z-score & standard deviation-based methods**
  - **Machine learning-based anomaly detection**
- Suggested actions: remove, cap, or replace outliers

### ⚙️ Interactive Rule-Based Cleaning
- Define and apply custom cleaning rules
- Example: "Replace all negative values in column X with 0"
- Save and reuse cleaning pipelines

### ✅ Data Validation & Quality Checks
- Consistency checks (e.g., valid email formats)
- Business logic validation (e.g., future dates should be flagged)
- Alerts for potential issues with suggested fixes

### 📤 Export & Integration
- Export cleaned data to **CSV, Excel, SQL databases, JSON**
- Integration with **Python scripts, Jupyter Notebooks, and BI tools**
- Generates a **cleaning report** summarizing applied transformations

## 🛠️ Tech Stack
- **Backend:** Python (**pandas**, **NumPy**, **scikit-learn**, **FastAPI** for APIs)
- **Frontend:** Streamlit / Dash (for interactive UI)
- **Database Support:** SQLite, PostgreSQL, MongoDB
- **ML Integration:** scikit-learn (for predictive imputation & anomaly detection)
- **Deployment:** Docker, AWS/GCP/Azure

## 🔧 Installation
```bash
git clone https://github.com/Lopes51789/DataCleaningAssistant.git
cd DataCleaningAssistant
pip install -r requirements.txt
```

## ▶️ Usage
```python
```

## 🛠️ Contributing
We welcome contributions! 🚀 If you'd like to improve the project:
1. Fork the repo
2. Create a new branch (`feature-xyz`)
3. Commit your changes
4. Push the branch and submit a PR

## 📄 License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 📢 Get Involved
Want to collaborate? Send me a DM or check out the GitHub repo! 🚀

🔗 **GitHub Repo:** [Data Cleaning Assistant](https://github.com/Lopes51789/DataCleaningAssistant)
