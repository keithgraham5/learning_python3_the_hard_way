name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_in_centimetres = (height * 2.54)
weight = 180 # lbs
weight_in_kilograms = (weight * 0.45359237)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall and {height_in_centimetres} in cm.")
print(f"He's {weight} pounds or {weight_in_kilograms} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age + height + weight

print(f"If I add {age}, {height}, and {weight} I get {total}.")