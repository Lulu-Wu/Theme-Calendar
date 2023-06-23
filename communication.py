import network

#连接WIFI
def wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('CUG_ZDH_2.4G', '724334359@qq.com')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())