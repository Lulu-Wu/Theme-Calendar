# coding:utf-8
# 获取指定城市location ID
# https://geoapi.qweather.com/v2/city/lookup?location=%E6%AD%A6%E6%B1%89&key=ff35520edf0a43acaa7481faac4f403b
# 通过location id获取指定城市实时天气
# https://devapi.qweather.com/v7/weather/now?location=101200101&key=ff35520edf0a43acaa7481faac4f403b
import uzlib as zlib
import network,time
import urequests
import ujson
from globalVariable import GlobalVal
FTEXT    = 1
FHCRC    = 2
FEXTRA   = 4
FNAME    = 8
FCOMMENT = 16

#hefeng API response data has compressed, need decompress to use decode method
def decompress(data):
    assert data[0] == 0x1f and data[1] == 0x8b
    assert data[2] == 8
    flg = data[3]
    assert flg & 0xe0 == 0
    i = 10
    if flg & FEXTRA:
        i += data[11] << 8 + data[10] + 2
    if flg & FNAME:
        while data[i]:
            i += 1
        i += 1
    if flg & FCOMMENT:
        while data[i]:
            i += 1
        i += 1
    if flg & FHCRC:
        i += 2
    return zlib.decompress(memoryview(data)[i:], -15)


def weather_info():
    location_id = 101200101     #武汉的location_id
#     url = f'https://devapi.qweather.com/v7/weather/now?location={location_id}&key=ff35520edf0a43acaa7481faac4f403b'
    url = 'https://devapi.qweather.com/v7/weather/now?location=101200101&key=ff35520edf0a43acaa7481faac4f403b'
    try:
        retry_times = 3
        while(retry_times > 0):
            response = urequests.get(url)
            if response.status_code == 200:
                data = decompress(response.content).decode()
                response_json = ujson.loads(data)                         #transfer bytes data to json format
                GlobalVal.today_weather = response_json['now']['text']           #get the current weather
                break
            else:
                retry_times -= 1
                print("Retry times left:", retry_times)
    except:
        print("failed to get weather info")
