# Requirements:
# 1. Given string: text = "Python Programming"
# 2. Print the length of the string
# 3. Print uppercase version
# 4. Print lowercase version
# 5. Print first and last character
# 6. Print first 6 characters (slicing)
# 7. Print last 3 characters (slicing)
# 8. Replace "Python" with "Java" using replace()

# Your Code:
text = "Python Programming"

print(f"Length: {len(text)}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Replace: {text.replace('Python', 'Java')}")
print(f"first 6 characters: {text[:6]}")
print(f"last 3 characters: {text[-3:]}")