from globalVariable import GlobalVal

MONTH = [[ 1,  2,  3,  4,  5,  6,  7],
         [ 8,  9, 10, 11, 12,  0,  0]]
DATE = [[ 1,  2,  3,  4,  5,  6,  7],
        [ 8,  9, 10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19, 20, 21],
        [22, 23, 24, 25, 26, 27, 28],
        [29, 30, 31,  0,  0,  0,  0]]
WEEKDAY = [1,  2,  3,  4,  5,  6,  7]
WEATHER = [1,  2,  3,  4,  5,  6,  7]

# get which day in one week
def get_weekday(year, month, day):
    if month in (1, 2): 
        month += 12
        year -= 1
    weekday = (day + 1 + 2 * month + 3 * (month + 1) // 5 + year + year // 4 - year // 100 + year // 400) % 7
    if weekday != 0:
        return weekday
    else:
        return 7
def get_today():
    real_time = GlobalVal.rtc.datetime()
    print(real_time)
    year = real_time[0]
    month = real_time[1]
    day = real_time[2]

# if one day is weekend
def is_weekend(year, month, day):
    weekday = get_weekday(year, month, day)
    if weekday in (6, 7):
        return True
    else:
        return False

# if one year is leap year
def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 1
    else:
        return 0

# total days of one month
def total_day_of_month(year, month):
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,11):
        return 30
    elif month == 2:
        return 28 + is_leap_year(year)
    else:
        return 0

# choose which month
def current_month_choose(month):
    if month < 8:
        GlobalVal.month_choose[0][month-1] = 1
    elif month < 13:
        GlobalVal.month_choose[1][month-8] = 1

# choose which date and the date is which type (holiday, working day for toil, normal weekend, normal working day)
def current_date_choose(year, month):
    for i in range(0, 5):
        for j in range(7):
            cur_day_is_weekend = is_weekend(year, month, DATE[i][j])
            day_count = total_day_of_month(year, month)
            if DATE[i][j] > 0 and DATE[i][j] <= day_count:
                if month < 10:
                    str_month = str(0)+str(month)
                else:
                    str_month = str(month)
                if DATE[i][j] < 10:
                    str_date = str(0)+str(DATE[i][j])
                else:
                    str_date = str(DATE[i][j])
                cur_day = str(year) + '-' + str_month + '-' + str_date
                if cur_day in GlobalVal.holiday:                    #curent_day is public holiday
                    GlobalVal.date_choose[i][j] = 1
                elif cur_day in GlobalVal.workday_for_holiday:      #curent_day is working day for toil
                    GlobalVal.date_choose[i][j] = 2
                elif cur_day_is_weekend:                            #curent_day is normal weekend
                    GlobalVal.date_choose[i][j] = 3
                else:                                               #curent_day is normal working day
                    GlobalVal.date_choose[i][j] = 4

# choose which day (1~7)
def current_weekday_choose(year, month, day):
    weekday = get_weekday(year, month, day)
    GlobalVal.weekday_choose[weekday-1] = 1

# current_day weather
def current_weather_choose():
    today_weather = '晴'
    if today_weather == '晴':
        GlobalVal.weather_choose[0] = 1;
    elif today_weather == '阴':
        GlobalVal.weather_choose[1] = 1;
    elif '云' in today_weather:
        GlobalVal.weather_choose[2] = 1;
    elif '雨' in today_weather:
        GlobalVal.weather_choose[3] = 1;
    elif '雪' in today_weather:
        GlobalVal.weather_choose[4] = 1;
    else:
        GlobalVal.weather_choose[5] = 1;

def calendar_choose(year, month, day):
#     holiday_info(year)
    current_month_choose(month)
    current_date_choose(year, month)
    current_weekday_choose(year, month, day)
    current_weather_choose()

    print("current month_choose is: ", GlobalVal.month_choose)
    print("current date_choose is: ", GlobalVal.date_choose)
    print("current weekday_choose is: ", GlobalVal.weekday_choose)
    print("current weather_choose is: ", GlobalVal.weather_choose)
    

