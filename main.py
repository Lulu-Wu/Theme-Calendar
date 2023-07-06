import time
from communication import wifi_connect
from holiday import holiday_info,update_holiday
from weather import weather_info
from calendar import calendar_choose,get_today,clear_choose
from init import np,tim0,tim1,tim2
from interrupt import month_switch_left_timer,month_switch_right_timer,theme_switch_timer
from globalVariable import GlobalVal
from show import calendar_show

month_switch_left_timer(tim0)
month_switch_right_timer(tim1)
theme_switch_timer(tim2)

wifi_connect()
holiday_info(2023)
weather_info()
day = get_today()[2]

count = 1
while True:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    calendar_choose(GlobalVal.year, GlobalVal.month, day)
    calendar_show(GlobalVal.year, GlobalVal.month, day)
    clear_choose()
    update_holiday()
    count += 1
    if count == 1000000000000000:
        weather_info()
        day = get_today()
        count = 1
    




