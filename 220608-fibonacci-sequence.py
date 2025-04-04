#費氏數列

f = [1,1]

n = 10

for k in range(n):
    f.append(f[k+1] + f[k]) #append:把數字加在list的後方

print(f)

for k in range(n):
    print('f[{}] = {}'.format(k,f[k]))
    
for k in range(n):
    print('ratio = {}'.format(f[k+1]/f[k]))
    
