import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Large_Patient_Vaccine_Dataset.csv')

overdue_by_store = df.groupby("Store_Location")["Overdue"].sum().reset_index()
imz_by_store = df.groupby("Store_Location")["Immunizations_This_Year"].sum().reset_index()
overdue_percent = df.groupby("Store_Location").agg(
    total_patients=("Overdue", "count"),
    overdue_patients=("Overdue", "sum")
).reset_index()
overdue_percent["Overdue_Percent"] = (overdue_percent["overdue_patients"] / overdue_percent["total_patients"]) * 100



# Create 1 row, 2 columns for our charts
fig, axes = plt.subplots(2, 2, figsize=(16, 6))  # 2 row x 2 columns
# Chart 1: Overdue patients by store
sns.barplot(data=overdue_by_store, x="Store_Location", y="Overdue", ax=axes[0,0], palette="Reds_r", hue=None, legend=False)
axes[0,0].set_title("Overdue Patients by Store")
axes[0,0].set_xlabel("Store")
axes[0,0].set_ylabel("Overdue Count")
axes[0,0].tick_params(axis='x', rotation=45)
# Chart 2: Total immunizations by store
sns.barplot(data=imz_by_store, x="Store_Location", y="Immunizations_This_Year", ax=axes[0,1], palette="Greens_r", hue=None, legend=False)
axes[0,1].set_title("Total Immunizations by Store")
axes[0,1].set_xlabel("Store")
axes[0,1].set_ylabel("Immunizations")
axes[0,1].tick_params(axis='x', rotation=45)
#chart 3: percentage of overdue patients by store
sns.barplot(data= overdue_percent, x="Store_Location", y= "Overdue_Percent",ax=axes[1,0], palette="Blues_r", hue=None, legend=False)
axes[1,0].set_title("Percentage of Overdue Vaccine Patients by Store Location")
axes[1,0].set_xlabel("Store Location")
axes[1,0].set_ylabel("Percent of Overdue Patients")
axes[1,0].tick_params(axis='x' ,rotation=45)
#chart 4: Boxplot of age by store
sns.boxplot(data=df, x="Store_Location", y="Age", ax=axes[1,1], palette="pastel", hue=None, legend=False)
axes[1,1].set_title("Age Distribution by Store Location")
axes[1,1].set_xlabel("Store Location")
axes[1,1].set_ylabel("Age")
axes[1,1].tick_params(axis='x')
axes[1,1].tick_params(rotation=45)
#saving the dashoboard
plt.tight_layout()  # Auto-fix spacing between plots
plt.savefig("dashboard_side_by_side.png")
plt.show()  # Show the combined dashboard

input("Press Enter to exit...")
