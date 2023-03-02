import requests
import access_token

at = access_token.at


url = "https://www.zohoapis.com/crm/v2/Contacts"
headers = {
    "Authorization": f"Bearer {at}",
    "Content-Type": "application/json"
}

# Se setea una variable data con la informacion que se enviara por campo
data = {
    "data": [
        {
            "First_Name": "Leon",
            "Last_Name": "Trujillo"
        }
    ]
}


response = requests.post(url, headers=headers, json=data)


print("Status Code:", response.status_code)
print("Response Body:", response.json())