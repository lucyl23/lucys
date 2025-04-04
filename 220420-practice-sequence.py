#數列運算練習

s = 'I am {} {}. {}'.format('Monkey','D','Luffy')
print(s)

sum=0 #總和

for k in range (1,9,1):
  if k<=7:
    print('{}*{} +' .format(2*k-1,3*k-1), end=' ')
  else:
    print('{}*{} =' .format(2*k-1,3*k-1))
  sum=sum+(2*k-1)*(3*k-1)

print(sum)

