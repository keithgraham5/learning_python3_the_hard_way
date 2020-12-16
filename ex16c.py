from sys import argv
#unpacks the arguments given through the command line
script, filename = argv
#
print(f"We're going to erase {filename}")
print("If you dont want that, hit CTRL-C (⌃C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file.....")
# ''' 'w' is an argument that puts open() into write mode
#  w  will truncate the file if it already exits
#  truncate esstially deletes the contents of the file '''
target = open(filename, 'w')

print("Truncating the file. GoodBye!")
#Line not needed as w truncates file anyway
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

#writes the contents of the variable and then a new line
#as a formated txt in the new file
target.write(line1 '\n', line2 '\n', line3 '\n')

print("And finally, we close it.")
target.close()