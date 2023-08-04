def generate_n_number(n):
    i = 1
    while i <= n:
        yield i
        i += 1


g = generate_n_number(10)
list1 = list(g)
print(list1)