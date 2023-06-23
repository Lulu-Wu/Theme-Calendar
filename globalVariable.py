#define global varibal
from machine import RTC

class GlobalVal:
    rtc = RTC()
    touch_value_left = 0             #记录电容采样值
    touch_value_left_prev = 0        #记录上一次的电容采样值
    touch_value_right = 0
    touch_value_right_prev = 0
    holiday = set()                   #记录节假日信息
    holiday = {'2023-05-02', '2023-12-31', '2023-09-30', '2023-01-02', '2023-01-01', '2023-06-23', '2023-09-29', '2023-01-23', '2023-01-22', '2023-01-21', '2023-04-30', '2023-06-22', '2023-10-06', '2023-10-05', '2023-10-04', '2023-10-03', '2023-06-24', '2023-10-02', '2023-10-01', '2023-01-25', '2023-01-24', '2023-04-29', '2023-01-26', '2023-05-03', '2023-01-27', '2023-04-05', '2023-05-01'}
    workday_for_holiday = set()       #记录调休上班日
    workday_for_holiday = {'2023-10-08', '2023-10-07', '2023-04-23', '2023-01-29', '2023-01-28', '2023-05-06', '2023-06-25'}
    month_choose = [[0 for j in range(7)] for i in range(2)]
    date_choose = [[0 for j in range(7)] for i in range(5)]
    weekday_choose = [0 for i in range(7)]
    weather_choose = [0 for i in range(7)]
    month = 1
    
    
#define const varibal
class const:
#     MIN_WIDTH_GLOABL = 0
#     MIN_HEIGHT_GLOBAL = 0
#     MAX_WIDTH_GLOBAL = 32
#     MAX_HEIGHT_GLOBAL = 8
# 
#     MIN_WIDTH_LOCAL = 0
#     MIN_HEIGHT_LOCAL = 0
#     MAX_WIDTH_LOCAL = 32
#     MAX_HEIGHT_LOCAL = 8
# 
#     BASE_FREQ_VALUE = 300
    
    TOUCH_THRESHOLD = 400        #电容触摸阈值