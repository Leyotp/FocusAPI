import requests

# Se setean los parametros a mandar al metodo response, url y params, que tiene las keys brindadas previamente para la respuesta API
url = "https://accounts.zoho.com/oauth/v2/token"
params = {
    "grant_type": "refresh_token",
    "client_id": "1000.NASSTGTS7A3YMCDXB7U7ZG09GKEN3H",
    "client_secret": "944f75f79aef9568bc25ad6995b9cbe18506a807e2",
    "refresh_token": "1000.365884a88476be0720d11c4931a3c026.ea403257d059d1f6727a715d72da4b9d"
}

# Resp contiene la url y los parametros como lo que se enviara al CRM 
resp = requests.post(url, params=params)

# Se extrae el token, pasandolo como JSON 
at = resp.json()["access_token"]

# Se imprime el token
print("Access Token:", at)