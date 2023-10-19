import requests


url = 'https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=10'

response = requests.get(url)

emails = response.text.replace("[", "").replace("]", "").replace('"', "").replace(" ", "").split(",")


print(emails) 
