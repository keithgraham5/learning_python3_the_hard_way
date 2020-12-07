
#creating a varaible with a value of 10
types_of_people = 10
#creating a variable with an f-string that contains another variable.
'''Use when imbedding python expressions inside string literals for formatting'''
x = "There are {types_of_people} types of people."
# 3 variables last one containing
binary = "binary"
do_not = "don't"
y = f"Those who know "binary' and those who "do_not"."

#print x and y variables
print(s)
print(y)
#print two f-strings each containing a variable x or y
print(f"I said: {x}")
print(f"I also said: '{y}'")

#create a variable, one vaiable contains a string with str.format
#print that varaible with str.format()
hilarious = False
joke_evaluation = "Isn't that joke so funny?! "

print(joke_evaluation.format(hilarious))

#create two str variable connecting the string together using +

w = This is the left side of...
e = a string with a right side.

print(w + e)