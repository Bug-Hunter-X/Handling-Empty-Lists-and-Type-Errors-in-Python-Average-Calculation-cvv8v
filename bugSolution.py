def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    try:
        #Check if all elements are numbers before proceeding
        if all(isinstance(num, (int, float)) for num in numbers):
            return sum(numbers) / len(numbers)
        else:
            return "Error: List contains Non-numeric values"
    except TypeError as e:
        return f"Error: {e}"

# Example usage
my_list = []
result = calculate_average(my_list)
print(f"Average: {result}")

my_list = [1, 2, 3, 4, 5]
result = calculate_average(my_list)
print(f"Average: {result}")

my_list = [1, 2, 'a']
result = calculate_average(my_list)
print(f"Average: {result}") 