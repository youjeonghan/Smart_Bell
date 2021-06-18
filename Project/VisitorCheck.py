#-*-coding: utf-8-*-
"""
방문자 확인 (카메라 촬영)
"""
from picamera import PiCamera
from time import sleep
from SoundOutput import sound_output
from decorator import time_chek

@time_chek
def take_photo(file_name):
    """
    input: 저장 파일명
    output: X
    description:
    방문자 촬영 안내 후 사진 촬영
    """
    file_path = "/home/jeongran/Project/Image/"+file_name+".jpg"
    camera = PiCamera()
    camera.start_preview()
    camera.brightness = 52  # 밝기 조절 / 기본값 50
    camera.rotation = 180   # 카메라 회전 / 기본값 0
    sound_output("visitor_check")   # 방문자 확인 안내 / 2초 정도 조도 조절 시간
    sound_output("camera_shutter_click")   # 방문자 확인 안내
    camera.capture(file_path)
    camera.stop_preview()
    camera.close()          # picamera instance 종료

if __name__=="__main__":
    take_photo("test6")