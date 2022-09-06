import math
from collections import deque

def cal(num_list:list) -> float:
    result = 0
    num_list = deque(num_list)
    if num_list[1] == '+':
        return float(num_list[0]) + float(num_list[2])
    elif num_list[1] == '-':
        return float(num_list[0]) - float(num_list[2])
    elif num_list[1] == '*':
        return float(num_list[0]) * float(num_list[2])
    elif num_list[1] == '/':
        return float(num_list[0]) / float(num_list[2])
    elif num_list[1] == '%':
        return float(num_list[0]) % float(num_list[2])


    return result