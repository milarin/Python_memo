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
#
# a = 'Osakana'
# for i in a:
#     print(i)
# for s in range(len(a)):
#     print(a[s])

# list = [1, 2, 3]
# print(list)
# list.append(4)
# print(list)

# list = []
# for i in range(5):
#     list.append(i)
# print(list)

# list = [1, 2, 3, 4]
# list.insert(1, 100)
# print(list)

# l1 = [1,2,3]
# l2 = [4, 5, 6]
# l1.extend(l2)
# print(l1)

# l = [100, 1, 2, 3, 100]
# l.remove(100)
# print(l)

# list = [i for i in range(5)]
# print(list)

# list = [i for i in range(100) if i % 2 == 0]
# print(list)
#
# t = (1, 2, 3, 4) # タプルは中身の変更はできないよ
# print(t[0])

# t = (1, 2)
# one, two = t #アンパックという こうやってタプルリストを取り出す
# print(one, two)

# t1 = (1, 2)
# t2 = (3, 4)
# t1 = t1 + t2
# print(t1)  # (1, 2, 3, 4) 全く新しいタプルが作られる

# d = {'apple': 400, 'banana': 342, 'peach': 150}
# print(d['apple'])
# print(d.keys())
# print(d)
# for key in d.keys():
#     print(key)
# for value in d.values():
#     print(value)
# for key, value in d.items():
#     print(key, value)

# a = {1, 2, 3, 4, 5}
# b = {2, 4, 5, 8, 10}
# print(a)
# print(type(a))

# def f(x):
#     return x + 3
# print(f(2))
# def get_full_name(first, name):
#     return first + ' ' + name
#
#
# r = get_full_name('佐藤', '太郎')
# print(r)
#
# get_full_name_v2 = lambda name, first: first + ' ' + name
# r2 = get_full_name_v2('aaa', 'bbb')
# print(r2)

# def f(x):
#     if x % 2 == 0:
#         return x
#     else:
#         return '2で割り切れません'
#
#
# r = f(2)
# print(r)
#
#
# f2 = lambda x: x if x % 2 == 0 else '2で割り切れません'
# r2 = f2(3)
# print(r2)


# add_num = lambda a, b: a + b
# try:
#     r = add_num(1, '2')
# except TypeError as e:
#     print(e)
#     print('例外処理が出ました')
# else:  # tyrで処理が実行できたときに処理される
#     print(r)
# finally:  # tryで処理の実行結果にかかわらず処理される
#     print('おわおわり・D・エース')


# class Child():
#     def say_hello(self):
#         print('hello!!')
#
#
# Child().say_hello()

# class Child():
#     def __init__(self, name):
#         print('これは初期化メソッドです')
#         print(self)
#         self.name = name
#         print('My name is', self.name)
#
#     def say_hello(self):
#         print('say_helloメソッドです')
#         print('My name is', self.name)
#
#
# child = Child('Taro')
# child2 = Child('Ore')
# child.say_hello()


# class Child():
#     def say_hello(self):
#         print('Childクラスのsay_helloメソッドです')
#
#
# class JapaneseChild(Child):
#     def say_ohayou(self):
#         print('JapaneseChildクラスのsay_ohayouメソッドです')
#
# japanese_child = JapaneseChild()
# japanese_child.say_hello()
# japanese_child.say_ohayou()

# import seaborn as sns  # as の後ろは監修的につける名前が決まっている
#
# iris = sns.load_dataset('iris')
# sns.pairplot(iris)

# word1 = input('text1')
# word2 = input('text2')
#
# l = ''
# for i in word1:
#     if i in word2 and i not in l:
#         l += i
#
# print(l)

# word = input('テキストを入力してください')
# count = 0
# for i in word:
#     count += 1
# index = count // 2
# if index % 2 == 0:
#     word = word[:index] + '@' + word[index:]
# else:
#     word = word[:index] + '@' + word[index+1:]
#
# print(f'変換した文字：{word}')

# l = [i for i in range(6)]
# count = 0
# for i in l:
#     count += i
# print(count)
# print(sum(l))

# l = [i for i in range(12)]
# max_value = 0
# for _ in l:
#     if _ >max_value:
#         max_value = _
# print(max_value)
# print(max(l))
#
# l = [1, 2, 2, 2, 3, 4]
# print(set(l))

# l = ['Python', 'JavaScript', 'PHP', 'Ruby']
# w = l[0]
# count = 0
# for i in l:
#     count += 1
#     if len(i) <= len(w):
#         w = l[count-1]
# print(w)

# l = ['Python', 'JavaScript', 'PHP', 'Ruby']
# new = sorted(l, key=len)
# print(new)


# l1 = ['Python', 'JavaScript', 'PHP', 'Ruby']
# l2 = ['Jave', 'Ruby', 'Golang', 'Python', 'Type']
#
# list = set(l1) & set(l2)
# print(list)

# l = [i for i in range(11)]
# print(l[::2])


# l = ['1', 2, '3', 4.0, '5', 6, '7', 8.0, '9', 10]
# new = []
# for i in l:
#     if isinstance(i, int):
#         new.append(i)
#
# print(new)

# l = [[i for i in range(1, 6)], [i for i in range(6, 10)]]
# new = [i for row in l for i in row]
# print(new)
# list = [i for i in range(100)]
# print(list)

# l = [1]
# if l:
#     print(l)
# else:
#     print('からです')

# l1 = [1, 2, 3, 4, 5]
# l2 = [10, 9, 8, 7 ,6]
# result = [i * j for i, j in zip(l1, l2)]
# print(result)

# l = [1, '22', 3, '444', 0.0, '5']
# new = [i for i in l if isinstance(i, int)]
# print(max(new))
# print(min(new))

# l = [0, '1', 3, 2, '4', 5, '7']
# new = [v for i, v in enumerate(l) if i == int(v)]
# print(new)

# l = [1, 2, 3, '4', 5]
#
# if any([v for v in l if isinstance(v, str)]):
#     print('文字列が入っています')
# else:
#     print('文字列は入っていません')

# l = [1, 2, 3, 4, 5, 6, 7, 8]
# new = []
# for i in l:
#     new.append('list')
#     new.append(i)
# print(new)
# for i in range(0, len(l * 2), 2):
#     l.insert(i, 'list')
# print(l)

# l = ['Python', 'Java', 1, 'Python2', 'Java2', 2]
# count = 0
# for i in l:
#     if 'Python' in str(i):
#         l.pop(count)
#     count += 1
# print(l)
# for i in l:
#     if 'Python' in str(i):
#         l.remove(i)
# print(l)
telephone_numbers = [
    '080-0000-0000',
    '090-1111-1111',
    '090-2222-2222',
    '080-3333-3333'
]
new = [i for i in telephone_numbers if '080' == i[:3]]
print(new)