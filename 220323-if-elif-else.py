#if-elif-else應用

print('How old are you? ')
year=int(input())

if year<6 or year>=65:
  print('票種: Free')
elif year>=6 and year<18:
  print('票種: 半票')

#elif year>18 and year<65:
else:
  print('票種: 全票')

print('輸入成績')
score=int(input())

if score>=60 and score<=100:
  print('Congratulation! You are safe. ')
elif score>=40 and score<60:
  print('還有救，可以補考')
elif score<40 and score>=0:
  print('死當')
else:
  print('錯誤')
  
