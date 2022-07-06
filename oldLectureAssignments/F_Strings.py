# Normal string concatenation

artist = "Lil Nas X"
song = "Old Town Road"
place = 2

print("Debuting at #" + str(place) + ": '" + song + "' by " + artist)

# Using f strings

print(f"Debuting at #{place}: '{song}' by {artist}")

# it is easier to see what the final string will be using f strings

# any valid python expression can go inside the parenthesis

greeting = 'Ahoy'
noun = 'Boat'

print(f"{greeting.lower()}, {noun.upper()}yMc{noun}Face")
print(f"{greeting*3}, {noun[0:3]}yMc{noun[-1]}face")
