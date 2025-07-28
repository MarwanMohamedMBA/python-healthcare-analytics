import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


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
highrisk_df.to_csv("high_risk_patients.csv", index=False)
print("High risk patients saved to high_risk_patients.csv")  # Confirm successful saving of the high-risk patients DataFrame
highrisk_count = len(highrisk_df)
df["Risk Level"] = df.apply(highrisk, axis=1)

plt.figure(figsize=(8, 5))
sns.barplot(x="Risk Level", y="no_show_next", data=df)
plt.title("No-Show Rate by Risk Level")
plt.tight_layout()  # Auto-fix spacing between plots
plt.savefig("insurance_types_high_risk.png")

input("Press Enter to continue...")

df["Insurance_Code"] = df["insurance"].astype("category").cat.codes
print(df[["insurance", "Insurance_Code"]].drop_duplicates())


X = df[["age", "Insurance_Code", "chronic_disease", "no_show_last"]]
y = df["no_show_next"]

# Show the shape of both
print("🧩 Features shape:", X.shape)
print("🎯 Label shape:", y.shape)

# Split: 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print("✅ Training features shape:", X_train.shape)
print("✅ Testing features shape:", X_test.shape)

# 1. Create the model (an empty decision tree)
model = DecisionTreeClassifier()

# 2. Train the model using training data
model.fit(X_train, y_train)

# 3. Make predictions using test data
y_pred = model.predict(X_test)

# Compare predicted values (y_pred) to true values (y_test)
accuracy = accuracy_score(y_test, y_pred)
#print(f"✅ Model Accuracy: {accuracy:.2f}")

cm = confusion_matrix(y_test, y_pred)


for i in range(10):
    print(f"Predicted: {y_pred[i]}, Actual: {y_test.values[i]}")

def print_summary():
    print("\nSummary of the analysis:")
    print(f"Total patients in dataset: {len(df)}")
    print(f"Bar plot of insurance types saved as 'insurance_types_high_risk.png'")
    print(f"High risk patients identified: {highrisk_count}")
    print(f"Model accuracy: {accuracy:.2f}")
    print(f"Top 5 predictions: {y_pred[:5]}")
    print(f"Confusion Matrix:\n{cm}")
    plt.show()  # Show the plot


print_summary()
