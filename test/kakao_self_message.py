import os
import json
import requests


def sendToMeMessage(text):
    header = {"Authorization": "Bearer " + KAKAO_TOKEN}
    # url = https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code&scope=talk_message
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"  # 나에게 보내기 주소
    # &scope=talk_message
    post = {
        "object_type": "text",
        "text": text,
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com",
        },
        "button_title": "바로 확인",
    }
    data = {"template_object": json.dumps(post)}
    return requests.post(url, headers=header, data=data)


text = "Hello, This is KaKao Message Test!!(" + os.path.basename(__file__).replace(".py", ")")

KAKAO_TOKEN = "Ol7cQZnMiLXu20E_wM9R5bmQmH4D5sbJAE2hLwopyNkAAAF5xZVAmg"

print(sendToMeMessage(text).text)