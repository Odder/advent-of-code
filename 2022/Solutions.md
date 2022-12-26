# Advent of Code 2022 debrief

## Day 1: Calorie Counting

Introduction to reading from stdin and printing to stdout.

### Time-space complexity analysis:

* n: data entries
* g: groups
* k: top k groups to identify (for part 1: 1, for part 2: 3)

### Part 1

Identify the highest sum within a list of lists.

#### Approach 1: map and sum

```python
# Python
inp = [[1, 2, 3], [4, 5], [6]]
print(max(map(sum, inp)))  # prints 9
```

Time complexity: O(n)<br>
Space complexity: O(n)

#### Approach 2: memorise best score

```python
# Python
inp = [[1, 2, 3], [4, 5], [6]]
best = -10**10
for group in inp:
    best = max(best, sum(group))
print(best)  # prints 9
```

Time complexity: O(n)<br>
Space complexity: O(1)

### Part 2

Identify the 3 highest sums within a list of lists.

#### Approach 1: sum, sort, sum

```python
# Python
inp = [[1, 2, 3], [4, 5], [6]]
sums = map(sum, inp)
sorted_sums = sorted(sums, reverse=True)
print(sum(sorted_sums[:3]))  # prints sum of top 3
```

Time complexity: O(glog g)<br>
Space complexity: O(g)

#### Approach 2: min-heaps

The idea here is that by using a min-heap we always keep track of the lowest number in O(n time with)

```
# Pseudo-code
inp = [[1, 2, 3], [4, 5], [6]]
top_k = MinHeap()

for group in inp:
    cals = sum(group)
    top_k.push(cals)
    if top_k.length > n:
        top_k.pop()
print(sum(top_k))  # prints sum of top 3
```

Time complexity: O(glog g)<br>
Space complexity: O(k)

## Day 2: Rock Paper Scissors

Introduction to data parsing and scoring of solutions

### Time-space complexity analysis:

* n: data entries
* k: number of possible selections per match (3 for both parts)

### Part 1

Sum up the outcomes of the games by using a scoring-system defined by the elves

#### Approach 1: Naïve mapping

```python
# Python
inp = ['A Y', 'B X']
outcomes = {'A X': 4, 'A Y': 8, ...}
score = sum(outcomes[match] in match for match in inp)
print(score)
```

Time complexity: O(n)<br>
Space complexity: O(k<sup>2</sup>)

#### Approach 2: ord and mod

By using ord and subtracting 65 from ABC  and 88 from XYZ we get all the options in the shape of 0, 1 and 2.

```python
# Python
inp = [(ord('A') - 65, ord('Y') - 88), (ord('B') - 65, ord('X') - 88)]
score = 0
for him, you in inp:
    outcome = (you + 4 - him) % 3
    score += you + 1 + outcome*3
```

Time complexity: O(n)<br>
Space complexity: O(1)

### Part 2

Trivial by applying minor tweaks to how you calculate scoring to part 1

## Day 3: Rucksack Reorganization

Finding the only character in common between k number of strings

### Time-space complexity analysis:

* n: data entries
* m: m length of strings to compare
* k: number of strings to compare

### Part 1

Identify the only character that the first and second part of each line has in common

#### Approach 1: Set intersections

```python
# Python
bags = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL']
def score(char):
    c = ord(char)
    return c - 38 if c < 95 else c - 96

total_score = 0
for bag in bags:
    size = len(bag)
    in_common = set(bag[:size]) & set(bag[size:])
    total_score += score(in_common.pop())
```

Time complexity: O(nlog k)<br>
Space complexity: O(m)

#### Approach 1: 

```python
# Python
bags = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL']
def score(char):
    c = ord(char)
    return c - 38 if c < 95 else c - 96

total_score = 0
for bag in bags:
    size = len(bag)
    in_common = set(bag[:size]) & set(bag[size:])
    total_score += score(in_common.pop())
```

Time complexity: O(nlog k)<br>
Space complexity: O(m)

### Part 2

Identify the only character that 3 strings have in common

#### Approach 1: Set intersections

```python
# Python
groups = [['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', ...], [...]]
def score(char):
    c = ord(char)
    return c - 38 if c < 95 else c - 96

total_score = 0
for bags in groups:
    bag1, bag2, bag3 = bags
    in_common = set(bag1) & set(bag2) & set(bag3)
    total_score += score(in_common.pop())
```

Time complexity: O(nlog k)<br>
Space complexity: O(m)



