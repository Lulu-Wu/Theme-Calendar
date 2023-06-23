def coordinate_map(x, y):
    if x >= 0 and x < 10 and y >= 0 and y < 7:
        if (x % 2) == 0:  
            point = x * 7 + y
        else:
            point = (x + 1) * 7 - (y + 1)
    else:
        point = -1
    return point