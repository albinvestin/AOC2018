# AOC2018
## Advent Of Code 2018

Solving the advent of code while learning Python. 

## Python self notes:

### Libraries:
numpy: use for array such as 2 or 3 dimensional:
```python
import numpy as np
```
Useful methods: where(), any(), size()

parse: external library from https://pypi.org/project/parse/ 
Inverse of .format(), useful for reading formatted input:

```python
  import parse
  extract_id = parse.parse('Guard #{id:d}{}', action)
  id = extract_id['id']
```
### Data structures:
* () tuple : ordered, unchangable, duplicates
* [] list : ordered, changeable, duplicates
* {} set : unordered, unindexed, no duplicates
* {:} dictionary : unordered, changeable, indexed

### Iterators, generators and comprehension:
Anonymous function:
```python
  lambda arg: expression
```

Iterables:
list, string etc. Pythonic way of iterate: 
```python
  for character in string:
    print(character)
  for element in list:
    print(element)
  for number in range(3)
    print(number)
  for index, value in enumerate(list)
    print(index, value)
```

List comprehension:
Small compact way of generating list, set, strings etc.: 
```python
  executable_nodes = [node for node in executable_nodes if node not in in_progress]
  finished_timers = [index for index, value in enumerate(completion_timers) if value == time]
  LETTERS = {letter : value for value, letter in enumerate(ascii_lowercase, start=1)}
```

Generators with any() or all():
When checking any() by creating a generator from list comprehension the function terminates as soon it hits a True value, hence it is very efficient. Do not use "[]" when using the any() or all() method since in Python 3 the list is generated on the fly.
```python
  any(user.is_cool() for user in users if is_prime(user.id))
  all(dependency in completed_nodes for dependency in current_node.prev_dependencies)
```

Generators:
Iterable you can only iterate over once. Generators do not store all values in memeory, they generate the values on the fly:
```python
  my_generator = (x*x fir x in range(3))
```

Yield:
Is a keyword used like return except it will return a generator. The code it return does not run until used:
```python
  for i in my_generator:
    print(i)
```
It is hany when your function will return a huge set of values that you only need to read once.
