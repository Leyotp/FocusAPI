import requests
import access_token

def create_contact(first_name,last_name):
    at = access_token.at

    try:
        headers = {
            "Authorization": f"Bearer {at}",
            "Content-Type": "application/json"
        }

        contact_data = {
        "data": [
            {
                "First_Name": first_name,
                "Last_Name": last_name
            }
        ]
    }

        url = "https://www.zohoapis.com/crm/v2/Contacts"

        resp = requests.post(url, headers=headers, json=contact_data)
        resp.raise_for_status()
        

        print("Status Code:", resp.status_code)
        print("Contact created successfully:", resp.json())
    

    except requests.exceptions.RequestException as e:   
        print("An error occurred while creating the contact:", str(e))
        print(resp.text)



if __name__ == "__main__":

    first_name = input("Enter the contact's first name: ")
    last_name = input("Enter the contact's last name: ")

    
    create_contact(first_name, last_name)