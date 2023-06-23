# coding:utf-8
import urequests
import ujson
from globalVariable import GlobalVal

def holiday_info(year):
    url = f'https://timor.tech/api/holiday/year/{year}/'
    global str_response
    global mid_data
    try:
        retry_times = 3
        while(retry_times > 0):
            response = urequests.get(url)
            if response.status_code == 200:
                response_json = ujson.loads(response.content)['holiday']     #transfer bytes data to json format
                for data in response_json:                                   #response_json type is dict, response_json[data] is the holiday information  
#                     print(response_json[data]['holiday'])
                    if response_json[data]['holiday'] == True:               #the date is a public holiday
                        GlobalVal.holiday.add(response_json[data]['date'])
                    elif response_json[data]['holiday'] == False:            #the date is a working day for toil
                        GlobalVal.workday_for_holiday.add(response_json[data]['date'])
                break
            else:
                retry_times -= 1
                print("Retry times left:", retry_times)
        print("holiday info:", GlobalVal.holiday)
        print("workday_for_holiday info:", GlobalVal.workday_for_holiday)
    except:
        print("failed to get holiday info")

