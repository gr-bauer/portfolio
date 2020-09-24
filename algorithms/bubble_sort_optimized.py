import random

# create array to sort
random.seed(42)
array = random.sample(range(0, 100), 8)
print('starting array:', array)

# loop over each element to get all elements in correct place
for i in range(len(array)):
    swapped = False
    
    # put the next largest element into place
    for j in range(len(array) - i -1):

        # swap adjacent elements if unordered
        if array[j] > array[j + 1]:
            array[j],  array[j + 1] = array[j + 1], array[j]
            swapped = True

    if swapped == False:
            break

print('sorted array:', array)