# Smart Outreach Generator for Python Learning Recap – Includes list/dict comprehensions, filters, conditionals, APIs, pandas, JSON. See README for project details.

import requests         #importing requests for API calls, pandas for data manipulation, and json for handling JSON data
import pandas as pd
import json

patients_df= pd.read_csv("smart_outreach_patients.csv")  #reading a CSV file containing patient data
print(patients_df.head())  #displaying the first few rows of the DataFrame
print("CSV file loaded successfully")  #confirming successful loading of the CSV file

def age_group(age):    #reusuable function to classify patients into age groups
    """Classify patients into age groups."""
    return "Senior" if age >= 60 else "Young"
def label_patient(p, vaccine_info_lookup): #function to label each patient with their name, age, status, age group, vaccine, and vaccine information
    """Label patient with their details and vaccine info."""
    return {
        "name": p["Name"],
        "age": p["Age"],
        "status": "Due" if p["Status"] == "no" else "Done",
        "age_group": age_group(p["Age"]),
        "vaccine": p["Vaccine"],
        "vaccine_info": vaccine_info_lookup.get(p["Vaccine"].lower(), "No info available.")
    }
def get_vaccine_info(vaccine_name): #function to fetch vaccine information from the FDA API
    try:
        url = f"https://api.fda.gov/drug/label.json?search={vaccine_name.lower()}&limit=1"
        response = requests.get(url)
        data = response.json()
        info = data["results"][0]["description"][0]
        return info[:200] + "..."  # Return a short preview
    except Exception as e:
        print(f"Error fetching info for {vaccine_name}: {e}")
        return "No info available."

def main():
    print("Starting smart outreach generator...")  #confirming the start of the smart outreach generator
    overdue_df = patients_df[patients_df["Status"] == "No"]  #filtering for overdue patients with status "No"

    unique_vaccines = overdue_df["Vaccine"].str.lower().unique() #creating a set of unique vaccine names from the overdue patients DataFrame
    vaccine_info_lookup = {v: get_vaccine_info(v) for v in unique_vaccines} #creating a dictionary to store vaccine information for each unique vaccine
    print("Vaccine information fetched successfully")  #confirming successful fetching of vaccine information

    outreach_list = [label_patient(row, vaccine_info_lookup) for _, row in overdue_df.iterrows()]
    print("Outreach list generated successfully")  #confirming successful generation of the outreach list

    overdue_df.to_csv("filtered_overdue.csv", index=False)
    print("Filtered overdue patients saved to filtered_overdue.csv")  #confirming successful saving of the filtered DataFrame

    with open("outreach_summary.json", "w") as f:
        json.dump(outreach_list, f, indent=2)

    print("\n📦 Outreach Summary")
    print(f"👥 Total patients contacted: {len(outreach_list)}")
    print(f"💉 Vaccines included: {', '.join(list(vaccine_info_lookup.keys()))}")
    print("📂 Files generated:")
    print("- filtered_overdue.csv")
    print("- outreach_summary.json")
    print("Smart outreach generator completed successfully")  #confirming successful completion of the smart outreach generator

if __name__ == "__main__":
    main()  #calling the main function to execute the smart outreach generator
    print("Smart outreach generator script executed successfully")  #confirming successful execution of the script