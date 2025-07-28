🧠 Weekly Prompts – Healthcare Tech Portfolio
This folder contains mini-projects developed as part of my Python + AI + Azure learning journey. Each challenge builds toward real-world healthcare or pharmacy operations use cases, applying Python, pandas, scikit-learn, API calls, and visualization.

💉 1. Smart Outreach Generator
An end-to-end Python mini-project that analyzes patient vaccination data, filters overdue cases, retrieves live vaccine information from the FDA, and outputs personalized summaries in both CSV and JSON formats.

🔧 Skills Demonstrated
✅ List & dictionary comprehensions

✅ Conditional logic & filtering

✅ Functions and reusable utilities

✅ Real-world API integration (requests)

✅ Pandas for CSV reading/writing

✅ JSON output generation

📁 Key Files
File	Description
smart_outreach_generator.py	Main Python script that runs the outreach workflow
smart_outreach_patients.csv	Input file containing mock patient data
filtered_overdue.csv	Output file with only patients who are overdue
outreach_summary.json	Enriched JSON summary with vaccine info from FDA

🔌 Example API Used
FDA Drug Label API — Only called once per unique vaccine.

🧬 2. No-Show Predictor & Risk Analyzer
A machine learning project that analyzes patient behavior data, flags high-risk patients, visualizes no-show patterns, and predicts future no-shows using a Decision Tree classifier.

🔧 Skills Demonstrated
✅ Conditional logic (apply, custom risk function)

✅ Pandas feature engineering

✅ Seaborn data visualization

✅ Label encoding with .astype("category").cat.codes

✅ Model training & testing with scikit-learn

✅ Accuracy measurement, predictions, confusion matrix

📁 Key Files
File	Description
predict_no_show_challenge.py	Full ML script: risk logic, visualization, model
patient_dataset.csv	Input dataset (age, insurance, chronic disease, etc.)
high_risk_patients.csv	Output of all patients flagged as "High Risk"
insurance_types_high_risk.png	Visualization of no-show rates by risk level

📊 Example Output
Prints predictions vs. actuals for first 10 patients

Model accuracy: ~0.55 (DecisionTreeClassifier)

Exports key plot for visual insight

⚙️ Requirements
Install once for both projects:

bash
Copy
Edit
pip install pandas seaborn scikit-learn requests matplotlib