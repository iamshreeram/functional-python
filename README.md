# functional-python
This repo helps you in learning functional reactive python. This contains gist of every concepts and also their resources for reference.

## Why? 
Refer my document on "functional programming in scala"

## How to approach
1. Use immutable data structures 
2. Understand `collections` module from `python3`
3. How to do transformation with `Map, Filter and Reduce` 
 
## Cheat sheet
1. Instead of `dictionary`, use `namedtuple`
2. `Filter` : Instead of creating a conditional for loop with `for():  if():` condition or
    Instead of creating list comprehension `[x for i in X if X.value = True]` 
    Go with `tuple(filter(func, <iterator object>))`
3. `Map` :  This is similar to `filter`. Only difference is, Instead conditional for loop, 
    map helps in applying any function to entire list 
4. `Reduce` : This is inside `functools`. This reduces the sequence of values to single value.
5. `multiprocessing` : To utilize multiple cores of CPU. This module create a `pool` and 
    run `map` or `filter` or any operation from pools. This has multiple options to define the 
    the pool size and number of CPU to be used
6. `concurrent.futures` : This is similar to `multiprocessing` module. But, We can switch the 
    execution method between `ThreadPoolExecutor` and `ProcessPoolExecutor`. This has few other 
    advantages over other different methods of parallelism
