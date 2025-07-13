import pandas as pd

patients_df = pd.read_csv("mock_patient_data.csv")
print(patients_df.head())
#listing preview for mock_patient_data.csv

overdue_df = patients_df[patients_df["Status"] == "No"]
print("Overdue Patients\n", overdue_df)
#filtering for overdue patients with status "No"

overdue_seniors_df = patients_df[(patients_df["Age"] >= 60) & (patients_df["Status"] == "No")]
print("Overdue Seniors\n", overdue_seniors_df)
#filtering for overdue seniors with age >= 60 and status "No"
patients_df.rename(columns={"Status": "Vaccine Status"}, inplace=True)
print("Renamed Status to Vaccine Status\n", patients_df.columns)
#renaming the "Status" column to "Vaccine Status"

overdue_seniors_df.to_csv("senior_overdue.csv", index=False)
print("File saved as senior_overdue.csv")