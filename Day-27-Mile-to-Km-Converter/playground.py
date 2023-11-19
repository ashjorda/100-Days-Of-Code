def add(*args):
    product = 0
    for n in args:
        product += n
    return product


print(add(10, 10, 15, 18, 32, 45, 76, 10))