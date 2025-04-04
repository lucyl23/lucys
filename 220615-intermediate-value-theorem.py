#勘根定理

def f(x):   
    return x**3-3*x**2+1   #return: 使用f(x)時可得x**3-3*x**2+1，回傳數值

u_bound = float(input('Please input The Upper bound = '))   #上限
l_bound = float(input('Please input The lower bound = '))   #下限
counter = 0  #計算while_loop跑幾次

while (u_bound - l_bound)>0.0001 :
    counter = counter + 1
    
    if f(u_bound)*f(l_bound) == 0  :  #表其中一項為0，就是有一個為函數解
        if f(u_bound) == 0 :
            print('The exact solution = {}'.format(u_bound))
        else :
            print('The exact solution = {}'.format(l_bound))
        break
    elif f(u_bound)*f(l_bound) < 0  :  #小於0: 在上下介必然有實根 
        temp = ( u_bound + l_bound )/2 #中間值
        if f(u_bound)*f(temp)<0 :
            l_bound = temp
        else :  #不然就是大於0
            u_bound = temp
    else:
        u_bound = ( u_bound + l_bound )/2
        
if  abs(f(l_bound))<0.001 :  #abs絕對值
    print('The approximated solution = {}'.format(l_bound))
else :
    print('We cannot find approximated solution so far')  

print('The program has run {} times'.format(counter))
 
#只會找到一個最小的根
