# 1 1 2 3 5 8 13
def fibo():
    first = 1
    second = 1
    third = 2
    print(first)
    print(second)
    for i in range(1, 10):
        third = first + second
        print(third)
        first = second
        second = third

fibo()