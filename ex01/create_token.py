import http.client
import os
import json
from dotenv import load_dotenv

load_dotenv()
username = os.getenv("PASQAL_EMAIL")
passwd = os.getenv("PASQAL_PASSWORD")

conn = http.client.HTTPSConnection("pasqal.eu.auth0.com")

payload = json.dumps({
    "client_id": "eiSaMfiINjiaXr0tnc2Bh1Mr6XPQ1BDK",
    "username": username,
    "password": passwd,
    "audience": "https://apis.pasqal.cloud/account/api/v1",
    "scope": "openid profile email",
    "realm": "pcs-users",
    "grant_type": "http://auth0.com/oauth/grant-type/password-realm"
})

headers = { "Content-Type": "application/json" }

conn.request("POST", "/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read().decode("utf-8")

print(f"Status: {res.status}")
print(data)