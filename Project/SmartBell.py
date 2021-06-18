#-*-coding: utf-8-*-
from sense_hat import SenseHat
from time import sleep
from SoundOutput import sound_output    # 소리 출력
from VisitorCheck import take_photo     # 사진 촬영
from Recorder import record             # 녹음
from GoogleDrive import file_upload
from KakaoMessage import send_message
from Controller import what_day_is_today, url_shorter, visit_cnt_check
from decorator import time_chek
import time

sense = SenseHat()
OUTMODE = False
VisitCount =0

@time_chek
def outmonde_act():
    date, f_date = what_day_is_today()
    record("record_"+f_date)            # 메세지 안내 및 방문목적
    take_photo("picture_"+f_date)        # 방문자 촬영
    picture_id, record_id = file_upload(f_date)
    send_message(picture_id, record_id, date)
    

sense.clear()   # LED 초기화
while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":     # 외출모드 변환
                sound_output("out_mode")
                OUTMODE = True

            elif event.direction == "down": # 외출모드 취소
                sound_output("out_mode_cancel")
                OUTMODE = False

            elif event.direction == "left": # 방문기록 확인
                VisitCount = visit_cnt_check(VisitCount)
                
            elif event.direction == "right": # 방문 기록 초기화
                VisitCount = visit_cnt_check(-1)

            elif event.direction == "middle":
                if OUTMODE == True: # 외출 모드 O
                    outmonde_act()
                    VisitCount +=1


                elif OUTMODE == False:  # 외출 모드 X
                    sound_output("wait")
        
        sleep(0.5)
        sense.clear()