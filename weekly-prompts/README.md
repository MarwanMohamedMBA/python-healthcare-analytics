# 💉 Smart Outreach Generator

An end-to-end Python mini-project that analyzes patient vaccination data, filters overdue cases, retrieves live vaccine information from the FDA, and outputs personalized summaries in both CSV and JSON formats.

This project demonstrates key Python skills including:

- ✅ List & dictionary comprehensions
- ✅ Conditional logic & filtering
- ✅ Functions and reusable utilities
- ✅ Real-world API integration (`requests`)
- ✅ Pandas for CSV reading/writing
- ✅ JSON output generation

---

## 📁 Files

| File | Description |
|------|-------------|
| `smart_outreach_generator.py` | Main Python script that runs the outreach workflow |
| `smart_outreach_patients.csv` | Input file containing mock patient data |
| `filtered_overdue.csv` | Output file with only patients who are overdue |
| `outreach_summary.json` | Enriched JSON summary with vaccine info from FDA |
| `README.md` | Project documentation (this file)

---

## 🧠 How It Works

1. **Reads patient data** from `smart_outreach_patients.csv` using `pandas`
2. **Filters for overdue patients** based on `"Status" == "No"`
3. **Extracts unique vaccine types** and calls the **FDA Drug Label API** to get real descriptions
4. **Builds labeled outreach summaries** using list/dict comprehensions
5. **Exports two outputs:**
   - 📄 `filtered_overdue.csv` — raw overdue data
   - 🧾 `outreach_summary.json` — patient summaries + API vaccine descriptions

---

## 🔌 Example API Used

FDA Drug Label API: https://api.fda.gov/drug/label.json?search={vaccine_name}&limit=1

You only call the API **once per vaccine**, not per patient.

---

## 🛠️ Requirements

- Python 3.9+
- `pandas`
- `requests`

Install via:

```bash
pip install pandas requests

🧪 Sample Output (JSON)
json
Copy
Edit
{
  "name": "Amy",
  "age": 67,
  "status": "Due",
  "age_group": "Senior",
  "vaccine": "Flu",
  "vaccine_info": "This vaccine is indicated for seasonal flu prevention in adults and children. Dosage..."
}

