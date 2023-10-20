import requests
import censusname
import time
import re

accounts =[]

## Get random emails

NumberofEmails = 100
i= 0
genCounter = 0
filename = "accounts.json"
squadCode = "b1iufn"
referralCode = "X-62KJW7O"
squadName = "Subway Squad"

url = 'https://www.1secmail.com/api/v1/?action=genRandomMailbox&count='+ str(NumberofEmails)

response = requests.get(url)

emails = response.text.replace("[", "").replace("]", "").replace('"', "").replace(" ", "").split(",")

print(" | 0/" + str(NumberofEmails) + " | Acquired Emails: "+ str(NumberofEmails)) 



## Register account with each email

for email in emails:

    i += 1 
    genCounter += 1

    formatting = " | " + str(i) + "/" + str(NumberofEmails) + " | "

    print(formatting + "Attempting Account Registration: "+ str(email))

    url = 'https://rewards.subway.co.uk/tx-sub/registration'

    headers = {
        "accept": "application/json",
        "Accept-Encoding": "gzip",
        "Accept-Language": "GB",
        "Connection": "Keep-Alive",
        "Content-Length": "242",
        "Content-Type": "application/json; charset=UTF-8",
        "Host": "rewards.subway.co.uk",
        "moduleCode": "SUB_STORMBORN",
        "User-Agent": "okhttp/4.9.0"
    }

    firstname = censusname.generate(nameformat='{given}', given='male')
    lastname = censusname.generate(nameformat='{surname}', given='male')

    myobj = {
    "channelApp": 1,
    "channelEmail": 1,
    "channelSMS": 0,
    "countryId": 10,
    "email": email,
    "firstName": firstname,
    "lastName": lastname,
    "password": "Password123!",
    "promoCode": referralCode,
    "typeCompetitions": 0,
    "typeNews": 0,
    "typeOffer": 0
    }

    x = requests.post(url, json=myobj, headers=headers)

    print(formatting + "Attempting Account Registration: "+ str(x.text))
    print(formatting + "Waiting for verification code...")

    time.sleep(7)

    ## Get verification code

    username = email.split("@")[0]
    domain = email.split("@")[1]

    url = 'https://www.1secmail.com/api/v1/?action=getMessages&login=' + username + '&domain=' + domain

    while True:
        response = requests.get(url)

        data = response.json()

        try:
            emailid = data[0].get("id")
            break
        except:
            print(formatting + "No verification code found yet, retrying...")
            time.sleep(5)
            continue

    url = 'https://www.1secmail.com/api/v1/?action=readMessage&login=' + username + '&domain=' + domain + '&id=' + str(emailid)

    response = requests.get(url)

    match = re.search(r'(?<=YOUR CODE).{7}', response.text)
    code = str(match.group(0)).replace(" ", "")
    if code:
        print(formatting + "Acquired verification code: "+ str(code))
    else:
        next()

    ## Verify account

    url = 'https://rewards.subway.co.uk/tx-sub/registration/activation/' + code

    print(formatting + "Verifying... : "+ str(url))

    verification_headers = {
        "accept": "application/json",
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Content-Length": "0",
        "Host": "rewards.subway.co.uk",
        "moduleCode": "SUB_STORMBORN",
        "User-Agent": "okhttp/4.9.0"
    }

    response = requests.put(url, headers=verification_headers)

    print(response.text)
    print(response.url)

    token = response.json().get("login").get("token")
    masterToken = response.json().get("login").get("masterToken")

    print(formatting + "Acquired token: " + str(token[:3]) + "..." + str(token[-5:]))

    ## Create Subsquad if not already exists // is full

    if (genCounter==8):
        url = 'https://rewards.subway.co.uk/tx-sub/squad-groups'
        headers = {
            "accept": "application/json",
            "Accept-Encoding": "gzip",
            "Authorization": token,
            "Connection": "Keep-Alive", 
            "Content-Length": "26",
            "Content-Type": "application/json",
            "Host": "rewards.subway.co.uk",
            "moduleCode": "SUB_STORMBORN",
            "User-Agent": "okhttp/4.9.0"
        }
        
        data = {
        "groupName": squadName,
        }

        response = requests.put(url, json=data, headers=headers)

        name = response.json().get("groups")[0].get("groupName")
        squadCode = response.json().get("groups")[0].get("groupUrn")

        print("Created squad: " + str(name))

        genCounter = 0

    ## Join subsquad

    url = 'https://rewards.subway.co.uk/tx-sub/members/squad-group'

    headers = {
        "Accept-Encoding": "gzip",
        "Authorization": token,
        "Connection": "Keep-Alive",
        "Content-Length": "21",
        "Content-Type": "application/json; charset=UTF-8",
        "Host": "rewards.subway.co.uk",
        "User-Agent": "okhttp/4.9.0"
    }

    myobj = {
        "groupUrn": squadCode
    }

    response = requests.post(url, json=myobj, headers=headers)

    print(formatting + "Joined squad: " + str(squadCode))

        
    url = 'https://rewards.subway.co.uk/tx-sub/members'
    headers = {
        "Accept-Encoding": "gzip",
        "Authorization": token,
        "Connection": "Keep-Alive",
        "Host": "rewards.subway.co.uk",
        "User-Agent": "okhttp/4.9.0"
    }

    response = requests.get(url, headers=headers)

    loyaltyId =  response.json().get("virtualCard")
    qrcode = "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data="+ str(loyaltyId)
    points = response.json().get("loyaltyBalance")

    accounts.append({"email": email, "token": token, "masterToken": masterToken, "loyaltyId": loyaltyId,"qrcode": qrcode, "points": points, "squadCode": squadCode, "referralCode": referralCode })

    print(formatting + "Acquired QR code for loyalty card: " + str(loyaltyId))

    ## Getting referral code so each account can be used to refer next

    url = 'https://promocode.tranxactor.com/promoCode/me'
    headers = {
        "Accept-Encoding": "gzip",
        "Authorization": token,
        "Connection": "Keep-Alive",
        "Host": "promocode.tranxactor.com",
        "User-Agent": "okhttp/4.9.0"
    }

    response = requests.get(url, headers=headers)

    referralCode = response.json()[0].get("code")

    print(formatting + "Acquired referral code: " + str(referralCode))


## output all accounts to file accounts.json

with open(filename, "w") as f:
    f.write(str(accounts))

print(formatting + "Accounts written to file: " + filename )

