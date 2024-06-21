
name = "chirag"

print(len(name))
print(name.endswith("rag")) # true 
print(name.startswith("ha")) # false 
print(name.capitalize())

# Returns the length of the string.
print(len("Hello"))  # Output: 5

# Converts all characters in the string to lowercase.
print("Hello".lower())  # Output: "hello"

# Converts all characters in the string to uppercase.
print("Hello".upper())  # Output: "HELLO"

# Capitalizes the first character of the string.
print("hello".capitalize())  # Output: "Hello"

# Converts the first character of each word to uppercase.
print("hello world".title())  # Output: "Hello World"

# Removes leading and trailing whitespace.
print("  hello  ".strip())  # Output: "hello"

# Removes leading whitespace.
print("  hello  ".lstrip())  # Output: "hello  "

# Removes trailing whitespace.
print("  hello  ".rstrip())  # Output: "  hello"

# Replaces occurrences of a substring.
print("hello world".replace("world", "there"))  # Output: "hello there"

# Splits the string into a list using the specified separator.
print("hello world".split(" "))  # Output: ["hello", "world"]

# Joins elements of a list into a string using the specified separator.
print(" ".join(["hello", "world"]))  # Output: "hello world"

# Returns the index of the first occurrence of the substring, or -1 if not found.
print("hello".find("e"))  # Output: 1

# Checks if the string starts with the specified prefix.
print("hello".startswith("he"))  # Output: True

# Checks if the string ends with the specified suffix.
print("hello".endswith("lo"))  # Output: True

# Checks if all characters in the string are digits.
print("12345".isdigit())  # Output: True

# Checks if all characters in the string are alphabetic.
print("hello".isalpha())  # Output: True

# Checks if all characters in the string are alphanumeric.
print("hello123".isalnum())  # Output: True

# Counts occurrences of a substring in the string.
print("hello world".count("o"))  # Output: 2


