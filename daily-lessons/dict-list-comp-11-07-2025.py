patients = [
    {"name": "Amy", "age": 67, "status": "No"},
    {"name": "Ben", "age": 55, "status": "Yes"},
    {"name": "Cara", "age": 72, "status": "No"},
    {"name": "Dan", "age": 45, "status": "Yes"}
]

due = [p["name"] for p in patients if p["status"] == "No"]
print ("Overdue patients", due)

age_group = {p["name"]: "Senior" if p["age"] >= 60 else "Young" for p in patients}
print("Age groups", age_group)


seniors_overdue = {p["name"] for p in patients if p["age"] >= 60 and p["status"] == "No"}
print ("Seniors overdue", seniors_overdue) 