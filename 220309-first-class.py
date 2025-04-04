x='hello world'
print (x)
print('what is your name')
Name = 'Tom'
# Name = Tom
Name = input()
# input 像c++的 cin ，接收
# print == cout

#print('Nice to meet you')
#print(Name)
#上面兩行可以等於下面一行，加法等於數學的加法
print('Nice to meet you ' + Name)
#HW: 計算圓錐體積，使用者輸入半徑(r)、高(h)，輸出體機(v)
# v=1/3(P*r*r)h 常數P=3.14...
print('輸入半徑r')
r = input()
print('輸入高h')
h = input()
p = 3.14
v = 1/3*p*(r*r)*h
# r*r = r**2
print('體積為 '+v )

#str() 設定誇號內數字為實數，才可以和字串一同出現，str(v)，print才會出現東西
#int(input())
#沒有int時，輸入數字皆為實數(str)，加上int後就變成了整數(數字)，才可以進行運算
