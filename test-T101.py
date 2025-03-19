#need a code to get a largest number in a array
def largest_number(numbers):
    
    #Finds and returns the largest number in a given array.
    
    # Parameters:
    # numbers (list): A list of numerical values.

    # Returns:
    # int/float: The largest number in the array.

    largest = numbers[0]  # Initialize with the first element
    for num in numbers:
        if num > largest:
            largest = num
    return largest

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(largest_number(numbers))
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"The largest number is: {largest_number(arr)}")
