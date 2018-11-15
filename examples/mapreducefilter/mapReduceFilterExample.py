# Map Example :
greetings = ('hello', 'how are you', 'goodbye')

def add_world(word):
    return word + ', world'

# map takes a list, tuple, etc. and applies your specificed function to each
# element and returns an iterator of the changed elements 
fixed = map(add_world, greetings)

# you either need to convert the map object into a list/tuple
# or iterate over the elements in a loop
for greeting in fixed:
    print(greeting)

'''
Output :
hello, world
how are you, world
goodbye, world
'''


# Reduce Example :
import functools # required for the reduce function

separate_words = ('man','bear','pig')

def word_glue(word1, word2):
    return word1 + word2 

# reduce takes a list/tuple and a function and returns a single
# value that results from that function
connected = functools.reduce(word_glue, separate_words)

print('\n' + connected + '\n')

'''
Output : 

manbearpig

'''


# Filter Example :
groceries = ('banana', 'apple', 'chainsaw', 'pepper', 'Old Hickory Mesquite Applewood Barbeque Sauce')

def fruity(item):
    fruit = ('apple', 'banana', 'orange', 'lemon', 'melon')
    if item.lower() in fruit:
        return True

# filter takes a list/tuple and a function that tests for a condition,
# and returns an iterable of items that returned True for that condition
fruit_groceries = filter(fruity, groceries)

for fruit in fruit_groceries:
    print(fruit)

'''
Output :
banana
apple
'''
