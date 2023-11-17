# Simple syntax that lets you create lists from lists
# Syntax:
# [variable to be created for iterable item in list/range/something interable]
# Example:
nums = [1, 2, 3]
[x * 10 for x in nums]

name = "colt"
[char.upper() for char in name]

friends = ["Ashley", "Matt", "Michael"]
[friend.capitalize() for friend in friends]

[num * 10 for num in range(1, 6)]

# List Comprehension with Conditional Logic
numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]

[num*2 if num % 2 == 0 else num/2 for num in numbers]

with_vowels = "This is so much fun!"
''.join(char for char in with_vowels if char not in "aeiou")
