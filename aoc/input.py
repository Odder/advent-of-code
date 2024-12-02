"""
This module gives you a collection of tools to parse input from an input file.
"""
from re import findall


def lines(file='input'):
    """
    return a generator that iterates over every line of a file while removing EOL markers.
    no parsing is going on and every line will be returned as a string

    input:
    ```txt
    hello
    world
    !
    ```

    example:
    ```python
    for line in lines():
        print(f'"{line}"')
    ```
    output:
    ```txt
    "hello"
    "world"
    "!"
    ```
    """
    with open(file, 'r') as f:
        for line in f:
            yield line.strip()

def grouped_lines(file='input'):
    group = []
    for line in lines():
        if not line:
            yield group
            group = []
        group.append(line)
    yield group


def tokens(modifier=str, file='input'):
    """
    return a generator that iterates over every line of a file and 
    splits every every line into a list of tokens split by spaces.

    input:
    ```txt
    1 2 3
    2 3 4
    3 4 5
    ```

    example:
    ```python
    for line in tokens():
        print(list(line))
    ```
    output:
    ```txt
    ['1', '2', '3']
    ['2', '3', '4']
    ['3', '4', '5']
    ```

    You can use `modifier` to pass in a function to type cast every token.

    example:
    ```python
    for line in tokens(modifier=int):
        print(sum(line))
    ```
    output:
    ```txt
    6
    9
    12
    ```
    """
    return ((modifier(x) for x in line.split()) for line in lines(file=file))


def tokens_filter(modifier=str, regex=' ', file='input'):
    return ((modifier(x) for x in findall(regex, line)) for line in lines(file=file))


def tokens_pattern(regex=' ', file='input'):
    return (findall(regex, line)[0] for line in lines(file=file))


def tokens_split(modifier=str, splitter=' ', file='input'):
    return ([modifier(x) for x in line.split(splitter)] for line in lines(file=file))


def ints(file='input'):
    """
    return a generator that parses every line as a single integer

    input:
    ```txt
    1
    2
    3
    4
    5
    ```

    example:
    ```python
    print(sum(ints))
    ```
    output:
    ```txt
    15
    ```
    """
    return (int(line) if line else None for line in lines(file=file))
