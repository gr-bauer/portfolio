import random

# create array to sort
random.seed(42)
array = random.sample(range(0, 100), 8)
print('starting array:', array)

swaps = 1

while swaps > 0:
    swaps = 0

    # iterate through entire array and swap adjacent element if l > r
    for j in range(len(array) - 1):
        if array[j] > array[j + 1]:
            array[j],  array[j + 1] = array[j + 1], array[j]
            swaps += 1

print('sorted array:', array)