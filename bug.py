def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

# Example usage with potential error:
my_list = []
result = calculate_average(my_list)
print(f"Average: {result}")

#Another example with a different type of error:
my_list = [1,2,'a']
result = calculate_average(my_list)
print(f"Average: {result}")