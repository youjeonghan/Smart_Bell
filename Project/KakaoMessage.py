#-*-coding: utf-8-*-
import requests
import json
from Controller import url_shorter
from decorator import time_chek

@time_chek
def send_message(image_name, record_name,date):
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    # 사용자 토큰
    headers = {"Authorization": "Bearer " + "wQqtQzW2lmAnIlBBgw5V71W7sTdOjSfN-qYh4AopcSEAAAF5_1P7vA"}

    time=date
    image_name = "https://drive.google.com/file/d/"+image_name+"/view?usp=sharing"
    image_link= str(url_shorter(image_name))
    record_name = "https://drive.google.com/file/d/"+record_name+"/view?usp=sharing"
    record_link= str(url_shorter(record_name))

    text = """
🔔 스마트벨 알람 🔔

⏰ %s

🙎 방문자 확인
%s

🔊 음성녹음 확인
%s""" % (time,image_link,record_link)

    data = {
        "template_object": json.dumps(
            {
                "object_type": "text",
                "text": text,
                "link": {
                    "web_url": "https://developers.kakao.com",
                    "mobile_web_url": "https://developers.kakao.com",
                },
                "button_title": "확인",
            }
        )
    }

    response = requests.post(url, headers=headers, data=data)
    if response.json().get("result_code") == 0:
        print("메시지를 성공적으로 보냈습니다.")
    else:
        print("메시지를 성공적으로 보내지 못했습니다. 오류메시지 : " + str(response.json()))

if __name__=="__main__":
    send_message("1dPpesDlvQcQ_IkqMXepp7krCzlU8AB8i", "1T0D6NEXecWnw_3ACDKFNJKaU3oAieEQz", "2016_06_08")