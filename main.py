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
# telephone_numbers = [
#     '080-0000-0000',
#     '090-1111-1111',
#     '090-2222-2222',
#     '080-3333-3333'
# ]
# new = [i for i in telephone_numbers if '080' == i[:3]]
# print(new)
#
# t1 = (1, 2, 3)
# t2 = ([1, 2, 3])
# print(type(t1))
# print(t2)
#
# t = (1,)
# print(type(t))

# t = (i for i in range(4))
# print(t)

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new = [tuple(l[i:i+3]) for i in range(0, 9, 3)]
# print(new)

# l = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# for i, row in enumerate(l, start=1):
#     a, b, c = row
#     print(a, b, c)
#
# t = (1, '2', 3, '4', 5, '6', 7, '8', 9)
# new_t = tuple(reversed(t))
# print(new_t)

# t = (1, '2', 3, '4', 5)
# str_t = tuple(str(i) for i in t)
# int_t = int(''.join(str_t)) # int同志のjoinはできない
# print(int_t)

# t = (1, [2, 3], '4', (5, 6, 7), '8', (9, 10))
# count = 0
# for i in t:
#     if isinstance(i, tuple):
#         count +=1
# print(count)
# t_in_tuple = [i for i in t if isinstance(i, tuple)] # やってることは同じだけどリスト化して数えたら早い
# print(len(t_in_tuple))

# t = (1, [2, 3], '4', (5, 6, 7), None, (9, 10))
# new_t = []
# for i in t:
#     if isinstance(i, tuple):
#         new_t.append(i)
#     elif isinstance(i, list):
#         new_t.append(tuple(i))
#     else:
#         new_t.append((i, ))
# print(new_t)
# l = [1, 2, 3]
# print(set(l))
# print(set())

# l1 = [1, 2, 3, 4, 5]
# l2 = [7, 6, 5, 4]
# # l3 = l1 + l2
# # print(set(l3))
# l3 = set(l1) | set(l2)
# print(l3)

# l1 = [1, 2, 3, 4, 5]
# l2 = [7, 6, 5, 4]
# l3 = set(l1) - set(l2)
# l4 = set(l1) ^ set(l2)
# l5 = set(l1) | set(l2)
# print(l3)
# print(l4)
# print(l5)

# l1 = [1, 2, 3, 4, 5]
# l2 = [3, 4, 5]
# l3 = set(l1) <= set(l2)
# l4 = set(l1) >= set(l2)
# print(l3)
# print(l4)

# d1 = {'A': 111, 'B': 222, 'C': 333}
# d2 = {}
# print(d1)
# print(d2)
# # d1['D'] = 444
# d1.update({'D': 444})
# print(d1)

# d1 = {'A': 111, 'B': 222, 'C': 333}
# d2 = {'D': 444, 'E': 555}
# d3 = {'F': 666}
# new_d = {}
# # for i in [d1, d2, d3]:
# #     new_d.update(i)
# # print(new_d)
# print({**d1, **d2, **d3})

# d1 = {'A': 111, 'B': 222, 'C': 333}
# print('A' in d1)
# print(d1.keys())  # こっちは古い　キーだけの存在確認なら上の方法
# print('444' in d1.values())

# keys = ['A', 'B', 'C']
# value = [111, 222, 333]
# d1 = dict(zip(keys, value))
# print(d1)

# d = {'A': 111, 'B': 222, 'C': 333}
# new_d = {k: v for k, v in d.items() if v > 150}  # key,valueを取り出したい場合はitems()を使う
# print(new_d)

# d = {'A': 111, 'B': 222, 'C': 333}
# l = ['B', 'C', 'D', 'A']
# for k in l:
#     print({d.get(k)})

# d = {'B': 222, 'A': 111, 'D':444, 'C': 333}
# d2 = sorted(d.items(), key=lambda x:x[1])
# print(d2)

# m, p, q = 10, 31, 52
# first = (1 - p / 100) * m
# second = (1 - q / 100) * first
# print(second)
# l = [
#     {'id': 10000,
#      'feature': {'name': 'Michael',
#                  'height': 180.3,
#                  'weight': 63.7,
#                  'skills': {
#                      'IT': ['Python', 'Golang', 'SQL'],
#                      'Others': ['Chinese', 'Math']
#                  }
#                  }
#      },
#     {'id': 10001,
#      'feature': {'name': 'Nancy',
#                  'height': 156.7,
#                  'weight': 39.7,
#                  'skills': {
#                      'IT': ['Java', 'SQL', 'JavaScript'],
#                      'Others': ['Accounting']
#                  }
#                  }
#      }
# ]

#  リストは数字で取り出し、辞書型は名前で取り出す
# print(l[0]['feature']['skills']['Others'][0])
#
# it_skills = [d['feature']['skills']['IT'] for d in l]
# michael_skill, nancy_skill = it_skills
# common_skill = set(michael_skill) & set(nancy_skill)
# print(common_skill)

# d = {'B': 222, 'A': 111, 'D': 444, 'C': 333}
# print(max(d.values()))
# print(min(d))

# item = {}
# if item == {}:
#     print('からの辞書です')
# else:
#     print(item)

# d = {'B': 222, 'A': 111, 'D': 444, 'C': 333}
# new_d = d.copy()
# for k, v in d.items():
#     if v % 2 != 0:
#         # forのループ処理中に中身を増減(削除追加)をするのはだめだから一回別の要素を作る必要がある
#         del new_d[k]
# print(new_d)
#
# for k, v in {**d}.items():
#     if v % 2 != 0:
#         del d[k]
#
# # new_d = {k: v for k, v in d.items() if v % 2 == 0}
# print(d)

# l = [False, True, False, False, True]
# print(len(l) - sum(l))
# # Falseは0 Trueは1 になるよ

# l = [False, True, False, False, True]
# new_l = [int(i) for i in l]
# print(new_l)

# a = 4
# if not (a == 3 or a == 7):
#     print(f'{a}は3でも7でもありません')

# l = [1, 0, [], (2, 3), 'AA', '', False, '*3']
# true_count = sum([bool(i) for i in l])
# print(true_count)

# x = False
# print(1 if x else 100)

# l = [1, 2, None, 3]
# for i in l:
#     if i is None:
#         print(10000)
#     else:
#         print(i)

# l = [1, 2, None, False, '3', '4', None, True]
# count = 0
# for i in l:
#     if i is None or i is True:
#         count += 1
# print(count)
# print(len([i for i in l if i is None or i is True]))  # 上のを1行で書く

# import  random
#
# d = {0: 'グー', 1: 'チョキ', 2: 'パー'}
# options = tuple(d.keys())
# print(options)
# my_option = 11
# is_win = False
# print('*****************')
# print(f'選択肢：{d}')
# print('*****************')
# while my_option not in options:
#     my_option = input('自分の出す手を入力してください(整数 : 0, 1, 2) >')
#     com_option = random.choice(options)
#     try:
#         my_option = int(my_option)
#     except:
#         print('整数の0, 1, 2から入力してください')
# if my_option == com_option:
#     is_win = 'あいこ'
# elif my_option == 0 and com_option == 2:
#     is_win = True
# elif my_option == 1 and com_option == 0:
#     is_win = True
# elif my_option == 2 and com_option == 1:
#     is_win = True
#
# if isinstance(is_win, bool):
#     is_win = '勝ち' if is_win else '負け'
# print(f'自分が選んだ数字： {d[my_option]}')
# print(f'CPが選んだ数字： {d[com_option]}')
# print(f'結果： {is_win}')


# import random
#
# d = {0: 'グー', 1: 'チョキ', 2: 'パー'}
# options = tuple(d.keys())
# pc_hand = random.choice(options)
# my_hand = 11
# is_win = False
# while my_hand not in options:
#     my_hand = input(f'数字を選択してください: {d} >')
#     try:
#         my_hand = int(my_hand)
#     except:
#         print('整数0, 1, 2から選んでください')
# print(f'自分の出した手: {d[my_hand]}')
# print(f'コンピュータの出した手：{d[pc_hand]}')
# if my_hand == pc_hand:
#     is_win = 'あいこ'
# elif my_hand == 0 and pc_hand == 1:
#     is_win = True
# elif my_hand == 1 and pc_hand == 2:
#     is_win = True
# elif my_hand == 2 and pc_hand == 0:
#     is_win = True
#
# if isinstance(is_win, bool):
#     is_win = '勝ち' if True else '負け'
#
# print(f'結果: {is_win}')


# print(7 + 3)
# print(7 - 3)
# print(7 * 3)
# print(7 % 3)
# print(7 / 3)
# n = input('すきな文字を入力してね')
# print(n)
# print(10 ** 10 ** 2)
# for i in range(31):
#     if i % 3 == 0:
#         print(i)

# print([i for i in range(1,31) if i % 3 == 0])

# l = [i for i in range(1, 31) if i % 3 == 0 and '3' in str(i)]
# print(l)
# kg = float(input('taijuu'))
# m = float(input('sinntyou')) / 100
# bmi = kg / (m ** 2)
# print(bmi)

# a = input('整数を入力してください>') # str型で受け取って aaa をつくる
# print(int(a) + int(a*3))

# count = 0
# n = str(input('文字を入力してください'))
# for i in n:
#     count += 1
# print(count)

# n = str(input('文字を入力してください'))
# print(f'{n[0]}, {n[-1]}')

# n = str(input('文字を入力してください'))
# d = {}
# for s in n:
#     if s in d.keys():
#         d[s] += 1
#     else:
#         d[s] = 1
# print(d)

# import collections
# count = collections.Counter(n)
# print(count)

# n = str(input('文字を入力してください'))
# # print(n.upper())
#
# # 回答と違うやり方
# if n == n.capitalize():
#     print(n*2)
# else:
#     print(n.capitalize())

# v = ['a', 'i', 'u', 'e', 'o']
# n = input('文字を入力してください')
# new = ''
# for i in n:
#     if i in v:
#         continue
#     new += i
# print(new)

# f = input('1つ目の文字を入力してください')
# s = input('2つ目の文字を入力してください')
# new = ''
# # 少しコード量が多いやり方
# # for i in f:
# #     for t in s:
# #         if i == t and not i in new:
# #             new += i
# #         else:
# #             continue
#
# # コードが短い方のやり方  文字列はリテラブルなので、わざわざ2回目のforを書かなくていい
# # for i in f:
# #     if i in s and not i in new:
# #         new += i
# print(new)

# f = input('1つ目の文字を入力してください').split()  # splitした時点でリスト化されるから[]で囲わなくていい
# s = input('2つ目の文字を入力してください').split()
# print(f)
# new = [i for i in f if i in s]  # 内包表記はできない？？？
# # for i in f:
# # #     if i in s and not i in new:
# # #         new.append(i)
#
# print(new)

# n = input('文字を入力してください')
# count = 0
# for i in n:
#     count += 1
# index = count // 2
# if count % 2 == 0:
#     new = n[:index] + '@' + n[index:]
# else:
#     new = n[:index] + '@' + n[index + 1:]
# print(new)
#
# f = input('1つ目の文字を入力してください')
# s = input('2つ目の文字を入力してください')
# t = input('3つ目の文字を入力してください')
#
# l = [f, s, t]
# l.sort()
# print(' '.join(l))

# l = [1, 2, 3, 4, 5]
# count = 0
# for _ in l:
#     count += _
# print(count)
# print(sum(l))

# l = [1, 5, 3, 2, 4]
# ma = 0 # 不確定な0を入れるよりl[0]とした方がいい
# for i in l:
#     if i > ma:
#         ma = i
# print(ma)
# print(max(l))

# l = [1, 2, 2, 2, 3, 3, 3, 4, 5]
# print(list(set(l))) # set()は辞書配列になる

# l = ['Python', 'Ruby', 'PHP', 'JavaScript']
# min_len = len(l[0])
# word = l[0]
# for i in l:
#     if int(len(i)) < min_len:
#         word = i
# print(word)

# l = ['Python', 'Ruby', 'PHP', 'JavaScript']
# print(sorted(l, key=len))

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(l[::2])

# l = ['1', 2, '3', 4.0, '5', 6, '7', 8.0, '9', 10]
# new = []
# for i in l:
#     if isinstance(i, int):
#         new.append(i)
# print(new)

# l = [[i for i in range(1, 6)], [j for j in range(6, 11)]]
# print(l)

# l = [[i for i in range(1, 6)], [j for j in range(6, 11)]] # l = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
# new = [j for i in l for j in i]
# print(new)

# l = [] # 空だとFalse,あるとTrue
# if not l: # 空の時
#     print('arisutoha karadesu')
# else: # 空ではない時
#     print(l)

# l1 = [1, 2, 3, 4, 5]
# l2 = [10, 9, 8, 7, 6]
# new = []
# for i, j in zip(l1, l2):
#     new.append(i * j)
# print(new)
# new_1 = [i * j for i, j in zip(l1, l2)]
# print(new_1)

# l = [1, '22', 3, '444', 0.0, '5']
# m = [i for i in l if isinstance(i, int)]
# print(max(m))
# print(min(m))

# a = 95367 + 3000 * 2 + 300 * 93
# print(a - 54000)

# l = [0, '1', 3, 2, '4', 5, '7']
# new = []
# for count, i in enumerate(l):
#     if count == int(i):
#         new.append(i)
# new_l = [i for count, i in enumerate(l) if count == int(i)]
# print(new)
# print(new_l)

# l = [1, 2, 3, 3]
# if len(set(l)) < len(l):
#     print('重複しています')
# else:
#     print('重複はありません')

# l = [1, 'aaa', 2, 'bbb', 'ddd', 4, 3, 'ccc']
# l_int = sorted([i for i in l if isinstance(i, int)])
# l_str = sorted([i for i in l if isinstance(i, str)])
# new = l_int + l_str
# print(new)

# l = [1, 2, 3, 4, '5']
# if [i for i in l if isinstance(i, str)]:
#     print('ari')
# else:
#     print('nasi')

# l = [1, 2, 3, 4, 5]
# for i in range(0, len(l)*2, 2):
#     l.insert(i, 'list')
#
# print(l)

# l = ['Python1', 'Java', 'Python2', 'Java2', 2]
# for i in l:
#     if 'Python' in str(i):
#         l.remove(i)  # remove()は最初の要素を探して削除する pop()はintしか受け付けない
# print(l)

# l = [1, 3, 2, 3, 4, 6, 5, 8, 7]
# for c, i in enumerate(l):
#     if c % 3 == 0 and i % 3 == 0:
#         l.pop(i)  # pop()はstrを引数に取れない
# print(l)

# l = [
#     '080-0800-0000',
#     '090-0000-0000',
#     '080-0900-0800',
# ]
# for i in l:
#     if '080-' not in i:
#         l.remove(i)
# print(l)
# new = [i for i in l if '080' in i[:3]]
# print(new)
# new_l = [i for i in l if '080' == i[:3]]
# print(new_l)
#
# l = [
#     '080-0800-0000',
#     '090-0000-0000',
#     '080-0900-0800',
#     '09-0909-0000',
# ]
# new = [i for i in l if i[3] == '-']
# print(new)
# new_l = [s for s in l if s.find('-') == 3]
# print(new_l)

# l1 = [4, 9, 6, 2]
# l2 = [3, 5, 7]
# l3 = [1, 9, 7]
# # new = [sum(i) / len(i) for i in [l1, l2, l3]]
# # print(new)
# l = [l1, l2, l3]
# sorted_l = sorted(l, key=lambda v: max(v) / len(v), reverse=True)
# print(sorted_l[0])
#
# t = 1, 2, 3
# l = [1, 2, 3]
# print(t)
# print(tuple(l))

# t = 1,
# print(t)
# print(type(t))

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# t = tuple([l[i:i+3] for i in range(0, len(l), 3)])
# print(t)
# for c, i in enumerate(t, start=1):
#     x, y, z = i
#     print(f'{c}行目： {x} {y} {z}')

# t = 1, '2', 3, '4', 5, '6', 7, '8', 9
# new = tuple(reversed(t))
# print(new)

# t = 1, '2', 3, '4', 5
# str_l = [str(i) for i in t]
# new = int(''.join(str_l))
# print(new)

# t = (1, [2, 3], '4', (5, 6, 7), '8', (9, 10))
# new = [i for i in t if isinstance(i, tuple)]
# print(len(new))

# t = (1, [2, 3], '4', (5, 6, 7), None, (9, 10))
# new = []
# for i in t:
#     if isinstance(i, tuple):
#         new.append(i)
#     elif isinstance(i, list):
#         new.append(tuple(i))
#     else:
#         new.append((i, ))
# print(tuple(new))

# print(set())
# print({1, 2, 3})
# print({1, 2, 2, 3, 3, 4, 4, 4})

# l1 = [1, 2, 3, 4, 5]
# l2 = [7, 6, 5, 4]
# l3 = [3, 4, 5]
# l1 = set(l1)
# l2 = set(l2)
# l3 = set(l3)
# print(l1 | l2)
# print(l1 - l2)
# print(l1 ^ l2)
# print(l1 >= l3)
# print(l1 <= l3)

# d = {'A': 111, 'B': 222, 'C': 333}
# d2 = {}
# print(d, d2, type(d), type(d2))
# # d['D'] = 444
# d.update({'D': 444})
# print(d)

# d1 = {'A': 111, 'B': 222, 'C': 333}
# d2 = {'D': 444, 'E': 555}
# d3 = {'F': 666}
# # new_d = {}
# # for i in [d1, d2, d3]:
# #     new_d.update(i)
# new_d1 = {**d1, **d2, **d3}
# print(new_d1)

# d = {'A': 111, 'B': 222, 'C': 333}
# print('A' in d)
# print('A' in d.keys())  # どちらでも正解。keys()を使わなくてもデフォルトでkeyを参照してくれる
# print(444 in d.values())  # valueを参照する場合はvalue()を書く

# keys = ['A', 'B', 'C']
# values = [111, 222, 333]
# new = {}
# # for key, value in zip(keys, values):
# #     new[key] = value
# new_d = {key: value for key, value in zip(keys, values)}
# print(new_d)

# d = {'A': 111, 'B': 222, 'C': 333}
# new = {k: v for k, v in d.items() if v >= 150}
# print(new)

# d = {'A': 111, 'B': 222, 'C': 333}
# l = ['B', 'C', 'D', 'E']
# for k in l:
#     print(f'{k}に対応するvalue： {d.get(k)}')

# d = {'B': 222, 'A': 111, 'D': 444, 'C': 333}
# new = dict(sorted(d.items()))
# # new = dict(sorted(d.items(), key=lambda x:x[0]))
# print(new)

# l = [
#     {'id': 10000,
#      'feature': {'name': 'Michael',
#                  'height': 180.3,
#                  'weight': 63.7,
#                  'skills': {
#                      'IT': ['Python', 'Golang', 'SQL'],
#                      'Others': ['Chinese', 'Math']
#                  }
#                  }
#      },
#     {'id': 10001,
#      'feature': {'name': 'Nancy',
#                  'height': 156.7,
#                  'weight': 39.7,
#                  'skills': {
#                      'IT': ['Java', 'SQL', 'JavaScript'],
#                      'Others': ['Accounting']
#                  }
#                  }
#      }
# ]
# print(l[0]['feature']['skills']['Others'][0])
# it_skill = [d['feature']['skills']['IT'] for d in l]
# m, n = it_skill
# print(set(m) & set(n))

# d = {'B': 222, 'A': 111, 'C': 333, 'D': 444}
# max_value = d['B']
# for v in d.values():
#     if v > max_value:
#         max_value = v
# print(max_value)
# max_value_1 = max(d.values())  # 1行で書けるで
# print(max_value_1)
# min_key = min(d.keys(), key=lambda k: d[k])
# print(min_key)

# d = {'S': 322}
# l = []
#
# if d:
#     print(d)
# else:
#     print('空です')

# d = {'B': 222, 'A': 111, 'C': 333, 'D': 444}
# # new = {k: v for k, v in d.items() if v % 2 == 0}
# # print(new)
# new = d.copy()
# for k, v in d.items():
#     if v % 2 != 0:
#         del new[k]
# print(new)

# l = [False, False, False, True, True]
# false_count = len(l) - sum(l)
# print(false_count)
# new = [int(f) for f in l]
# print(new)

# a = 3
# if a != 3 and a != 7:
#     print(f'{a}は3でも7でもありません')
# if not (a == 3 or a == 7):
#     print(f'{a}は3でも7でもありません')

# l = [1, 0, [], (2, 3), 'AA', '', False, '' * 3]
# new = [i for i in l if i]
# print(new)  # True の要素をlから集めてる
# print(len(new))
# is_true_count = sum([bool(i) for i in l])  # [True, False, False, True, True, False, False, False]
# print(is_true_count)
# print([bool(i) for i in l])

# x = False
# print(1 if x else 100)

# l = [1, 2, None, 3]
# for i in l:
#     if i is None:
#         print(10000)
#     else:
#         print(i)

# l = [1, 2, None, False, '3', '4', None, True]
# is_true_or_none = len([i for i in l if i is None or i is True])
# print(is_true_or_none)
# print([i for i in l if i is None or i is True])
aaaa
