#數列運算列式

r=range(0,10,1)
print(list(r))

for i in range(10):
  print(i, end=' ')

# end=' '是讓數字列一整行，若無，則會變一數字一行
  
for k in range(1,16,1):
  print(str(k)+'+',end='')

for k in range(1,16,1):
  if k<15 :
    print( str(k)+'+',end='')
  else:
    print( str(k) + '=')

for k in range(1,16,2):
  if k<15: 
    print( str(k)+'**2 +',end=' ')
  else:
    print( str(k) + '**2 =')


for k in range(1,16,2):
  if k<14 :
    print(str(k)+'*'+str(k+2)+' + ', end='')
  else:
    print(str(k)+'*'+str(k+2)+'=')
    
