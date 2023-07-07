from coordinateMap import coordinate_map
from calendar import calendar_choose,get_today
from init import np
import color
from globalVariable import GlobalVal
                    
def calendar_show(year, month, day):
    cur_date = get_today()
    #year
    np[coordinate_map(0, 0)] = color.default_color()
    for j in range(1, 7):
        if GlobalVal.year_choose[j-1] == 1:
            np[coordinate_map(0, j)] = color.cur_year_color()
        else:
            np[coordinate_map(0, j)] = color.default_color()
        np.write()
    
    #month
    for i in range(1, 3):
        for j in range(7):
            if GlobalVal.month_choose[i-1][j] == 1:
                np[coordinate_map(i, j)] = color.cur_month_color()
            else:
                np[coordinate_map(i, j)] = color.default_color()
            np.write()
        
    #date
    for i in range(3, 8):
        for j in range(7):
            if GlobalVal.date_choose[i-3][j] == 5:
                np[coordinate_map(i, j)] = color.date_type_color('today')
            elif GlobalVal.date_choose[i-3][j] == 1:
                np[coordinate_map(i, j)] = color.date_type_color('holiday')
            elif GlobalVal.date_choose[i-3][j] == 2:
                np[coordinate_map(i, j)] = color.date_type_color('toil')
            elif GlobalVal.date_choose[i-3][j] == 3:
                np[coordinate_map(i, j)] = color.date_type_color('weekend')
            elif GlobalVal.date_choose[i-3][j] == 4:
                np[coordinate_map(i, j)] = color.date_type_color('workday')
            else:
                np[coordinate_map(i, j)] = (0, 0, 0)
            np.write()
    
    #weekday
    for j in range(7):
        if GlobalVal.weekday_choose[j] == 1 and year == cur_date[0] and month == cur_date[1]:
            np[coordinate_map(8, j)] = color.cur_weekday_color()
        else:
            np[coordinate_map(8, j)] = color.default_color()
        np.write()
    
    #weather
    for j in range(7):
        if GlobalVal.weather_choose[j] == 1 and year == cur_date[0] and month == cur_date[1]:
            np[coordinate_map(9, j)] = color.cur_weather_color()
        else:
            np[coordinate_map(9, j)] = color.default_color()
        np.write()
                
    
    