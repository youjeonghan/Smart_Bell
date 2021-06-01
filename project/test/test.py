import requests
import urllib
import json


def getAccessToken(refreshToken):
    url = "https://kauth.kakao.com/oauth/token"
    payload = (
        "grant_type=refresh_token&client_id=************************************&refresh_token="
        + refreshToken
    )
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cache-Control": "no-cache",
    }
    reponse = requests.request("POST", url, data=payload, headers=headers)
    access_token = json.loads(((reponse.text).encode("utf-8")))
    return access_token


result = getAccessToken(
    "**************************************************"
)  # 메세지 받을 사람의 REFRESH TOKEN 이용
print(result)