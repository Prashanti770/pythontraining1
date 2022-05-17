"""
def add(a,b):
    c=a+b
    print("add",c)
add(20,7)
"""
"""
def mul(a,b):
    c=a*b
    print("mul",c)
mul(20,7)
"""
"""
def my_func(a,b=1):
    c = a * b
    print("mul", c)
my_func(10)
"""

# def my_func(a=6,b):
#     c = a * b
#     print("mul", c)
# my_func(10)


def my_func(b):
    return 4*b
print(my_func(10))
print(my_func(20))
print(my_func(10))