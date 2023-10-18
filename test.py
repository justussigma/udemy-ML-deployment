from collections import Counter

# Your list of lists
data = [[1, 2, 2, 3, 4, 4],
        [2, 2, 3, 3, 3, 4],
        [4, 4, 4, 4, 4, 4]]

# Initialize a Counter to count the numbers
number_counter = Counter()

# Iterate through the sublists and update the counter
for sublist in data:
    number_counter.update(sublist)

# Find the most common number and its count across all sublists
most_common_number, count = number_counter.most_common(1)[0]

# Display the result
print(f"The most common number across all sublists is {most_common_number}, which appears {count} times.")

