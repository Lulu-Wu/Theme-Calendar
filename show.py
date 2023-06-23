from coordinateMap import coordinate_map
from picture import number
from calendar import calendar_choose
from init import np
import color
from globalVariable import GlobalVal
                    
def calendar_show(year, month, day):
    for i in range(1, 3):
        for j in range(7):
            if GlobalVal.month_choose[i-1][j] == 1:
                np[coordinate_map(i, j)] = color.cur_month_color()
            else:
                np[coordinate_map(i, j)] = (0, 0, 0)
            np.write()
                
    for i in range(3, 8):
        for j in range(7):
            if GlobalVal.date_choose[i-3][j] == 1:
                np[coordinate_map(i, j)] = color.date_type_color('holiday')
            elif GlobalVal.date_choose[i-3][j] == 2:
                np[coordinate_map(i, j)] = color.date_type_color('toil')
            elif GlobalVal.date_choose[i-3][j] == 3:
                np[coordinate_map(i, j)] = color.date_type_color('weekend')
            elif GlobalVal.date_choose[i-3][j] == 4:
                np[coordinate_map(i, j)] = color.date_type_color('workday')
            np.write()
                
    for j in range(7):
        if GlobalVal.weekday_choose[j] == 1:
            np[coordinate_map(8, j)] = color.cur_weekday_color()
        else:
            np[coordinate_map(8, j)] = (0, 0, 0)
        np.write()
        
                
    
    