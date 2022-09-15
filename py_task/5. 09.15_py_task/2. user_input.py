def user_input():
    cnt = 0
    while cnt < 5:
        num = input()
        if num.isdigit():
            print(int(num) * 2)
            cnt += 1
        else:
            if num == 'exit':
                cnt = 5
                continue
            print(f'입력한 문자는 {num}입니다.')
    return

user_input()