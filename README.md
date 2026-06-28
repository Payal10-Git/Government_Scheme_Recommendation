# 🇮🇳 Government Scheme Recommendation System

An AI-powered Government Scheme Recommendation System that recommends the most suitable Central and State Government schemes to citizens based on their personal profile, eligibility, and requirements.

The project combines **Data Cleaning, Exploratory Data Analysis (EDA), Feature Engineering, Natural Language Processing (TF-IDF), Cosine Similarity, and Rule-Based Eligibility Filtering** to provide personalized scheme recommendations.

---

# 📌 Features

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Hybrid Recommendation System
- Eligibility-based Filtering
- TF-IDF Vectorization
- Cosine Similarity Matching
- Scheme Ranking using Weighted Score
- Personalized Scheme Recommendations
- Model Evaluation
- CSV Report Generation

---

# 📂 Project Structure

```
Government_Scheme_Recommendation/

├── notebooks/
│   ├── Data_Cleaning.ipynb
│   ├── EDA.ipynb
│   ├── Feature_Engineering.ipynb
│   ├── Recommendation_System.ipynb
│   └── Model_Evaluation.ipynb
│
├── ML_model/
│   ├── tfidf_vectorizer.pkl
│   └── tfidf_matrix.pkl
│
├── src/
│   ├── preprocessing.py
│   ├── eda_utils.py
│   ├── feature_engineering.py
│   
│
├── README.md

```

---

# 📊 Dataset

The dataset contains information about various Government Schemes available across India.

### Dataset includes

- Scheme Name
- Ministry
- Department
- State/UT
- Category
- Beneficiary Type
- Gender
- Occupation
- Age Limit
- Income Criteria
- BPL Eligibility
- Minority Eligibility
- Disability Eligibility
- Marital Status
- Documents Required
- Key Benefits
- Description
- Official Website
- Application Mode
- Interest Rate
- Repayment Period
- Scheme Level
- Tags

---

# 🧹 Phase 1 : Data Cleaning

The following preprocessing steps were performed:

- Removed unwanted columns
- Standardized column names
- Cleaned text columns
- Removed duplicate records
- Converted numeric columns
- Filled missing values
- Cleaned URLs
- Standardized gender values
- Standardized ministry names
- Standardized state names

Output:

```
cleaned_dataset1.csv
```

---

# 📈 Phase 2 : Exploratory Data Analysis

EDA includes

- Dataset Overview
- Missing Value Analysis
- Duplicate Analysis
- Numerical Feature Analysis
- Categorical Feature Analysis
- Correlation Matrix
- Histogram
- Boxplots
- Ministry-wise Analysis
- Department-wise Analysis
- State-wise Analysis
- Scheme Category Analysis
- Gender Distribution
- Occupation Distribution
- Application Mode Analysis
- Interest Rate Distribution
- Repayment Period Analysis
- Description Length Analysis

Generated graphs are stored inside

```
reports/graphs/
```

---

# ⚙ Phase 3 : Feature Engineering

Generated features include

- recommendation_text
- combined_text
- eligible_age
- scheme_name_length
- description_length
- beneficiary_count
- document_count
- tag_count
- benefit_length
- government_level

Output

```
feature_engineered_dataset.csv
```

---

# 🤖 Phase 4 : Recommendation System

The recommendation engine uses a hybrid approach.

### Step 1

User Profile Input

Example

```
Age
Gender
State
Occupation
Category
Income
BPL
Minority
Differently Abled
Marital Status
```

### Step 2

Eligibility Filtering

Checks

- Age
- Gender
- State
- Occupation
- Category
- BPL
- Minority
- Disability

### Step 3

Text Vectorization

TF-IDF Vectorizer converts scheme descriptions into numerical vectors.

### Step 4

Cosine Similarity

Measures similarity between

User Query

and

Government Scheme Information

### Step 5

Weighted Scoring

Final Score is calculated using

```
Final Score

=

70% Eligibility Score

+

30% Cosine Similarity Score
```

### Step 6

Ranking

Top matching schemes are returned.

Output

```
recommended_schemes.csv
```

---

# 📊 Phase 5 : Model Evaluation

Evaluation includes

- Recommendation Statistics
- Precision@10
- Recall
- F1 Score
- Recommendation Quality Distribution
- Recommendation Score Distribution
- Best Recommendation
- Worst Recommendation

Output

```
reports/model_evaluation.csv
```

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Joblib
- Jupyter Notebook

---

# 📦 Installation

Clone repository

```bash
git clone https://github.com/yourusername/Government_Scheme_Recommendation.git
```

Move into project

```bash
cd Government_Scheme_Recommendation
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

Run notebooks in the following order

```
1. Data_Cleaning.ipynb

2. EDA.ipynb

3. Feature_Engineering.ipynb

4. Recommendation_System.ipynb

5. Model_Evaluation.ipynb
```

---

# 📌 Recommendation Workflow

```
Government Scheme Dataset
            │
            ▼
     Data Cleaning
            │
            ▼
 Exploratory Data Analysis
            │
            ▼
  Feature Engineering
            │
            ▼
     TF-IDF Vectorization
            │
            ▼
     Eligibility Filtering
            │
            ▼
    Cosine Similarity
            │
            ▼
     Weighted Ranking
            │
            ▼
Top Recommended Government Schemes
```

---

# 📈 Future Improvements

- Web Application using Flask
- User Authentication
- Real-time Government Scheme Updates
- Large Language Model (LLM) Integration
- Voice-based Scheme Search
- Multilingual Recommendation System
- PDF Eligibility Report Generation
- Chatbot Integration
- Explainable AI Recommendations

