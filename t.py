# chara = 'word'
# for c, i in enumerate(chara):
#     print(f'{c}買い目 {i}')

# nums = [2, 4, 6, 8]
# for i in nums:
#     if i % 2 == 1:
#         break
#     else:
#         print('奇数の値を含めてください')
# n = 0
# while n < 3:
#     print(n)
#     n += 1
# else:
#     print('しゅうりょう')

# def has_book(items):
#     for item in items:
#         if 'book' in item:
#             print('Found')
#             break
#     else:
#         print('Not Found')
#
# has_book(['book'])

# def print_content(content='content'):
#     return print(content)
# #
# # print_content('hinako')
# # hinako = print_content
# # hinako('hinakoooo')
#
# def print_title(printer, title):
#     printer(title.upper())
#
# print_title(print_content, 'Python')

# def increment(num):
#     return num + 1
# f = increment(1)
# print(f)

# def no_value():
#     return
# print(no_value())

# def print_page(one, two, three):
#     print(one)
#     print(two)
#     print(three)
#
# contents = ['my content', 'content2', 'content3']
# #
# # print_page(*contents)
#
# def print_page(*args):
#     print('init')
#     for i in args:
#         print(i)
#
# print_page(*contents)

class Page:
    def __init__(self, num, content, section=None):
        self.num = num
        self.content = content
        self.section = section

    def output(self):
        return f'{self.content}'


# # print(Page)
# title_page = Page(0, 'Python book')
# print(title_page)
# print(title_page.output())
# print(title_page.section)
#
# first_page = Page(1, 'first page', 1)
# print(first_page)
# print(first_page.output())
# print(first_page.section)

class Klass:
    def __new__(cls, *args, **kwargs):
        print(f'{cls=}')
        print('new', args)
        return super().__new__(cls)

    def __init__(self, *args):
        print('init', args)


kls = Klass('aaa', 'asd', 'sdg')
# print(kls)
