import random

# create array to sort
random.seed(42)
array = random.sample(range(0, 100), 8)
print('starting array:', array)

for i in range(len(array)):
    idx_of_minimum = i

    # find smallest element in remaining unsorted array    
    for j in range(i + 1, len(array)):
        if array[idx_of_minimum] > array[j]:
            idx_of_minimum = j

    # swap element with new found smallest element 
    array[i], array[idx_of_minimum] = array[idx_of_minimum], array[i]

print('sorted array:', array)