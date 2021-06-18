#-*-coding: utf-8-*-
import pygame


def sound_output(file_name):
    """
    input: 음성 파일 경로
    output: X
    description:
    해당 음성을 출력
    """
    pygame.mixer.init()                     # mixer 초기화
    file_path = "/home/jeongran/Project/Sound/"+file_name+".mp3"
    pygame.mixer.music.load(file_path)      # 파일 load
    pygame.mixer.music.set_volume(1.0)      # 음량 최대
    pygame.mixer.music.play()               # 파일 실행
    while pygame.mixer.music.get_busy() == True:    # 파일 종료까지 대기
        continue

if __name__=="__main__":
    sound_output("wait")
