# functional-python
[![License:MIT](https://img.shields.io/packagist/l/doctrine/orm.svg)](https://opensource.org/licenses/MIT)

This repo helps you in learning functional reactive python. This contains gist of every concepts and also their resources for reference.

## Why? 
Refer my document on [functional programming in scala](https://github.com/iamshreeram/scala-starter/blob/master/README.md#1-functional-reactive-programming)

## How to approach?
1. Use immutable data structures 
2. Understand `collections` module from `python3`
3. How to do transformation with `Map, Filter and Reduce` 
4. Understand `asyncio` module for reactive programming
5. Learn `generators`, `yield` and `await`

## Cheat sheet
1. `namedtuple` : Instead of `tuples`, use `namedtuple`. Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code. They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of position index.

    ```python3
    from collections import namedtuple
    Student = namedtuple('Student', 'fname last_name score')
    s1 = Student('James', 'Mathew', '90')
    print(s1.fname)
    print(s1[0])
    print(s1.score)
    ```
	
2. `Map` :  Map helps in applying any function / list of functions to entire list 

	```python3
	from math import sin, cos, tan, pi
	def map_functions(x, functions):
		 return [ func(x) for func in functions ]
		 
	family_of_functions = (sin, cos, tan)
	print(map_functions(pi, family_of_functions))

	```

3. `Reduce` : This is inside `functools`. This reduces the sequence of values to single value. Helps in aggregation of the list.
	```
	from functools import reduce
	reduce(lambda x, y: x+y, range(1,101))
	```

4. `Filter` : Instead of creating a conditional for loop with `for():  if():` condition or
    Instead of creating list comprehension `[x for i in X if X.value = True]` 
    Go with `tuple(filter(func, <iterator object>))`

5. `multiprocessing` : To utilize multiple cores of CPU. This module create a `pool` and 
    run `map` or `filter` or any operation from pools. This has multiple options to define the 
    the pool size and number of CPU to be used
6. `concurrent.futures` : This is similar to `multiprocessing` module. But, We can switch the 
    execution method between `ThreadPoolExecutor` and `ProcessPoolExecutor`. This has few other 
    advantages over other different methods of parallelism
7. `asyncio` : This removes the overhead of having multiple thread / process. Asyncio provides event 
    loop to track different I/O events. This helps in removing over head of context switches