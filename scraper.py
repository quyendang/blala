import json, urllib, http.client
import requests

pushoverAPIToken = "ah2hby41xn2viu41syq295ipeoss4e"
pushoverUserID = "uqyjaksy71vin1ftoafoujqqg1s8rz"



headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/10.0; Trident/6.0)'}
page = requests.get('https://googleads.g.doubleclick.net/mads/static/mad/sdk/native/sdk-core-v40-loader.appcache', headers=headers)
htmlstr = page.text
x = htmlstr.split("#")
y = x[3].split(" = ")
sdk = y[1]

message = "SDK change to " + sdk

if "sdk_20221206_RC00" in sdk:
    messages = {
        "token": pushoverAPIToken,
        "user": pushoverUserID,
        "message": message,
        "title": "SDK Alert",
        "html": 1,
        "priority": 1,
        "sound": "falling",
        "url": "https://googleads.g.doubleclick.net/mads/static/mad/sdk/native/sdk-core-v40-loader.appcache"
        }
    r = requests.post(url = "https://api.pushover.net/1/messages.json", data = messages)
    print(r.text)
