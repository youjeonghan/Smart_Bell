#-*-coding: utf-8-*-
import time
import functools


def time_chek(original_func):
    """ 함수 실행시간 확인 데코레이터"""
    @functools.wraps(original_func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)
        end = time.time()
        # print(original_func.__name__ +" 함수 수행시간: %f 초" % (end - start))
        return result
    return wrapper