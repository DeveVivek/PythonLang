a = input("Enter first number: ")
b = input("Enter second number: ")
a = int(a)
b = int(b)
avg = (a + b)/2
print("The average of a and b is", avg)

# greeting = "Good Morning, "
# name = "Harry"
# print(type(name))

# Concatenating two strings
# c = greeting + name
# print(c)
name = "Harry"
# print(name[4])
# name[3] = "d" --> Does not work

# print(name[1:4])
# print(name[:4]) # is same as name[0:4]
# print(name[1:]) # is same as name[1:5]
# c = name[-4:-1] # is same is name[1:4]
# print(c)

name = "HarryIsGood"
# d = name[0::3]
d = name[:0:-1]
print(d)

story = "once upon a time there was a youtuber named Harry who uploaded python course with notes Harry"

# String Functions
# print(len(story))
# print(story.endswith("notes"))
# print(story.count("c"))
# print(story.capitalize())
# print(story.find("upon"))
print(story.replace("Harry", "CodeWithHarry"))
 

story = "Harry is good.\nHe\tis ve\\ry good"
print(story)

name = input("Enter your name\n")
print("Good Afternoon, " + name)

letter = '''Dear <|NAME|>,
Greetings from ABC coding house. I am happy to tell you about your selection
You are selected!
Have a great day ahead!
Thanks and regards,
Bill
Date: <|DATE|>
'''
name = input("Enter Your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)

st = "This is a string with double  spaces"

doubleSpaces = st.find("  ")
print(doubleSpaces)

st = "This is a string with double  spaces  ok"

st = st.replace("  ", " ")
print(st)

letter = "Dear Harry, This Python course is nice! Thanks!"
print(letter)

formatted_letter = "Dear Harry,\n\tThis Python course is nice!\nThanks!"
print(formatted_letter)