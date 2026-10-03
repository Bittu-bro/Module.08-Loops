import random




# print(random.random()) #.    random) - it's return float value between 0.0 to 1.0. (1.0 is excluded)


# #random.randint(... , ...)
# print(random.randint(10, 20))


# #choice(sequence)  => return a random items from Sequence

# nums = [3,4,8,7,2,6,9]
# print(random.choice(nums))

fruits = ['apple','banana', 'orenge', 'popaya']
print(random.choice(fruits))
# shuffle(sequence) => returns the elements shuffled in random order
random.shuffle(fruits)
print(fruits)