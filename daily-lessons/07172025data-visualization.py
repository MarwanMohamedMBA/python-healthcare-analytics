import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


patient_data = pd.read_csv('Large_Patient_Vaccine_Dataset.csv')

overdue_by_store = patient_data.groupby("Store_Location")["Overdue"].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(data=overdue_by_store, x="Store_Location", y="Overdue", palette="Reds_r", hue=None, legend=False)
plt.title("Overdue Vaccine Patients by Store Location")
plt.xlabel("Store Location")
plt.ylabel("Number of Overdue Patients")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
input("Press Enter to continue...")

# This code visualizes the number of overdue vaccine patients by store location using a bar plot.
# It groups the data by store location, sums the overdue counts, and then plots the results using seaborn and matplotlib.
# The x-axis represents different store locations, while the y-axis shows


# Group by store and calculate total and overdue counts
store_summary = patient_data.groupby("Store_Location").agg(
    total_patients=("Overdue", "count"),
    overdue_patients=("Overdue", "sum")
).reset_index()

# Calculate percent overdue
store_summary["Overdue_Percent"] = (store_summary["overdue_patients"] / store_summary["total_patients"]) * 100
plt.figure(figsize=(12, 6))
sns.barplot(data= store_summary, x="Store_Location", y= "Overdue_Percent", palette="Blues_r", hue=None, legend=False)
plt.title("Percentage of Overdue Vaccine Patients by Store Location")
plt.xlabel("Store Location")
plt.ylabel("Percent of Overdue Patients")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
input("Press Enter to continue...")


#Total IMZ per store

IMZperstore = patient_data.groupby("Store_Location")["Immunizations_This_Year"].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(data=IMZperstore, x="Store_Location", y="Immunizations_This_Year", palette="Greens_r", hue=None, legend=False)
plt.title("Total Immunizations by Store Location")
plt.xlabel("Store Location")
plt.ylabel("Total Immunizations This Year")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
input("Press Enter to continue...")



#Boxplot of age by store, no grouping needed for this seaborn plot

plt.figure(figsize=(12, 6))
sns.boxplot(data=patient_data, x="Store_Location", y="Age", palette="pastel", hue=None, legend=False)
plt.title("Patient Age Distribution by Store")
plt.xlabel("Store Location")
plt.ylabel("Age")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
input("Press Enter to quit...")



