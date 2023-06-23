from machine import Timer
from init import tim0,tim1,touch_key_left,touch_key_right
from globalVariable import GlobalVal,const

#get time form suning
def sync_time():
    try:
        response = urequests.get('http://quan.suning.com/getSysTime.do')
        print(response.status_code)
        if response.status_code == 200:  
            time = response.json()['sysTime1']
            year = int(time[0:4])
            month = int(time[4:6])
            day = int(time[6:8])
            hour = int(time[8:10])
            minite = int(time[10:12])
            second = int(time[12:14])
            web_time = [hour, minite]
            return web_time
    except:
        print("failed to obtain suning network time")

# check if there is touch to switch month to the previous one
def touch_callback_left():
    GlobalVal.touch_value_left = touch_key_left.read()
    if (GlobalVal.touch_value_left < const.TOUCH_THRESHOLD) and (GlobalVal.touch_value_left_prev > const.TOUCH_THRESHOLD):
        print("switch month to the previous one")
    GlobalVal.touch_value_left_prev = GlobalVal.touch_value_left
        
# check if there is touch to switch month to the next one
def touch_callback_right():
    GlobalVal.touch_value_right = touch_key_right.read()
    if (GlobalVal.touch_value_right < const.TOUCH_THRESHOLD) and (GlobalVal.touch_value_right_prev > const.TOUCH_THRESHOLD):
        print("switch month to the next one")
        GlobalVal.month += 1
        if GlobalVal.month > 12:
            GlobalVal.month = 1
    GlobalVal.touch_value_right_prev = GlobalVal.touch_value_right
    
    
def sync_calendar():
    from holiday import holiday_info
    print("start to get calendar info from network")
    holiday_info(2023)

def month_switch_left_timer(timer):
    timer.init(period = 5, mode = Timer.PERIODIC, callback = lambda t:touch_callback_left())
    
def month_switch_right_timer(timer):
    timer.init(period = 5, mode = Timer.PERIODIC, callback = lambda t:touch_callback_right())
    
def sync_calendar_timer(timer):        #every 30days to get calendar info from network
    timer.init(period = 1000*3600*24, mode = Timer.PERIODIC, callback = lambda t:sync_calendar())
