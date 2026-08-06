text = input("Enter some text: ")

characters = len(text)
words = len(text.split())
lines = len(text.splitlines())

print("Characters:", characters)
print("Words:", words)
print("Lines:", lines)
