def add_positive_numbers(x, y):
    assert x > 0 and y > 0 #Both numbers must be positive
    return x + y

add_positive_numbers(1, 1) #Works
add_positive_numbers(1,-1) #Results in Assertion Error

def eat_junk(food):
    assert food in ["pizza", "ice cream", "candy", "fried butter"], "food must be a junk food!"
    return f"NOM NOM NOM I am eating {food}"

food = input("Enter a food please: ")
print(eat_junk(food))