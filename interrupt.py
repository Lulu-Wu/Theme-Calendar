from machine import Timer
from init import tim0,tim1,touch_key_left,touch_key_right,touch_key_theme
from globalVariable import GlobalVal,const

# check if there is touch to switch month to the previous one
def touch_callback_left():
    GlobalVal.touch_value_left = touch_key_left.read()
    if (GlobalVal.touch_value_left < const.TOUCH_THRESHOLD) and (GlobalVal.touch_value_left_prev > const.TOUCH_THRESHOLD):
        print("switch month to the previous one")
        GlobalVal.month -= 1
        if GlobalVal.month < 1:
            GlobalVal.month = 12
            GlobalVal.year -= 1
            GlobalVal.need_update_holiday = 1
            if GlobalVal.year < 2023:
                GlobalVal.year = 2028
    GlobalVal.touch_value_left_prev = GlobalVal.touch_value_left
        
# check if there is touch to switch month to the next one
def touch_callback_right():
    GlobalVal.touch_value_right = touch_key_right.read()
    if (GlobalVal.touch_value_right < const.TOUCH_THRESHOLD) and (GlobalVal.touch_value_right_prev > const.TOUCH_THRESHOLD):
        print("switch month to the next one")
        GlobalVal.month += 1
        if GlobalVal.month > 12:
            GlobalVal.month = 1
            GlobalVal.year += 1
            GlobalVal.need_update_holiday = 1
            if GlobalVal.year > 2028:
                GlobalVal.year = 2023
    GlobalVal.touch_value_right_prev = GlobalVal.touch_value_right

# check if there is touch to switch color theme
def touch_callback_theme():
    GlobalVal.touch_value_theme = touch_key_theme.read()
    if (GlobalVal.touch_value_theme < const.TOUCH_THRESHOLD) and (GlobalVal.touch_value_theme_prev > const.TOUCH_THRESHOLD):
        print("switch them to the next one")
        GlobalVal.theme_mode += 1
        if GlobalVal.theme_mode > 4:
            GlobalVal.theme_mode = 0
    GlobalVal.touch_value_theme_prev = GlobalVal.touch_value_theme

# def sync_calendar():
#     from holiday import holiday_info
#     print("start to get calendar info from network")
#     holiday_info(2023)

def month_switch_left_timer(timer):
    timer.init(period = 5, mode = Timer.PERIODIC, callback = lambda t:touch_callback_left())
    
def month_switch_right_timer(timer):
    timer.init(period = 5, mode = Timer.PERIODIC, callback = lambda t:touch_callback_right())
    
def theme_switch_timer(timer):
    timer.init(period = 5, mode = Timer.PERIODIC, callback = lambda t:touch_callback_theme())
    
# def sync_calendar_timer(timer):        #every 30days to get calendar info from network
#     timer.init(period = 1000*3600*24, mode = Timer.PERIODIC, callback = lambda t:sync_calendar())

