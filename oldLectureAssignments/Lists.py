from unicodedata import lookup

# Lists are Mutable

# Using the example of playing cards
chinese_cards = ['coin', 'string', 'myriad']  # A list literal
suits = chinese_cards  # Two names refer to the same list

# Cards migrated to europe, only suit of coins remained in Spanish decks
print(suits.pop())  # Remove and return final element
suits.remove('string')  # Remove the first element that equals the argument

# Three more suits were added
suits.append('cup')  # Add an element to the end
suits.extend(['sword', 'club'])  # Add all elements of a sequence to the end

# Italians called the swords, spades
suits[2] = 'spade'  # Replace an element

# These were the suits of a traditional Italian deck of cards
print(suits)

# The french variant used today in the U.S. changes the first two suits:
suits[0:2] = ['heart', 'diamond']  # Replace a slice
print(suits)

# Methods also exist for inserting, sorting, and reversing lists, they change the value, and do not create new list objects

nest = list(suits)  # Bind "nest" to a second list with the same elements
nest[0] = suits     # Create a nested list

suits.insert(2, 'Joker')  # Insert an element at index 2, shifting the rest
print(nest)

print(nest[0].pop(2))
print(suits)

print(suits is nest[0])                                # True, suits and nest[0] are the same object
print(suits is ['heart', 'diamond', 'spade', 'club'])  # False, this is a new list object and is not the same object as suits
print(suits == ['heart', 'diamond', 'spade', 'club'])  # True, suits stores the same values as this new list

# Fun method to get unicode
symbols = [lookup('WHITE ' + s.upper() + ' SUIT') for s in suits]
print(symbols)
