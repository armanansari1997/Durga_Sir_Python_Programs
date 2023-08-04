def hello_world(outer):
    def inner():
        outer()
        return "Hello World !!!!!"
    return inner


def hello_indore(outer):
    def inner():
        outer()
        return "Hello Indore !!!!!"
    return inner


@hello_world
@hello_indore
def hello_india():
    return "Hello India !!!"


# print(hello_india())
# res = hello_world(hello_india)
# out = res()
# print(res)
# print(out)

res = hello_india()
print(res)
