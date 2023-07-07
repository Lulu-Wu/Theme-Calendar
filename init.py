from machine import Pin,TouchPad,Timer 
from neopixel import NeoPixel
import ujson
import urequests
from globalVariable import GlobalVal 

#引脚使用
# LED信号口
pin_led = Pin(12, Pin.OUT)
np = NeoPixel(pin_led, 70)

# touch key
touch_key_left = TouchPad(Pin(32))      #向左切换月份
touch_key_right = TouchPad(Pin(33))    #向右切换月份
touch_key_theme = TouchPad(Pin(27))    #向右切换月份

#interrupt_timer
tim0 = Timer(0)
tim1 = Timer(1)
tim2 = Timer(2)

#sync real time from suning one time
def sync_time():
    try:
        retry_times = 3
        while(retry_times > 0):
            response = urequests.get('http://quan.suning.com/getSysTime.do')    # get time first
            if response.status_code == 200:
                time = response.json()['sysTime1']
                year = int(time[0:4])
                month = int(time[4:6])
                day = int(time[6:8])
                hour = int(time[8:10])
                minite = int(time[10:12])
                second = int(time[12:14])
                GlobalVal.rtc.datetime((year, month, day, 1, hour, minite, second, 0))
                break
            else:
                retry_times -= 1
                print("Retry times left:", retry_times)
    except:
        print("Sync time from network error.")
        pass