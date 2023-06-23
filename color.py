#color theme file

#color[0] stand holiday, color[1] stand TOIL, color[3] stand normal weekend, color[4] stand normal working day, 
color = [0 for i in range(4)]
color[0] = 0x000005
color[1] = 0x050000
color[2] = 0x000500
color[3] = 0x050200

def cur_month_color():
    choose_month_color = color[3]
    choose_month_color_r = ((choose_month_color >> 16) & 0xFF)
    choose_month_color_g = ((choose_month_color >>  8) & 0xFF)
    choose_month_color_b = ((choose_month_color >>  0) & 0xFF)
    return choose_month_color_r, choose_month_color_g, choose_month_color_b

def cur_date_color():
    today_color = color[3]
    today_color_r = ((today_color >> 16) & 0xFF)
    today_color_g = ((today_color >>  8) & 0xFF)
    today_color_b = ((today_color >>  0) & 0xFF)
    return today_color_r, today_color_g, today_color_b

def date_type_color(date_type):
    holiday_color = color[0]
    holiday_color_r = ((holiday_color >> 16) & 0xFF)
    holiday_color_g = ((holiday_color >>  8) & 0xFF)
    holiday_color_b = ((holiday_color >>  0) & 0xFF)
    
    toil_color = color[1]
    toil_color_r = ((toil_color >> 16) & 0xFF)
    toil_color_g = ((toil_color >>  8) & 0xFF)
    toil_color_b = ((toil_color >>  0) & 0xFF)
    
    weekend_color = color[2]
    weekend_color_r = ((weekend_color >> 16) & 0xFF)
    weekend_color_g = ((weekend_color >>  8) & 0xFF)
    weekend_color_b = ((weekend_color >>  0) & 0xFF)
    
    workday_color = color[3]
    workday_color_r = ((workday_color >> 16) & 0xFF)
    workday_color_g = ((workday_color >>  8) & 0xFF)
    workday_color_b = ((workday_color >>  0) & 0xFF)
    
    if date_type == 'holiday':
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
    choose_weekday_color = color[3]
    choose_weekday_color_r = ((choose_weekday_color >> 16) & 0xFF)
    choose_weekday_color_g = ((choose_weekday_color >>  8) & 0xFF)
    choose_weekday_color_b = ((choose_weekday_color >>  0) & 0xFF)
    return choose_weekday_color_r, choose_weekday_color_g, choose_weekday_color_b
    

