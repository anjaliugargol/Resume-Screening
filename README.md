# 🤖 AI-Powered Resume Screening for HR Systems

---

## 📌 Project Objective

Analyze incoming job applications using AI-driven scoring techniques to identify and shortlist the most suitable candidates efficiently.

---

## 🧠 Problem Statement

Recruiters receive thousands of job applications for a single role.  
Manual screening is time-consuming, inconsistent, and subjective.

This project applies data analytics and machine learning techniques to:

- Analyze candidate attributes  
- Identify hiring patterns  
- Predict recruiter decisions  
- Improve shortlisting efficiency through automation  

---

## 📊 Dataset Description

The dataset contains structured resume information including:

- Resume_ID  
- Name  
- Skills  
- Experience (Years)  
- Education  
- Certifications  
- Job Role  
- Recruiter Decision  
- Salary Expectation ($)  
- Projects Count  
- AI Score (0-100)  

Total Records: 1000+

---

## 🛠 Tools & Technologies Used

- Python (Pandas, NumPy)  
- Matplotlib & Seaborn  
- Scikit-learn  
- MySQL  
- Power BI  

---

## 🔎 Step 1: Data Cleaning

- Handled missing certification values  
- Encoded Recruiter Decision (Reject = 0, Hire = 1)  
- Verified null values  
- Exported cleaned dataset for modeling and database storage  

---

## 📈 Step 2: Exploratory Data Analysis (EDA)

Performed:

- AI Score distribution analysis  
- Experience vs AI Score relationship study  
- Projects count comparison  
- Correlation heatmap between numerical features  
- Recruiter decision distribution analysis  

---

## 🤖 Step 3: Predictive Modeling

### 📈 Linear Regression

Target Variable:  
AI Score (0-100)

Objective:  
Predict AI Score using candidate features such as experience, project count, and salary expectation.

Evaluation Metrics:
- Mean Squared Error (MSE)  
- R² Score  

Business Value:  
Helps understand which candidate attributes influence AI-based scoring.

---

### 📊 Logistic Regression

Target Variable:  
Recruiter_Decision_Encoded (0 = Reject, 1 = Hire)

Objective:  
Predict hiring decision based on candidate features.

Evaluation Metrics:
- Accuracy  
- Confusion Matrix  
- Classification Report  
- ROC Curve  

Business Value:  
Enables automated candidate shortlisting and improves recruitment efficiency.

---

## 🗄 Step 4: Database Integration

- Designed MySQL database schema  
- Created Resume database  
- Inserted cleaned dataset into MySQL  
- Executed analytical SQL queries to evaluate hiring trends and role-based selection rates  

---

## 📊 Step 5: Power BI Dashboard

Developed an interactive dashboard to visualize:

- Hiring vs Rejection trends  
- AI Score comparison  
- Experience distribution  
- Salary expectation insights  
- Role-based candidate analysis  

Dashboard File Location:  
`/dashboard/resume_powerbi.pbix`

---

## 📌 Key Business Insights

- Higher AI scores significantly increase hiring probability.  
- Experience and project count positively influence AI Score as validated by Linear Regression.  
- Candidates with higher experience and more projects show stronger selection rates.  
- Salary expectations influence recruiter shortlisting decisions.  
- Predictive modeling enables automated and data-driven resume screening.  

---

## 🚀 Future Enhancements

- NLP-based resume parsing  
- Skill matching using machine learning embeddings  
- Real-time recruitment dashboard integration  
- Model deployment as REST API  

---

## 📂 Project Structure

AI-Resume-Screening-Analytics/  
│  
├── data/  
├── notebooks/  
├── database/  
├── dashboard/  
├── requirements.txt  
└── README.md  

---

## ▶ How to Run the Project

1. Clone the repository  
2. Install required libraries:

   pip install -r requirements.txt  

3. Open notebooks/Resume_Screening_Analysis.ipynb  
4. Run all cells  

---

## 🎯 Project Outcome

This project demonstrates an end-to-end data analytics workflow including:

- Data Cleaning  
- Exploratory Data Analysis  
- Regression & Classification Modeling  
- Database Integration  
- Interactive Business Dashboard  

The system enables intelligent, data-driven resume screening for HR departments.
