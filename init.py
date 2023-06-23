from machine import Pin,TouchPad,Timer 
from neopixel import NeoPixel

#引脚使用
# LED信号口
pin_led = Pin(13, Pin.OUT)
np = NeoPixel(pin_led, 70)

# touch key
touch_key_left = TouchPad(Pin(4))      #向左切换月份
touch_key_right = TouchPad(Pin(27))    #向右切换月份

#interrupt_timer
tim0 = Timer(0)
tim1 = Timer(1)