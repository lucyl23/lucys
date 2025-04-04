import math

print('1:計算一元二次方程式之實數解')
print('2:計算等比級數和')
print('3:離開程式')

option = ''  #option為一空字串(定義)

while(option !='3' ):   #執行直到option不等於3
    option = input('請選擇所需要功能：')
    
    if option =='1':
            print('一元二次方程式：ax^2+bx+c=0') 
            a = float(input('請輸入a = '))
            b = float(input('請輸入b = '))
            c = float(input('請輸入c = '))
            x_1 = (-1*b + math.sqrt(b**2-4*a*c))/(2*a)
            x_2 = (-1*b - math.sqrt(b**2-4*a*c))/(2*a)
            print('方程式之二根分別為 x_1={},x_2={}'.format(x_1,x_2))
    elif option == '2':
            print('計算等比級數 S_n= a + ar + ar^2 + ... + ar^(n-1)')
            a = float(input('請輸入首項 a = '))
            r = float(input('請輸入公比 r = '))
            n = float(input('請輸入項數 n = '))
            S = a*(1-r**n)/(1-r)
            print('等比級數和 S_n={}'.format(S))
    elif option =='3':
            print('歡迎再次使用, bye bye')  

    else:   #除了以上三種情形以外的就會顯示這個
        print('請輸入正確選項')
      
