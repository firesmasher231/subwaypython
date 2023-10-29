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
		"email": "ytex7swnzm47@laafd.com",
		"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2R1bGVDb2RlIjoiU1VCX1NUT1JNQk9STiIsImlzcyI6IlRyYW54YWN0b3IgTHRkIiwidXNlclR5cGUiOiIxIiwiZXhwIjoxNjk3ODQ4MTU3LCJ0cmFkZXJJZCI6IjE3NDcyNzI1NyIsInVzZXJOYW1lIjoieXRleDdzd256bTQ3QGxhYWZkLmNvbSIsImlhdCI6MTY5Nzg0NDU1NywidXNlcklkIjoiMTc0NzI3MjU3IiwicHJvZ3JhbUlkIjoiNiJ9.TcDxk_F6YR_4S3iaT1rR1DEM85F8PnqG0qgwJmIH-4U",
		"masterToken": "YmUwZjMzOTllZDFmNDgzOGFlY2ExZTg3ZDRiOTIzZTU=",
		"loyaltyId": "6338450222098839",
		"qrcode": "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=6338450222098839",
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
    try:
        match = re.search(r'Your code: ([A-Z0-9]{6})', response.text)
    except:
        print("No verification code found yet, retrying...")
    
    if match == None:
        match = re.search(r'YOUR CODE ([A-Z0-9]{6})', response.text)
        

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

    print("Attempting Email Verification: " + str(url))

    response = requests.put(url, headers=headers)

    print("Attempting Email Verification: " + str(response.json().get("outComeMessage")))

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