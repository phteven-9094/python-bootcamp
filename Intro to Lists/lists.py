#Creating Lists
#Key Syntax is [" ", " ", " "]
demo_list = ["a", 1, 45, True, 6.777]
#Check for amount of items in a list
len(demo_list)
#Another way to make a list
tasks = list(range(0 , 4))

#Accessing Values in a List
friends = ["Ashley", "Matt", "Michael"]
print(friends[0])

#Iterating Over Lists
numbers = [1, 2, 4 ,5]
for num in numbers:
    print(num)

numbers = [1, 2, 4, 5]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
    
sounds = ['super', 'cali', 'fragil', 'istic', 'expi', 'ali', 'docious']
result = ''
for s in sounds:
    result += s.upper()

#List Methods: Append, Insert, and Extend
#Append = Add an item to the end of the list
first_list = [1, 2, 3, 4, 5]
first_list.append(5)
print(first_list)

#Extend: Add to the end of a list all values passed to extend
second_list = [6, 7, 8, 9]
second_list.extend([10, 11, 12])
print(second_list)

#Insert: Insert an item at a given position
third_list = [13, 14, 15]
third_list.insert(2, 'Hi!')
#First argument is the index to insert at, 2nd argument is what you want to insert