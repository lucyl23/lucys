#判斷來電，a[0:2]代表a的前兩個數字，len(a)代表a的數字長度


print('輸入電話')
a=input()
if a[0:2]=='02' and len(a)==10:
  print('此號碼為市話來電')
elif a[0:2]=='09' and len(a)==10:
  print('此號碼為手機來電')
else:
  print('此號碼為未知來電')
