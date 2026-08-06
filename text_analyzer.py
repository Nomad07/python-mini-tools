def count_characters(text):
    return len(text)


def count_words(text):
    return len(text.split())


def count_lines(text):
    return len(text.splitlines())


def word_frequency(text):
    words = text.lower().split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def main():
    text = input("Enter some text: ")

    print("Characters:", count_characters(text))
    print("Words:", count_words(text))
    print("Lines:", count_lines(text))
    print("Word frequency:", word_frequency(text))


if __name__ == "__main__":
    main()
