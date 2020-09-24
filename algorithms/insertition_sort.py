import random

# create array to sort
random.seed(42)
array = random.sample(range(0, 100), 8)
print('starting array:', array)

# iterate through unsorted part of array from l->r
for i in range(1, len(array)):
    j = i - 1           # define start of sorted array
    to_sort = array[i]  # define element to sort

    # iterate through sorted part of array from r->l
    # figure out where in sorted portion element should go
    while j >= 0 and to_sort < array[j]:
        array[j + 1] = array[j]
        j -= 1

    # insert element into sorted portion of array
    array[j + 1] = to_sort

print('sorted array:', array)