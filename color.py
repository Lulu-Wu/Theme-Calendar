from globalVariable import GlobalVal 
# five theme color map
# 0：圣诞快乐
# 1：夏至未至
# 2：蓝色星空
# 3：一叶知秋
# 4：梦幻风铃
# 0: choose yaer, 4: not choose year
# 0: choose month, 4: not choose month
# 0: today, 1: Holiday, 2: toil, 3: weekend, 4: default
# 0: today weekday, 4: default
# 0: today weather, 4: default
color_map = {0:{0:0x0000C8, 1:0x965000, 2:0x960000, 3:0x009600, 4:0x960000},\
             1:{0:0x963200, 1:0xC83222, 2:0x009614, 3:0x960096, 4:0x009614},\
             2:{0:0x960096, 1:0x963200, 2:0x001996, 3:0x009632, 4:0x001996},\
             3:{0:0x009614, 1:0x006464, 2:0x963200, 3:0x960096, 4:0x963200},\
             4:{0:0x964214, 1:0x006415, 2:0x641064, 3:0xC83232, 4:0x641064}}

def cur_year_color():
    choose_year_color = color_map[GlobalVal.theme_mode][0]
    choose_year_color_r = ((choose_year_color >> 16) & 0xFF)
    choose_year_color_g = ((choose_year_color >>  8) & 0xFF)
    choose_year_color_b = ((choose_year_color >>  0) & 0xFF)
    return choose_year_color_r, choose_year_color_g, choose_year_color_b

def cur_month_color():
    choose_month_color = color_map[GlobalVal.theme_mode][0]
    choose_month_color_r = ((choose_month_color >> 16) & 0xFF)
    choose_month_color_g = ((choose_month_color >>  8) & 0xFF)
    choose_month_color_b = ((choose_month_color >>  0) & 0xFF)
    return choose_month_color_r, choose_month_color_g, choose_month_color_b

def cur_date_color():
    today_color = color_map[GlobalVal.theme_mode][0]
    today_color_r = ((today_color >> 16) & 0xFF)
    today_color_g = ((today_color >>  8) & 0xFF)
    today_color_b = ((today_color >>  0) & 0xFF)
    return today_color_r, today_color_g, today_color_b

def date_type_color(date_type):
    today_color = color_map[GlobalVal.theme_mode][0]
    today_color_r = ((today_color >> 16) & 0xFF)
    today_color_g = ((today_color >>  8) & 0xFF)
    today_color_b = ((today_color >>  0) & 0xFF)
    
    holiday_color = color_map[GlobalVal.theme_mode][1]
    holiday_color_r = ((holiday_color >> 16) & 0xFF)
    holiday_color_g = ((holiday_color >>  8) & 0xFF)
    holiday_color_b = ((holiday_color >>  0) & 0xFF)
    
    toil_color = color_map[GlobalVal.theme_mode][2]
    toil_color_r = ((toil_color >> 16) & 0xFF)
    toil_color_g = ((toil_color >>  8) & 0xFF)
    toil_color_b = ((toil_color >>  0) & 0xFF)
    
    weekend_color = color_map[GlobalVal.theme_mode][3]
    weekend_color_r = ((weekend_color >> 16) & 0xFF)
    weekend_color_g = ((weekend_color >>  8) & 0xFF)
    weekend_color_b = ((weekend_color >>  0) & 0xFF)
    
    workday_color = color_map[GlobalVal.theme_mode][4]
    workday_color_r = ((workday_color >> 16) & 0xFF)
    workday_color_g = ((workday_color >>  8) & 0xFF)
    workday_color_b = ((workday_color >>  0) & 0xFF)
    
    if date_type == 'today':
        return today_color_r, today_color_g, today_color_b
    elif date_type == 'holiday':
        return holiday_color_r, holiday_color_g, holiday_color_b
    elif date_type == 'toil':
        return(toil_color_r, toil_color_g, toil_color_b)
    elif date_type == 'weekend':
        return weekend_color_r, weekend_color_g, weekend_color_b
    elif date_type == 'workday':
        return workday_color_r, workday_color_g, workday_color_b
    else:
        return 0, 0, 0

def cur_weekday_color():
    choose_weekday_color = color_map[GlobalVal.theme_mode][0]
    choose_weekday_color_r = ((choose_weekday_color >> 16) & 0xFF)
    choose_weekday_color_g = ((choose_weekday_color >>  8) & 0xFF)
    choose_weekday_color_b = ((choose_weekday_color >>  0) & 0xFF)
    return choose_weekday_color_r, choose_weekday_color_g, choose_weekday_color_b

def cur_weather_color():
    choose_weather_color = color_map[GlobalVal.theme_mode][0]
    choose_weather_color_r = ((choose_weather_color >> 16) & 0xFF)
    choose_weather_color_g = ((choose_weather_color >>  8) & 0xFF)
    choose_weather_color_b = ((choose_weather_color >>  0) & 0xFF)
    return choose_weather_color_r, choose_weather_color_g, choose_weather_color_b

def default_color():
    default_color = color_map[GlobalVal.theme_mode][4]
    default_color_r = ((default_color >> 16) & 0xFF)
    default_color_g = ((default_color >>  8) & 0xFF)
    default_color_b = ((default_color >>  0) & 0xFF)
    return default_color_r, default_color_g, default_color_b
    

