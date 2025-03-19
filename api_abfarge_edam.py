import requests
import json

# Ersetze hier durch deine echten Zugangsdaten
app_id = ""
app_key = ""
user_id = ""
url = f"https://api.edamam.com/api/recipes/v2?app_id={app_id}&app_key={app_key}"

# Beispiel-Payload: Ein Rezept mit Titel und Zutatenliste
payload = {
    "title": "Chicken Vesuvio",
    "ingr": [
        "1/2 cup olive oil",
        "5 cloves garlic",
        "2 large russet potatoes, peeled and cut into chunks",
        "1 3-4 pound chicken, cut into 8 pieces (or 3 pound chicken legs)",
        "3/4 cup white wine",
        "3/4 cup chicken stock",
        "3 tablespoons chopped parsley"
    ]
}

# Header anpassen und die UserID hinzufügen
headers = {
    "Content-Type": "application/json",
    "Edamam-Account-User": ""
}

# Sende die POST-Anfrage
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Prüfe, ob die Anfrage erfolgreich war
if response.status_code == 200:
    result = response.json()
    print("API-Antwort:")
    print(json.dumps(result, indent=2))
else:
    print("Fehler bei der API-Abfrage:")
    print("Status Code:", response.status_code)
    print("Antwort:", response.text)
