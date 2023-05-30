# of all subarrays of size K

# Function to find the sum of
# all subarrays of size K
def calcSum(arr, n, k):
    # Initialize sum = 0
    sum = 0

    # Consider first subarray of size k
    # Store the sum of elements
    for i in range(k):
        sum += arr[i]

    # Print the current sum
    print(sum, end=" ")

    # Consider every subarray of size k
    # Remove first element and add current
    # element to the window
    for i in range(k, n):
        # Add the element which enters
        # into the window and subtract
        # the element which pops out from
        # the window of the size K
        sum = (sum - arr[i - k]) + arr[i]

        # Print the sum of subarray
        print(sum, end=" ")


# Drivers Code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    n = len(arr)
    k = 3

    # Function Call
    calcSum(arr, n, k)
