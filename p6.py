#fibanocci series
def fib_series():
    first_num = 0
    sec_num = 1
    while first_num < 5:
        value = first_num
        first_num, sec_num = sec_num, first_num+sec_num
        yield value


genrtor1 = fib_series()
print(next(genrtor1))
print(next(genrtor1))
print(next(genrtor1))
print(next(genrtor1))

