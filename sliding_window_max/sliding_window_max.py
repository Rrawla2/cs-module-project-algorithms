'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

def sliding_window_max(nums, k):
    # Your code here
    # start at index 0, hold the result in a new array
    start = 0
    result = []
    # while k is less than or equal to the length of the array
    # append the max to result, increment start and k to move the window to the right by 1
    while k <= len(nums):
        result.append(max(nums[start:k]))
        start += 1
        k += 1
    # return the new array
    return result

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 2

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
