#"""
#📅 Date: July 9, 2025
#📁 Repo: python-healthcare-analytics
#🎯 Lesson: Real-World API Practice with Healthcare Data (FDA Drug Label Lookup)
#""""
import requests
print(requests.__version__)


def fetch_drug_info(drug_name):
    url = "https://api.fda.gov/drug/label.json"
    params = { 'search': drug_name.lower(), 'limit': 1 }
    try:
        response = requests.get(url, params=params)
        print("📡 API URL Used:", response.url)
        if response.status_code == 200:
            data = response.json()
            if 'results' in data:
                result = data['results'][0]
                
                brand = result.get('openfda', {}).get('brand_name', ['Unknown'])[0]
                manufacturer = result.get('openfda', {}).get('manufacturer_name', ['Unknown'])[0]
                usage = result.get('indications_and_usage', ['Not available'])[0]

                print("\n📋 Drug Information:")
                print(f"🔹 Brand Name: {brand}")
                print(f"🏢 Manufacturer: {manufacturer}")
                print(f"💊 Indications & Usage:\n{usage[:500]}{'...' if len(usage) > 500 else ''}")
            else:
                print("❗ No results found for that drug.")
        else:
            print(f"🚨 API request failed with status code {response.status_code}")
    except Exception as e:
        print("❌ An unexpected error occurred:", e)

def show_menu():
    while True:
        print("\n📋 What would you like to do?")
        print("1. Look up a single drug or vaccine")
        print("2. Look up multiple drugs")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            drug = input("Enter a drug or vaccine name: ").strip()
            fetch_drug_info(drug)
        elif choice == "2":
            drugs = input("Enter names separated by commas (e.g., flu, covid, ibuprofen): ").split(',')
            for drug in drugs:
                fetch_drug_info(drug.strip())
        elif choice == "3":
            print("👋 Exiting. Stay healthy!")
            break
        else:
            print("⚠️ Invalid choice. Please enter 1, 2, or 3.")



if __name__ == "__main__":
    show_menu()
    drugs = input("Enter drug names separated by commas: ").split(',')
    for drug in drugs:
        fetch_drug_info(drug.strip())
