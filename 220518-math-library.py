import math #引用library函數庫
x,y=10,4
print('as x={}. X的平方根= {}'.format(x,math.sqrt(x)))

print('as x={}. 以2為底， log_2(x) = {}'.format(x,math.log(x,2)))
print('as x={}. 以10為底，log_10(x) = {}'.format(x,math.log(x,10)))
print('as x={}, y={}. x 的 y 次方= {}'.format(x,y,math.pow(x,y)))

print('Pi={}. sin(Pi) = {}'.format(math.pi,math.sin(math.pi)))#注意數值
print('Pi={}. cos(Pi) = {}'.format(math.pi,math.cos(math.pi)))

print('x={}, y={}.則x,y的最大公因數 (x,y)={}'.format(x,y,math.gcd(x,y)))

print('as x={},y={}. x! = {}, y! = {}'.format(x,y,math.factorial(x),math.factorial(y)))
print('as x={},y={}. the combination of C(x,y)={}'.format(x,y,math.comb(x,y)))
print('as x={},y={}. the permutation of P(x,y)={}'.format(x,y,math.comb(x,y)*math.factorial(y)))

print('as x={}, y={}.則x,y的最小公倍數 [x,y]={}'.format(x,y,math.lcm(x,y)))
