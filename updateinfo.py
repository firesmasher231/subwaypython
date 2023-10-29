import requests
import json
import time
import re

# with open('accounts-batch1.json', 'r') as json_file:
#     data = json_file.read()

# filename = "accounts.json"

# accountsData = json.loads(data)

null = None


accountsData = [
  {
    "email": "fblv2tej@vjuum.com",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2R1bGVDb2RlIjoiU1VCX1NUT1JNQk9STiIsImlzcyI6IlRyYW54YWN0b3IgTHRkIiwidXNlclR5cGUiOiIxIiwiZXhwIjoxNjk4NTQ2ODcyLCJ0cmFkZXJJZCI6IjE3NDc4MjA0MSIsInVzZXJOYW1lIjoiZmJsdjJ0ZWpAdmp1dW0uY29tIiwiaWF0IjoxNjk4NTM5NjcyLCJ1c2VySWQiOiIxNzQ3ODIwNDEiLCJwcm9ncmFtSWQiOiI2In0.LUR0-nzkB13herkHZ9BA98gGXQ0VZWtSpYEInEYdQ5M",
    "masterToken": "YjFmZTcxZTkxOTM1NDFkZTlmOWU0YTljMDllZGIxMjY=",
    "loyaltyId": "6338450225779724",
    "qrcode": "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=6338450225779724",
    "points": 250,
    "squadCode": null,
    "referralCode": "X-63632KO"
  },
  {
    "email": "5ngqvczn1w1@ezztt.com",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2R1bGVDb2RlIjoiU1VCX1NUT1JNQk9STiIsImlzcyI6IlRyYW54YWN0b3IgTHRkIiwidXNlclR5cGUiOiIxIiwiZXhwIjoxNjk4NTQ2ODgxLCJ0cmFkZXJJZCI6IjE3NDc4MjA0MiIsInVzZXJOYW1lIjoiNW5ncXZjem4xdzFAZXp6dHQuY29tIiwiaWF0IjoxNjk4NTM5NjgxLCJ1c2VySWQiOiIxNzQ3ODIwNDIiLCJwcm9ncmFtSWQiOiI2In0.ICboeZntw_uMWkdOm2cY_swhZfe7O_gR4yb0bzE3dzU",
    "masterToken": "OGQxNThkMTE1NDA1NGU1MGE2ODQ4Y2Y3OGUwYmE3NTQ=",
    "loyaltyId": "6338450261829839",
    "qrcode": "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=6338450261829839",
    "points": 250,
    "squadCode": null,
    "referralCode": "X-63632KO"
  },
  {
    "email": "l1cskx@txcct.com",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2R1bGVDb2RlIjoiU1VCX1NUT1JNQk9STiIsImlzcyI6IlRyYW54YWN0b3IgTHRkIiwidXNlclR5cGUiOiIxIiwiZXhwIjoxNjk4NTQ2ODkwLCJ0cmFkZXJJZCI6IjE3NDc4MjA0MyIsInVzZXJOYW1lIjoibDFjc2t4QHR4Y2N0LmNvbSIsImlhdCI6MTY5ODUzOTY5MCwidXNlcklkIjoiMTc0NzgyMDQzIiwicHJvZ3JhbUlkIjoiNiJ9.EGPXxkEKvDk5Sd7867RTyAh2K6BGzCgaKOEmSRcp92k",
    "masterToken": "NzY1ZTE2MTRhYmRlNGIzMjg4ZGFmMjAzY2JkMjk1NjI=",
    "loyaltyId": "6338450294859969",
    "qrcode": "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=6338450294859969",
    "points": 250,
    "squadCode": null,
    "referralCode": "X-63632KO"
  }]


for i in range(len(accountsData)):

    token = accountsData[i].get("token")
    email = accountsData[i].get("email")
    masterToken = accountsData[i].get("masterToken")
    squadCode = accountsData[i].get("squadCode")
    referralCode = accountsData[i].get("referralCode")

    url = 'https://rewards.subway.co.uk/tx-auth/auth/logon'
    headers = {
        'Accept-Encoding': 'gzip',
        'appVersion': '1.8.3',
        'Connection': 'Keep-Alive',
        'Content-Length': '52',
        'Content-Type': 'application/json; charset=UTF-8',
        'deviceId': '00000000-5e1f-f5f9-ffff-ffffef05ac4a',
        'Host': 'rewards.subway.co.uk',
        'latitude': '0',
        'longitude': '0',
        'moduleCode': 'SUB_STORMBORN',
        'platform': 'Android',
        'User-Agent': 'okhttp/4.9.0'
    }

    myobj = {
        "username": email,
        "password": "Password123!",
    }

    x = requests.post(url, json=myobj, headers=headers)

    print("Attempting token refresh: " + str(x.text))

    # verify email code

    ## Get verification code

    username = email.split("@")[0]
    domain = email.split("@")[1]

    url = 'https://www.1secmail.com/api/v1/?action=getMessages&login=' + username + '&domain=' + domain

    time.sleep(5)

    while True:
        response = requests.get(url)

        data = response.json()

        try:
            emailid = data[0].get("id")
            break
        except:
            print("No verification code found yet, retrying...")
            time.sleep(5)
            continue

    url = 'https://www.1secmail.com/api/v1/?action=readMessage&login=' + username + '&domain=' + domain + '&id=' + str(emailid)

    response = requests.get(url)

    # Extract the code using a regular expression
    match = re.search(r'Your code: ([A-Z0-9]{6})', response.text)

    print("Attempting to extract verification code from email: " + str(response.text))
    print("Verification code: " + str(match))

    if match:
        code = str(match.group(0)).split(" ")[2]
        if code:
            print("Acquired verification code: "+ str(code))
    else:
        next()

    ##


    url = 'https://rewards.subway.co.uk/tx-sub/registration/verification/' + str(code)
    headers = {
    'accept': 'application/json',
    'Accept-Encoding': 'gzip',
    'Connection': 'Keep-Alive',
    'Content-Length': '0',
    'Host': 'rewards.subway.co.uk',
    'moduleCode': 'SUB_STORMBORN',
    'User-Agent': 'okhttp/4.9.0'
    }

    response = requests.put(url, headers=headers)

    print("Attempting Email Verification: " + str(response.text))

    token = response.json().get("login").get("token")

    print("Acquired new token: " + str(token))

    url = 'https://rewards.subway.co.uk/tx-sub/members'
    headers = {
        "Accept-Encoding": "gzip",
        "Authorization": token,
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




# for account in accountsData:

#     time.sleep(1)

#     print(accountsData.index(account))

#     token = accountsData[0].get("token")
#     email = accountsData[0].get("email")
#     masterToken = accountsData[0].get("masterToken")
#     squadCode = accountsData[0].get("squadCode")
#     referralCode = accountsData[0].get("referralCode")

#     url = 'https://rewards.subway.co.uk/tx-sub/login'
#     headers = {
#         'Accept-Encoding': 'gzip',
#         'Username': email,
#         'Password': 'Password123!',
#         'Authorization': token,
#         # 'Master-Token': masterToken,
#         'Connection': 'Keep-Alive',
#         'Host': 'rewards.subway.co.uk',
#         'User-Agent': 'okhttp/4.9.0'
#     }

#     response = requests.get(url, headers=headers)

#     if response.status_code == 200:
#         data = response.json()
#         print(data)  # Print the response JSON
#     else:
#         print('Request failed with status code:', response.status_code, response.text)

    # url = 'https://rewards.subway.co.uk/tx-sub/members'

    # headers = {
    #     "Accept-Encoding": "gzip",
    #     "Authorization": token,
    #     "Connection": "Keep-Alive",
    #     "Host": "rewards.subway.co.uk",
    #     "User-Agent": "okhttp/4.9.0"
    # }

    # response = requests.get(url, headers=headers)

    # print(response.json())

    # loyaltyId =  response.json().get("virtualCard")
    # qrcode = "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data="+ str(loyaltyId)
    # points = response.json().get("loyaltyBalance")

    # accounts.append({"email": email, "token": token, "masterToken": masterToken, "loyaltyId": loyaltyId,"qrcode": qrcode, "points": points, "squadCode": squadCode, "referralCode": referralCode })

# with open(filename, "w") as f:
#     f.write(str(accounts))

# print( "Accounts written to file: " + filename )