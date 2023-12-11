
import requests

postUrl='http://panel.1sms.com.tr:8080/api/smspost/v1'
musteriNo=''
kullaniciAdi=''
sifre=''
header="test"
orjinator=""

mesaj='Bu bir test mesajidir.'
numara1='05354447775'

headers = {"Content-Type": "text/xml; charset=UTF-8", "Content-Encoding": "UTF-8"}

string = """
<sms>
    <username>"""+kullaniciAdi+"""</username>
    <password>"""+sifre+"""</password>
    <header>"""+header+"""</header>
    <validity>"""+2880+"""</validity>
    <message>"""+mesaj+"""</message>
    <numaralar>"""+numara1+"""</numaralar>
</sms>
"""

response =  requests.post(postUrl, data={"data":string})

print(response.text)


#try catch ekle finally de disconnect felan


# sends value "12.6" to webapi - timestamp = fixed "2018-11-23T14:00:00Z"
import requests
import httplib2
import urllib3

# defining the api-endpoint
# \\lehmannme7480\AAA
API_ENDPOINT = "https://172.16.4.95/piwebapi/streams/F1DP9gA_4i5ui0aJABcUJd1W1gDgAAAAUEk0REVWUElcWU5ZUE9JTlQ/value/"

# data to be sent to api
data = {
    "Timestamp": "2019-09-25T16:00:00Z",
    "UnitsAbbreviation": "m",
    "Good": True,
    "Questionable": False,
    "Value": 13
}

# sending post request and saving response as response object
# you can generate Basic Authentication header on the website
#   https://www.blitter.se/utils/basic-authentication-header-generator/
headers = {'Content-Type': 'application/json', 'Authorization': "Basic S01UXFBJVmlzaW9uOkttXzEyMzQ=",
           "X-Requested-With": "XMLHttpRequest"}
r = requests.post(url=API_ENDPOINT, verify=False, json=data, headers=headers)
# extracting response text
pastebin_url = r.text
print(r)


import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://172.16.4.95/piwebapi/dataservers/F1DS9gA_4i5ui0aJABcUJd1W1gUEk0REVWUEk/points/"
serverWebID = "F1DS9gA_4i5ui0aJABcUJd1W1gUEk0REVWUEk"
#response = requests.get(url,auth=HTTPBasicAuth('PI4DEV','Password1'),verify=False)
headers = {"X-Requested-With": "XMLHttpRequest"}
myData = {
"Name": "YNYPoint",
"PointClass": "classic",
"PointType": "Float32",
"Step": False
}
addData = requests.post(url,data=json.dumps(myData),auth=HTTPBasicAuth('PI4DEV','Password1'),verify=False,headers=headers)
print(addData)
