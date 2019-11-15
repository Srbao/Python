#file=open('C:/Users/admin/Desktop/text.txt','w')
#file.write("hello")
'''
def text_create(name,msg):
    desktop_path = 'C:/Users/admin/Desktop/'
    full_pash    =  desktop_path + name + '.py'
    file = open (full_pash,'w')
    file.write(msg)
    file.close()
    print('Done')

text_create('hello','hello world')
'''

password_list = ['*#*#','12345']    #创建列表，用于存储用户初始密码和其他数据
def accuont_login():                #函数定义
    password = input('Password:')   #使用input获取用户输入的字符串并存储在变量password中
    password_correct = password == password_list[-1] 
    password_reset = password == password_list[0]
    if password_correct:
        print('Login success')
    elif password_reset:
        new_password = input('Enter a new password:')
        password_list.append(new_password) #添加新元素自动的排列到列表的尾部
        print('Your password has changed successfully!')
        accuont_login()
    else:
        print('wrong password or invalid input!')
        accuont_login()
accuont_login()


