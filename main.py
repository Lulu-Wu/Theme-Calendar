import time
from time import sleep
from communication import wifi_connect
from holiday import holiday_info
from calendar import calendar_choose
from init import np,tim0,tim1
from interrupt import month_switch_left_timer,month_switch_right_timer,sync_calendar_timer
from show import calendar_show
from globalVariable import GlobalVal  


month_switch_left_timer(tim0)
month_switch_right_timer(tim1)
# sync_calendar_timer(tim1)

wifi_connect()
# holiday_info(2023)
    
while True:
#     year = int(input("year:"))  #年
#     month = int(input("month:"))  #月
#     day = int(input("day:"))  #日
    year = 2023
    month = GlobalVal.month
    day = 1
    print("current month is :", month)
#     np.fill((0, 0, 0))
#     np.write()
    calendar_choose(year, month, day)
    calendar_show(year, month, day)
    GlobalVal.month_choose = [[0 for j in range(7)] for i in range(2)]
    GlobalVal.date_choose = [[0 for j in range(7)] for i in range(5)]
    GlobalVal.weekday_choose = [0 for i in range(7)]
    GlobalVal.weather_choose = [0 for i in range(7)]
    




