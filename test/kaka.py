import requests
import json

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

# 사용자 토큰
headers = {"Authorization": "Bearer " + "zewAa3Gk1NSBklDd_QZ1TZ8_1a_f1xwhNrWwEQo9dVoAAAF5x9vuWw"}

text = """
👉스마트벨 알람
--------------------------------
테스트입니다.
https://drive.google.com/file/d/1_cuskySCMBeiFZvp_BKpy5pagES6ogfp/view
"""
data = {
    "template_object": json.dumps(
        {
            "object_type": "text",
            "text": text,
            "link": {
                "web_url": "https://developers.kakao.com",
                "mobile_web_url": "https://developers.kakao.com",
            },
            "button_title": "바로 확인",
        }
    )
}

response = requests.post(url, headers=headers, data=data)
print(response.status_code)
if response.json().get("result_code") == 0:
    print("메시지를 성공적으로 보냈습니다.")
else:
    print("메시지를 성공적으로 보내지 못했습니다. 오류메시지 : " + str(response.json()))
