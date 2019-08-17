import requests
from requests.auth import HTTPBasicAuth


def send_sms(number, text):
    data = {
        "messages":
            [
                {
                    "recipient": number,
                    "message-id": 1113,
                    "sms": {
                        "originator": "3700",
                        "content": {
                            "text": text
                        }
                    }
                }
            ]
    }
    url = "http://91.204.239.42:8083/broker-api/send"
    requests.post(url, json=data, auth=HTTPBasicAuth('manpower', 'A1MeUf5'))
