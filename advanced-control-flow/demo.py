# Other logical operators:
# and, or, is, not, in

test_string = "hello world!"
b = 4
c = "4"
d = 4.0

# What does this print out?
# print(b == d and b is d)
print(b == c)

# You can also write if statements like this:
# Why would this method not be good?
number = 1329

if(number > 1000): print("Wow very big number !!!")
else: print ("Wow very tiny number !!!")

# Match statements
command = input("Type 1 to say hello, type 2 to say goodbye, type 3 to say cheese")
match command:
    case "1":
        print("hello!")
    case "2":
        print("goodbye!")
    case "3":
        print("cheese!")
    case other:
        print("that wasn't an option!")

# Inline if statements
print("true case" if 5 > 2 else "false case")
print("true case" if 5 < 2 else "false case")

# Transform the following if statement into an inline if
if 3 > 2:
    print("true")
else:
    print("false")

# Escape Codes
# print(" / ")
# print('ron's ronning')

# Other Escape Codes: \t, \n

# ANSI Escape Codes - alter the command line!
# https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
# Ex. color:
RED = "\u001b[31m"
RESET = "\u001b[0m"
print(f'{RED}This text is red. {RESET} This text is back to normal.')

    