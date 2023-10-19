import requests
import json

url = 'https://rewards.subway.co.uk/tx-sub/members'
headers = {
    "Accept-Encoding": "gzip",
    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2R1bGVDb2RlIjoiU1VCX1NUT1JNQk9STiIsImlzcyI6IlRyYW54YWN0b3IgTHRkIiwidXNlclR5cGUiOiIxIiwiZXhwIjoxNjkyOTU4MTYwLCJ0cmFkZXJJZCI6IjE3NDMxNDk2NiIsInVzZXJOYW1lIjoiZ2VuZ2FuYTk5QGdtYWlsLmNvbSIsIm1hc3RlclRva2VuIjoiWW1GbU16ZGhNMlV5TXpCaE5EVXlOV0psWWpaaE5qUTNaalUxTnpRek1UVT0iLCJpYXQiOjE2OTI5NTQ1NjAsInVzZXJJZCI6IjE3NDMxNDk2NiJ9.6LhNn1CYq8HeMmYZDkVnZyfQmMp14cbO-_QQDPNP4ew",
    "Connection": "Keep-Alive",
    "Host": "rewards.subway.co.uk",
    "User-Agent": "okhttp/4.9.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()

    loyalty_balance = str(data.get("loyaltyBalance"))
    email = data.get("email")
    first_name = data.get("firstName")
    last_name = data.get("lastName")

    # print(response.text.email + " " + response.text.firstName + " " + response.text.lastName + " " + response.text.loyaltyBalance)
    print(loyalty_balance + " | " + email + " | " + first_name + " | " + last_name) 
else:
    print(f"Request failed with status code: {response.text}")