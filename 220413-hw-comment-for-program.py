#為程式寫註解

print('請輸入帳號')
#print類似C++裡的cout，input類似C++裡的cin
Account = input()
#Account=輸入的東西，若無用int()在框起來，為字串；若有，則為數字，可用於計算。
print('請輸入密碼')
Password = input()
if (Account == 'mlsh') and (Password=='123456'):
    print('登入成功')

elif (Account == 'mlsh') and (Password!='123456'):
    print('密碼錯誤，請重新輸入密碼')
    Password=input()
    if(Password=='123456'):
        print('登入成功，密碼輸入錯誤 1 次')
    else:
        print('登入失敗，密碼輸入錯誤 2 次')
else:
    print('帳號不存在，請重新輸入帳號')
    Account = input()
    print('請輸入密碼')
    Password = input()
    if(Account == 'mlsh') and (Password=='123456'):
        print('登入成功,帳號輸入錯誤 1 次')
    elif (Account != 'mlsh'):
        print('登入失敗，帳號輸入錯誤 2 次')
    else:
        print('錯誤次數過多，登入失敗')

'''
如果輸入的帳號account等於mlsh且密碼password等於123456(字串)
則螢幕會顯示：登入成功

如果輸入的帳號account等於mlsh且密碼password不等於123456(字串)
螢幕顯示：密碼錯誤，請重新輸入密碼
之後會請你再次輸入密碼password
密碼password等於123456顯示：登入成功，密碼輸入錯誤 1 次
密碼password不等於123456則顯示：登入失敗，密碼輸入錯誤 2 次

如果輸入的帳號account不等於mlsh且密碼password不等於123456(字串)
螢幕顯示：帳號不存在，請重新輸入帳號
重新輸入的帳號密碼後，若帳號account等於mlsh且密碼password等於123456(字串)
則螢幕顯示：登入成功,帳號輸入錯誤 1 次
若帳號account不等於mlsh
螢幕顯示：登入失敗，帳號輸入錯誤 2 次
若帳號account等於mlsh但密碼password不等於123456
螢幕顯示：錯誤次數過多，登入失敗
'''
