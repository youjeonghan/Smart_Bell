#-*-coding: utf-8-*-
import datetime
import pyshorteners
from pyshorteners import Shorteners
import re
from decorator import time_chek
from SoundOutput import sound_output

@time_chek
def what_day_is_today():
    """
    input: X
    output: string, string
    description:
    현재 시간을
    ex) 2021년 6월 2일 수요일 12:29 / 2021_06_02_12_29_53
    위와 같이 string으로 반환
    """
    now = datetime.datetime.now()
    t = ['월', '화', '수', '목', '금', '토', '일']
    r = datetime.datetime.today().weekday()
    day = str(now.year) + '년 ' + str(now.month) + '월 ' + str(now.day) + '일 ' + t[r] + '요일 ' + str(now.hour)+":"+ str(now.minute)
    p = re.compile(r'-|:|\.| ')
    p = p.sub('_',str(now))
    return day, p[:-7]  # p = "2021_06_08_16_58_53"

@time_chek
def url_shorter(url):
    """
    input: string
    output: string
    description:
    url이 들어오면 해당 url을 짧게 만들어 반환
    """
    s = pyshorteners.Shortener(Shorteners.TINYURL, timeout=3)
    result = s.short(url)
    return result

@time_chek
def visit_cnt_check(cnt):
    if 0<=cnt <10:
        sound_output("VisitHistory"+str(cnt))
    else:
        sound_output("VisitHistoryReset")
        cnt=0
    return cnt
if __name__=="__main__":
    """
    해당 모듈을 main으로 호출시 테스트 실행
    """
    print(what_day_is_today())
    print(url_shorter("https://drive.google.com/file/d/1_cuskySCMBeiFZvp_BKpy5pagES6ogfp/view"))