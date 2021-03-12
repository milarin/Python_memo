# d = {}
# for i in range(1, 31):
#     if i % 3 == 0:
#         index = f'{i // 3}番目'
#         d[index] = i
# print(f'制作したリスト: {i}')

# h = float(input('身長を入力してください(cm)')) / 100
# w = float(input('体重を入力してくダサい(kg)'))
# bmi = w / h ** 2
# print(bmi)
# print(60 / (170 / 100) ** 2)

# ms = float(input('時速(km/h)を入力してください>')) / 3600
# print(f'秒速 = {ms} m/s')

'''a = input('整数を入力してください') #strで受け取って
x = int(a)
y = int(a*3) #a*3 = aaa つまり 222をintに変換して計算している
print(x + y)'''

# a = int(input('1tume'))
# b = int(input('2tume'))
# if a + b <= 0:
#     print(-(a + b))

'''n = str(input('文字を入力してください'))
count = 0
for _ in n: #n(文字数分処理を行う)
    count += 1
print(count)'''

# n = str(input('文字を入力してください'))
# print(f'{n}の最初の文字:{n[0]}')
# print(f'{n}の最後の文字:{n[-1]}')

# n = input('文字列を入力してください')
# d = {}
# for m in n:
#     if m in d.keys():
#         d[m] += 1
#     else:
#         d[m] = 1
# print(d.keys())

# vowels = {'a', 'e', 'i', 'o', 'u'}
# new = ''
# n = input('test?')
# for i in n:
#     if i in vowels:
#         continue
#     new += i
# print(f'制作した文字: {new}')

# n = input('text?')
# print(n.upper())

# n = input('text?')
# if n[0].islower():
#     print(n.capitalize())
# elif n[0].upper():
#     print(n*2)