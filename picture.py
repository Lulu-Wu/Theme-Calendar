number_list = [[0 for i in range(15)] for j in range(10)]   #10为数字1-9,15为占用3*5的空间
number_list[0] = [1,1,1,1,0,1,1,0,1,1,0,1,1,1,1]
number_list[1] = [0,1,0,1,1,0,0,1,0,0,1,0,1,1,1]
number_list[2] = [1,1,1,0,0,1,1,1,1,1,0,0,1,1,1]
number_list[3] = [1,1,1,0,0,1,1,1,1,0,0,1,1,1,1]
number_list[4] = [1,0,1,1,0,1,1,1,1,0,0,1,0,0,1]
number_list[5] = [1,1,1,1,0,0,1,1,1,0,0,1,1,1,1]
number_list[6] = [1,1,1,1,0,0,1,1,1,1,0,1,1,1,1]
number_list[7] = [1,1,1,0,0,1,0,0,1,0,0,1,0,0,1]
number_list[8] = [1,1,1,1,0,1,1,1,1,1,0,1,1,1,1]
number_list[9] = [1,1,1,1,0,1,1,1,1,0,0,1,1,1,1]
def number(num):
    global number_list
    return(number_list[num])