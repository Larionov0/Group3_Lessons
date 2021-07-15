def helloer():
    print('Hello world! :)')


def triangle():
    for i in range(1, 6):
        print('*' * i)


def my_func(other_function, n):
    for x in range(n):
        other_function()


my_func(helloer, 5)
my_func(triangle, 6)
