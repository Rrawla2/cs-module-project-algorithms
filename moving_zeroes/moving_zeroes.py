'''
Input: a List of integers
Returns: a List of integers
'''
# Write a function that takes an array of integers and moves each non-zero integer to the left side of the array,
# then returns the altered array. The order of the non-zero integers does not matter in the mutated array.

def moving_zeroes(arr):
    # Your code here
    # set a count to keep track of items that are not zero
    count = 0
    # check if the integer is not equal to 0
    # then increase count
    for item in range(len(arr)):
        if arr[item] != 0:
            arr[count] = arr[item]
            count += 1
    # while the count is less than the length of the array
    # set the array[count] to index 0 then increase the count
    while count < len(arr):
        arr[count] = 0
        count += 1
    # return the array
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")