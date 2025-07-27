import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix





# Load the data
df = pd.read_csv("patient_vaccine.csv")

# Show first 5 rows
print(df.head())

# Summary info (columns, data types, missing?)
print("\nSummary info:")
print(df.info())

# Stats for numeric columns
print("\nDescriptive statistics:")
print(df.describe())

# Define features (X) and label (y)
X = df[["age", "past_no_shows", "reminder_sent", "vaccines_due"]]
y = df["no_show_next"]

# Show the shape of both
print("🧩 Features shape:", X.shape)
print("🎯 Label shape:", y.shape)



# Split: 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Show result
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

print(f"✅ Model Accuracy: {accuracy:.2f}")

model = RandomForestClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy2 = accuracy_score(y_test, y_pred)
print(f"✅ Random Forest Model Accuracy: {accuracy2:.2f}")

cm = confusion_matrix(y_test, y_pred)
print(cm)


