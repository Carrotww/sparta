import sys
import random
import time
from typing import List
from datetime import datetime
from datetime import timedelta

def config_num(): # configuration 3 ~ 10 number
    print('자릿수 정하기 3 ~ 10 사이 수를 입력해 주세요 : ')
    while 1:
        num = input()
        if not num.isdigit():
            print('숫자를 입력해 주세요.')
            continue
        elif int(num) > 2 and int(num) < 10:
            break
        else:
            print('3 ~ 10의 수를 입력해 주세요.')
    return num

def gen_ran_num(num: int) -> List:
    temp = [i for i in range(10)]
    answer_list = random.sample(temp, int(num))
    return answer_list

if __name__ == '__main__':
    now = datetime.now()
    game_digit = config_num()
    answer_list = gen_ran_num(game_digit)
    print(answer_list)

    cnt = 1
    exit = True
    start = time.time()
    while 1:
        print(f'정답 {game_digit}자릿수를 입력해 주세요. ex) num num num')
        while 1:
            # player_input = list(map(int, sys.stdin.readline().split()))
            temp = sys.stdin.readline().split()
            if temp[0] == 'exit':
                break
            player_input = list(map(int, temp))
            if len(player_input) == int(game_digit):
                break
            else:
                print('자릿수를 확인해 주세요.')
        if temp[0] == 'exit':
            break

        strike, ball = 0, 0
        for i in range(int(game_digit)):
            if player_input[i] == answer_list[i]:
                strike += 1
            elif player_input[i] in answer_list:
                ball += 1
        if strike == int(game_digit):
            end = time.time()
            sec = end - start
            result_list = str(timedelta(seconds=sec)).split(".")
            break
        cnt += 1
        print(f'{strike}S {ball}B')
    if temp[0] == 'exit':
        print('게임을 종료합니다.')
    else:
        print('승리!!')
        print(f'{cnt}번 만에 맞추셨으며, {result_list[0]} 소요. 현재 시간 :',now.strftime('%Y-%m-%d %H:%M:%S'))
    