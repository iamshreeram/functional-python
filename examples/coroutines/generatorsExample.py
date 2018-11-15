# Example 1 :
def simple_gen():
    # If there is yield statement, the function becomes generator
    yield "Hello"
    yield "World"

gen = simple_gen()
print(next(gen))
print(next(gen))

'''
Output : 
Hello
World
'''

# Example 2 :
def generate_nums():
    num = 0
    while True:
        yield num
        num = num + 1
nums = generate_nums()
for x in nums:
    print(x)
    if x > 9:
        break