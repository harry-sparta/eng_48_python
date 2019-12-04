# Write a bizz and zzuu game ##project

# write a program that take a number
# prints back each individual number, but
    # if it is a multiple of 3 it returns bizz
    # if a multiple of 5 it return zzuu
    # if a multiple of 3 and 5 it return bizzzzuu

# Game codes-------------------------------------------------------------------------------------
import time
user_num = int(input('Give me a max number to stop at:    '))
for counter_num in range(0,user_num):
    time.sleep(0.1)
    print(counter_num)
    time.sleep(0.3)
    if counter_num%3 and counter_num%5 == 0:
        print('BIZZZZZZUUUUUUUUUU!')
    elif counter_num%5 == 0:
        print('ZZUUUUUUUUUUUUUUUU!')
    elif counter_num%3 == 0:
        print('BIZZZZZZZZZZZZZZZZ!')
    else:
        print('...........')
