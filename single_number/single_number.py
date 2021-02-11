'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # Outer loop keeps track of the count for each number
    for i in range(len(arr)):
        count = 0
        # Inner loop adds to the count for each item
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        # if the count has a remainder it returns that index
        if count % 2 != 0:
            return arr[i]

    return -1


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")