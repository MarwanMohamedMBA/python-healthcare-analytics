import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("patient_dataset.csv")
print(df.head())  # Display the first few rows of the DataFrame
print("CSV file loaded successfully")  # Confirm successful loading of the CSV file
print(df.columns)
print(df.isnull().sum())

def highrisk(row):
    if row["age"] >= 65 and row["chronic_disease"] == 1 and row["no_show_last"] > 0:
        return "High Risk"
    else:
        return "Low Risk"

highrisk_df = df[df.apply(highrisk, axis=1) == "High Risk"]
print("High risk patients identified successfully")  # Confirm successful identification of high-risk patients
df["Risk Level"] = df.apply(highrisk, axis=1)

plt.figure(figsize=(8, 5))
sns.barplot(x="Risk Level",y= "no_show_next", data=df)
plt.title("No-Show Rate by Risk Level")
plt.tight_layout()  # Auto-fix spacing between plots
plt.show()  # Display the plot

df["Insurance_Code"] = df["insurance"].astype("category").cat.codes
print(df[["insurance", "Insurance_Code"]].drop_duplicates())

X = df[["age", "Insurance_Code", "chronic_disease", "no_show_last"]]
y = df["no_show_next"]

print("🧩 Features shape:", X.shape)
print("🎯 Label shape:", y.shape)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

print("✅ Training features shape:", X_train.shape)
print("✅ Testing features shape:", X_test.shape)

model = DecisionTreeClassifier()
# 2. Train the model using training data
model.fit(X_train, y_train)
print("✅ Model trained successfully")  # Confirm successful training of the model

# 3. Make predictions on the test set
y_pred = model.predict(X_test)
print("✅ Predictions made successfully")  # Confirm successful predictions

accuracy_score = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy_score:.2f}")  # Display the accuracy of the model
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)  # Display the confusion matrix

for i in range(10):
    print(f"Predicted: {y_pred[i]}, Actual: {y_test.values[i]}")
print("✅ Predictions compared to actual values")  # Confirm successful comparison of predictions to actual values


unique_meds = df["medication"].unique()

def get_med_description(med_name):
    url = f"https://api.fda.gov/drug/label.json?search={med_name}&limit=1"
    try:
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            return data["results"][0]["description"][0]
        else:
            return "No description available"
    except:
        return "No info found"

med_info_dict = {med: get_med_description(med) for med in unique_meds}
df["medication_info"] = df["medication"].map(med_info_dict)

highrisk_df = df[df["Risk Level"] == "High Risk"]

summary = []

for _, row in highrisk_df.iterrows():
    summary.append({
        "name": "Patient",  # Placeholder
        "age": row["age"],
        "risk_level": row["Risk Level"],
        "medication": row["medication"],
        "medication_info": row["medication_info"]
    })

# Save to JSON file
import json

with open("high_risk_summary.json", "w") as f:
    json.dump(summary, f, indent=2)

print("✅ Saved high-risk JSON summary to high_risk_summary.json")
