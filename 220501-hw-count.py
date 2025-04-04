#作業-算數

sum=0
for k in range(2,11,1):
  if k <10:
    print('{}^{} +' .format(k,15-k), end=' ')
  else:
    print('{}^{} =' .format(k,15-k))
  
  sum=sum+k**(15-k)
  
print(sum)

