# Other logical operators:
# and, or, is, not, in

test_string = "hello world!"
b = 4
c = "4"
d = 4.0

# What does this print out?
# print(b == d and b is d)

# You can also write if statements like this:
# Why would this method not be good?
number = 1329

if(number > 1000): print("Wow very big number !!!")
else: print ("Wow very tiny number !!!")

# Match statements

# Inline if statements

# Transform the following if statement into an inline if
if 3 > 2:
    print("true")
else:
    print("false")

# Uncomment, then try printing these out
# print(" / ")
# print('ron's ronning')

# Other Escape Codes: \t, \n

# ANSI Escape Codes - alter the command line!
# https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
# Ex. color:
RED = "\u001b[31m"
RESET = "\u001b[0m"
print(f'{RED}This text is red. {RESET} This text is back to normal.')