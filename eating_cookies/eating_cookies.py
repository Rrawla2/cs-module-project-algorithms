'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    # This is the base case
    if n < 0:
        return 0
    if n == 0:
        return 1

    # Tribonacci sequence
    cookies = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    return cookies


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    # num_cookies = 5
    # num_cookies = 3
    # num_cookies = 10
    # num_cookies = 60 - crashed my IDE

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
