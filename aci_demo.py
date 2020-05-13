import requests
import json
from pprint import pprint

# LOGIN
url = "https://sandboxapicdc.cisco.com:443/api/aaaLogin.json"

payload = {"aaaUser": {"attributes": {
    "name": "admin",
            "pwd": "ciscopsdt"
}
}
}

headers = {'Content-Type': "application/json"}

response = requests.post(
    url, data=json.dumps(payload), headers=headers, verify=False).json()

# pprint(json.dumps(response, indent=2, sort_keys=True))

token = response['imdata'][0]['aaaLogin']['attributes']['token']

# pprint(token)

# PARSE TOKEN AND SET COOKIE
cookie = {}
cookie['APIC-cookie'] = token


# GET APPLICATION PROFILE


url = "https://sandboxapicdc.cisco.com/api/node/mo/uni/tn-Heroes/ap-Save_The_Planet.json"

headers = {
    'cache-control': "no-cache"
}

get_response = requests.get(
    url, headers=headers, cookies=cookie, verify=False).json()

#print(json.dumps(get_response, indent=2, sort_keys=True))


# UPDATE APPLICATION DESCRIPTION
# ADDING DESCRIPTION

url = "https://sandboxapicdc.cisco.com/api/node/mo/uni/tn-Heroes/ap-Save_The_Planet.json"

post_payload = {"fvAp":
                {"attributes":
                 {
                     "descr": "",
                     "dn": "uni/tn-Heroes/ap-Save_The_Planet"
                 }
                 }
                }

post_response = requests.post(url, data=json.dumps(
    payload), cookies=cookie, headers=headers, verify=False).json()

get_response = requests.get(
    url, headers=headers, cookies=cookie, verify=False).json()

print(json.dumps(get_response, indent=2, sort_keys=True))
