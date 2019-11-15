'''songslist = ['Holy','Thund','Rebel']
for song in songslist:
    if song == 'Holy':
        print(song,'-Dio')
    elif song=='Thund':
        print(song,'-AC/DC')
    elif song =='Rebel':
        print(song,'-David Bowie')'''

#for 循环
'''for i in range(1,10):
    for j in range(1,10):
        print('{}x{}={}'.format(i,j,i*j))'''

#while 循环
'''count = 0
while True:
    print('Repeat this line !')
    count = count + 1
    if count == 5:
        break'''

password_list = ['***','12345']
def account_login():
    tries = 3
    while tries > 0:
        password = input('Password:')
        password_correct = password == password_list [-1]
        password_reset = password == password_list[0]

        if password_correct:
            print('success!')
        elif password_reset:
            new_password = input ('Enter an new password :')
            password_list.append(new_password)
            print('change success')
            account_login()
        else:
            print('Wrond ')
            tries = tries - 1
            print(tries,'times left')
    else:
        print('Your account has been suspended')
account_login()

