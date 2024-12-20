def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case gracefully
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
result = calculate_average(my_empty_list) # This will return 0
print(f"The average is: {result}")

my_list_with_zero = [10,0,20,30]
result = calculate_average(my_list_with_zero)
print(f"The average is: {result}")
