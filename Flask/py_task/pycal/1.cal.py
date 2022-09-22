import sys
from calmain import *

if __name__ == "__main__":
    print('num (input : +, -, *, %, /) num : ', end='')
    temp = sys.stdin.readline().split()
    print(cal(temp))