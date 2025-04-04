#作業-如何判定質數-2
#0504的作業：1、2、3無法判定，負數會錯誤

while 1:
  print()
  print('請輸入一正數')
  n=int(input())
  vn=int(n**0.5)+1
  if n>3:
    for k in range(2,vn,1):
      if n%k==0:
        print('{} 為合數'.format(n))
        break
      elif k==vn-1:
        print('{} 為質數'.format(n))
  elif n>1:
    print(str(n)+'為質數')
  else:
    print(str(n)+'不為質數也不為合數')
    
