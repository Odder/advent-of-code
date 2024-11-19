from time import perf_counter
from importlib import import_module


def part1(*dec_args, **dec_kwargs):
    def decorator(func):
        start = perf_counter()
        result = func(*dec_args, **dec_kwargs)
        end = perf_counter()
        print(f'Part 1: {result} in {1000*(end-start):.3f}ms')

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator


def part2(*dec_args, **dec_kwargs):
    def decorator(func):
        start = perf_counter()
        result = func(*dec_args, **dec_kwargs)
        end = perf_counter()
        print(f'Part 2: {result} in {1000*(end-start):.3f}ms')

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator


def part1and2(*dec_args, **dec_kwargs):
    def decorator(func):
        start = perf_counter()
        result1, result2 = func(*dec_args, **dec_kwargs)
        end = perf_counter()
        print(f'Part 1: {result1} in {1000*(end-start):.3f}ms')
        print(f'Part 2: {result2} in 0s')

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator


def part1and2yield(*dec_args, **dec_kwargs):
    def decorator(func):
        gen = func(*dec_args, **dec_kwargs)
        start = perf_counter()
        result = next(gen)
        end = perf_counter()
        print(f'Part 1: {result} in {1000*(end-start):.3f}ms')
        start = perf_counter()
        result = next(gen)
        end = perf_counter()
        print(f'Part 2: {result} in {1000*(end-start):.3f}ms')

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator


def import_mod(module_name):
        imported_module = import_module(module_name)
        print(f"Successfully imported the {module_name} module")
        return imported_module


if __name__ == '__main__':
    day = input('Day: ')

    challenge = import_mod(f'2022.{day}.{day}-concept.main')
    print(challenge)

    print(f'Part 1: {runners["part1"][0]} in {runners["part1"][1]:.3f}ms')
    print(f'Part 2: {runners["part2"][0]} in {runners["part2"][1]:.3f}ms')

