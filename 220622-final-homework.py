import math

def sum_GP(a1,r,n):
    if r==1:
      sum=a1*n
    else:
      sum=(a1(1-r^n ))/(1-r)
    return sum

def print_GP(a1,r,n):
    for i in range (n):
      if i<(n-1):
        print('{} +'.format(a1*r^(n-1)),end='')
      else:
        print('{} ='.format(a1*r^(n-1)),end='')
        print(sum_GP(a1,r,n))

def SolQuadEqu(a,b,c):
    if a==0:
      print('這不是一元二次方程式')
    else:
      if b^2-4*a*c>=0:
        x_1=(-b+math.sqrt(b^2-4*a*c))/2*a
        x_2=(-b-math.sqrt(b^2-4*a*c))
        print('方程式之二根分別為 x_1={},x_2={}'.format(x_1,x_2))

print('1:計算等比級數和')
print('2:計算一元二次方程式之實數解')
print('3:離開程式')
option = ' '

while(option !='3' ):
    option = input('請選擇所需要功能：')
    if option == '1':
        print('計算等比級數 S_n= a +ar + ... + ar^(n-1)')
        a = float(input('請輸入首項 a = '))
        r = float(input('請輸入公比 r = '))
        n = float(input('請輸入項數 n = '))
        S = a*(1-r**n)/(1-r)
        print('等比級數和 S_n={}'.format(S))
      
    elif option =='2':
        print('一元二次方程式：ax^2+bx+c=0') 
        a = float(input('請輸入a = '))
        b = float(input('請輸入b = '))
        c = float(input('請輸入c = '))
        x_1 = (-1*b + math.sqrt(b**2-4*a*c))/(2*a)
        x_2 = (-1*b - math.sqrt(b**2-4*a*c))/(2*a)
        print('方程式之二根分別為 x_1={},x_2={}'.format(x_1,x_2))
    elif option =='3':
        print('歡迎再次使用, bye bye')
        break        
    else:
        print('請輸入正確選項')
