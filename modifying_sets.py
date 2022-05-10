# numbers = {*""} # fastest way to create an empty set
# numbers = {*{}} # also fast
numbers = set()  # usual way

print(numbers, type(numbers))
# numbers.add(1)
# print(numbers)

# while len(numbers) < 4:
#     next_value = int(input("Please enter your next value: "))
#     numbers.add(next_value)
# print(numbers)  # THE CODE KEEPS LOOPING
# until 4 UNIQUE values have been entered!!!
# sets can only contain unique values
data = ["blue", "red", "blue", "green", "red", "blue", "white"]
# Create a set of the list to remove duplicates:
unique_data = sorted(set(data))  # returns a list out of the set
print(unique_data)

# Create a list of unique colors keeping the order that they appeared
unique_data = list(dict.fromkeys(data))  # insertion order preserved
# (initial order) - adding the same key a second time does nothing
print(unique_data)

print(dict.fromkeys(data))