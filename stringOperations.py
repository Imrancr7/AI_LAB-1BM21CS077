#day 13
a="hi i am imran"
# The upper() method converts a string to upper case.
print(a.upper())
# The lower() method converts a string to lower case.
print(a.lower())
# The title() method capitalizes each letter of the word within the string.
print(a.title())
# The strip() method removes any white spaces before and after the string.
str="Silver spoon"
print(str.strip())
# the rstrip() removes any trailing characters. Example
str1="hello !!!"
print(str1.rstrip("!"))
# The replace() method replaces all occurences of a string with another string. Example:
print(str1.replace("sp","m"))
# The split() method splits the given string at the specified instance and returns the separated strings as list items.
print(str1.split(" "))
str2="hello"
print(str2.capitalize()) # The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase.
str4="Welcome to the console"
# The center() method aligns the string to the center as per the parameters given by the user
print(str4.center(100))
b="california"
# The count() method returns the number of times the given value has occurred within the given string
count=b.count("i")
print(count)
str5="Welcome to the console !!!"
# The endswith() method checks if the string ends with a given value. If yes then return True, else return False
print(str5.endswith("!"))
str6 = "Welcome to the Console !!!"
print(str6.endswith("to", 4, 10))
str7 = "He's name is Dan. He is an honest man."
# The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1
print(str7.find("is"))
str8 = "He's name is Dan. Dan is an honest man."
# The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception
print(str8.index("Dan"))
str9 = "WelcomeToTheConsole"
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
print(str9.isalnum())
str0 = "Welcome"
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
print(str0.isalpha())
st = "hello world"
# The islower() method returns True if all the characters in the string are lower case, else it returns False
print(st.islower())
st1 = "We wish you a Merry Christmas"
# The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
print(st1.isprintable())
# The isspace() method returns True only and only if the string contains white spaces, else returns False.
st2= "        "       #using Spacebar
print(st2.isspace())
str22 = "        "       #using Tab
print(str22.isspace())
# The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
str11 = "World Health Organization" 
print(str11.istitle())
str21 = "To kill a Mocking bird"
print(str21.istitle())
# The isupper() method returns True if all the characters in the string are upper case, else it returns False.
str13 = "WORLD HEALTH ORGANIZATION" 
print(str13.isupper())
# The endswith() method checks if the string starts with a given value. If yes then return True, else return False.
str14 = "Python is a Interpreted Language" 
print(str14.startswith("Python"))
# The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case
str15 = "Python is a Interpreted Language" 
print(str15.swapcase())
# The title() method capitalizes each letter of the word within the string
str16 = "He's name is Dan. Dan is an honest man."
print(str16.title())