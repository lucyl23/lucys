#作業-如何判定質數-1

print('請輸入一數')
n=int(input())
vn=int(n**0.5)+1

for k in range(2,vn,1):
  if n%k==0:
    print(str(n)+'不為質數')
    break  
  elif k==vn-1:
    print(str(n)+'為質數')

