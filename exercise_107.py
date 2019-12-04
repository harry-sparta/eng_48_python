# Write a bizz and zzuu game ##project

# write a program that take a number
# prints back each individual number, but
    # if it is a multiple of 3 it returns bizz
    # if a multiple of 5 it return zzuu
    # if a multiple of 3 and 5 it return bizzzzuu

while True:
    user_num = int(input('Give me a number (-1 to exit):    '))
    if user_num != 0 and user_num%3 and user_num%5 == 0:
        print(user_num)
        print('BIZZZZZZUUUUUUUUUU!')
    elif user_num%5 == 0 and user_num !=0 :
        print(user_num)
        print('ZZUUUUUUUUUUUUUUUU!')
    elif user_num%3 == 0 and user_num !=0 :
        print(user_num)
        print('BIZZZZZZZZZZZZZZZZ!')
    elif user_num == -1:
        print('Thanks! That was a good game of BIZZUU! Bye!')
        break
    else:
        print('That\'s no fun. Let\'s try another number.')