def f1():
    print('Hello')


f1()  # Hello
print(f1)  # <function f1 at 0x000001B5249EA290>
print(id(f1))  # 1877515084432

'''Function Initializing'''


def wish(name):
    print('Good Evening', name)


'''function aliasing'''
greeting = wish

greeting('Arman')  # Good Evening Arman
wish('Durga')  # Good Evening Durga
print(id(greeting))  # 2220298183456
print(id(wish))  # 2220298183456
print(greeting)  # <function wish at 0x00000275897BA320>
print(wish)  # <function wish at 0x00000275897BA320>

'''deleting function name then also we can access function by using alias name'''
del wish
greeting('Arman')  # Good Evening Arman
