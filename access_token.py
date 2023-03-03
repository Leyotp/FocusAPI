import requests
import os
from dotenv import load_dotenv

load_dotenv("connection.env")
client_id = os.environ.get("ZOHO_CLIENT_ID")
client_secret = os.environ.get("ZOHO_CLIENT_SECRET")
refresh_token = os.environ.get("ZOHO_REFRESH_TOKEN")

url = "https://accounts.zoho.com/oauth/v2/token"
params = {
    "grant_type": "refresh_token",
    "client_id": client_id,
    "client_secret": client_secret,
    "refresh_token": refresh_token }

   
resp = requests.post(url, params=params)



at = resp.json()["access_token"]
print("Access Token:", at)