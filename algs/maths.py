from functools import reduce
from operator import mul

def prod(numbers):
    return reduce(mul, numbers)

