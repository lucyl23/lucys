#判斷質數-老師版

import math
print('1:判斷質數')
print('0:結束程式')
n=''
while n!='0':
  n=input('請選取所需功能：')
  if n=='1':  
    x=int(input(' 請輸入一正整數：'))
    if x==2 or x==3:
      print('  {} 是質數'.format(x))
    else:
      r=-1
      divisor=2
      test=1+int((math.sqrt(x)))
      while(divisor<test):
        r=x%divisor
        if r==0:
          print('  {} 不是質數，{}可以被{}整除'.format(x,x,divisor))
          break
        divisor=divisor+1
        if divisor==test:
          print('  {} 是質數'.format(x))
  elif n=='0':
    print(' 程式結束')
  else:
    print(' 輸入錯誤，請重新輸入')
    
  
