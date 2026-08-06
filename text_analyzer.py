def count_characters(text):
    return len(text)


def count_words(text):
    return len(text.split())


def count_lines(text):
    return len(text.splitlines())


text = input("Enter some text: ")

print("Characters:", count_characters(text))
print("Words:", count_words(text))
print("Lines:", count_lines(text))
