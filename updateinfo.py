import requests
import json
import time

with open('accounts-batch1.json', 'r') as json_file:
    data = json_file.read()

filename = "accounts.json"

accountsData = json.loads(data)

accounts = []

for account in accountsData:

    time.sleep(1)

    print(accountsData.index(account))

    token = accountsData[0].get("token")
    email = accountsData[0].get("email")
    masterToken = accountsData[0].get("masterToken")
    squadCode = accountsData[0].get("squadCode")
    referralCode = accountsData[0].get("referralCode")

    url = 'https://rewards.subway.co.uk/tx-sub/members'
    headers = {
        'Accept-Encoding': 'gzip',
        'Authorization': token,
        'Connection': 'Keep-Alive',
        'Host': 'rewards.subway.co.uk',
        'User-Agent': 'okhttp/4.9.0'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(data)  # Print the response JSON
    else:
        print('Request failed with status code:', response.status_code, response.text)

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

with open(filename, "w") as f:
    f.write(str(accounts))

print( "Accounts written to file: " + filename )