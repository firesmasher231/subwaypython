import requests

url = 'https://vyper.io/entries/create?contest_id=445296&referrer_id=20458671&display_type=Landing%20Page'

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Length": "1087",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryhhAfRHIrbIWRxvTj",
    "Cookie": "_ga=GA1.2.899756481.1693007461; _ga_JFKY9J9Q57=GS1.1.1693007460.1.1.1693007952.55.0.0; _uetsid=3e6c92a043a211ee8ec9f721fabc9584; _uetvid=3e6cba2043a211ee8383e70578a3a4d6",
    "Host": "vyper.io",
    "Origin": "https://vy.lc",
    "Referer": "https://vy.lc/",
    "sec-ch-ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

data = """\
------WebKitFormBoundaryhhAfRHIrbIWRxvTj
Content-Disposition: form-data; name="_csrf"

NVF1bFYtWVdmPSQ6ZxwwNl0zMlQTbxQ0czM2GhkaEBpdOhMEOhs/FA==
------WebKitFormBoundaryhhAfRHIrbIWRxvTj
Content-Disposition: form-data; name="Entries[contest_id]"

445296
------WebKitFormBoundaryhhAfRHIrbIWRxvTj
Content-Disposition: form-data; name="Entries[referrer_id]"

20458671
------WebKitFormBoundaryhhAfRHIrbIWRxvTj
Content-Disposition: form-data; name="Entries[registration_ip]"

54.151.31.245
------WebKitFormBoundaryhhAfRHIrbIWRxvTj
Content-Disposition: form-data; name="Entries[gc]"

1e213483
------WebKitFormBoundaryhhAfRHIrbIWRxvTj
Content-Disposition: form-data; name="Entries[full_name]"

Name
------WebKitFormBoundaryhhAfRHIrbIWRxvTj
Content-Disposition: form-data; name="Entries[email]"

zvq91n2nxl@icznn.com
------WebKitFormBoundaryhhAfRHIrbIWRxvTj
Content-Disposition: form-data; name="terms_text"

on
------WebKitFormBoundaryhhAfRHIrbIWRxvTj
Content-Disposition: form-data; name="g-recaptcha-response"


------WebKitFormBoundaryhhAfRHIrbIWRxvTj--
"""

response = requests.post(url, data=data, headers=headers)

print(response.text)
