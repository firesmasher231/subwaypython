from flask import Flask, jsonify, request
import requests
import censusname
import time
import re
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def get_accounts_data():
    try:
        # Assuming the JSON file is in the same directory as your script
        json_file_path = './accounts.json'

        # Load JSON data
        with open(json_file_path, 'r') as file:
            data = json.loads(file)
            

        # Serve the JSON data
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})




@app.route('/delete-account', methods=['GET', 'POST'])
def delete_accounts():
    try:

        # Assuming the JSON file is in the same directory as your script
        json_file_path = './accounts.json'

        # Load accounts data which is in accounts.json file but is in a list of json objects
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            
        # Get the email from the request
        email = request.args.get('email')
        
        # Loop through the list of json objects and delete the one with the email that matches the email from the request
        for i in range(len(data)):
            if data[i]['email'] == email:
                del data[i]
                break

        # Save the updated list of json objects to the json file
        with open(json_file_path, 'w') as file:
            json.dump(data, file)

        # Serve the JSON data
        return jsonify(data)


    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/generate-accounts', methods=['GET'])
def generate_accounts():
    accounts = []

    # Get random emails
    NumberofEmails = 3
    i = 0
    genCounter = 0
    filename = "accounts.json"
    squadCode = "b1iufn"
    referralCode = "X-62KJW7O"
    squadName = "Subway Squad"

    url = 'https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=' + str(NumberofEmails)

    response = requests.get(url)
    emails = response.json()

    for email in emails:
        i += 1
        genCounter += 1

        formatting = " | " + str(i) + "/" + str(NumberofEmails) + " | "

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

        print(formatting + "Using Referral code " + str(referralCode))

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

        print(formatting + "Attempting Account Registration: " + str(x.text))
        print(formatting + "Waiting for verification code...")

        time.sleep(7)

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
            print(formatting + "Acquired verification code: " + str(code))
        else:
            next()

        url = 'https://rewards.subway.co.uk/tx-sub/registration/activation/' + code

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
        token = response.json().get("login").get("token")
        masterToken = response.json().get("login").get("masterToken")

        print(formatting + "Acquired token: " + str(token[:3]) + "..." + str(token[-5:]))

        if genCounter == 8:
            url = 'https://rewards.subway.co.uk/tx-sub/squad-groups'
            headers = {
                "accept": "application.json",
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

            # Inside the block where you make a request to get groups
            response = requests.put(url, json=data, headers=headers)

            try:
                name = response.json().get("groups")[0].get("groupName")
                squadCode = response.json().get("groups")[0].get("groupUrn")
            except json.decoder.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                print(f"Response text: {response.text}")
                name = None
                squadCode = None

            if name:
                print("Created squad: " + str(name))
            else:
                print("Error creating squad. Check the response for details.")


            # response = requests.put(url, json=data, headers=headers)

            # name = response.json().get("groups")[0].get("groupName")
            # squadCode = response.json().get("groups")[0].get("groupUrn")

            print("Created squad: " + str(name))

            genCounter = 0

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

        loyaltyId = response.json().get("virtualCard")
        qrcode = "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=" + str(loyaltyId)
        points = response.json().get("loyaltyBalance")

        accounts.append({"email": email, "token": token, "masterToken": masterToken, "loyaltyId": loyaltyId,
                         "qrcode": qrcode, "points": points, "squadCode": squadCode, "referralCode": referralCode})

        print(formatting + "Acquired QR code for loyalty card: " + str(loyaltyId))

        url = 'https://promocode.tranxactor.com/promoCode/me'
        headers = {
            "Accept-Encoding": "gzip",
            "Authorization": token,
            "Connection": "Keep-Alive",
            "Host": "promocode.tranxactor.com",
            "User-Agent": "okhttp/4.9.0"
        }

        response = requests.get(url, headers=headers)

        # referralCode = response.json()[0].get("code")

        # print(formatting + "Acquired referral code: " + str(referralCode))

    with open(filename, "w") as f:
        # save as a json object instead of a list of json objects
        json.dump(accounts, f)


    print(formatting + "Accounts written to file: " + filename)
    
    return jsonify({"message": "Accounts generated and written to file", "accounts": accounts})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
