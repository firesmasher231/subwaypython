import requests
import json

url = 'https://rewards.subway.co.uk/tx-sub/members'
headers = {
    "Accept-Encoding": "gzip",
    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2R1bGVDb2RlIjoiU1VCX1NUT1JNQk9STiIsImlzcyI6IlRyYW54YWN0b3IgTHRkIiwidXNlclR5cGUiOiIxIiwiZXhwIjoxNjk4NTExNTk4LCJ0cmFkZXJJZCI6IjE3NDczNTUzNSIsInVzZXJOYW1lIjoibDUwaHF4NGlocXo5QHR4Y2N0LmNvbSIsImlhdCI6MTY5ODUwNzk5OCwidXNlcklkIjoiMTc0NzM1NTM1IiwicHJvZ3JhbUlkIjoiNiJ9.MBMgQwm7_C_ZyrDIgDjUa7itXm3iKeiVcWfk463aRic",
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