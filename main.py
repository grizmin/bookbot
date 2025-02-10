with open("books/frankenstein.txt") as f:
    text = f.read()

def count_words(text):
    words = text.split()
    return len(words)

# print(count_words(text))

def count_chars(text):
    charmap = {}
    for c in text.lower():
        if c in charmap:
            charmap[c] += 1
        else:
            charmap[c] = 1
    return charmap

chars = count_chars(text)

#sorted chars
chars = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))

def report_chars(chars):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} words found in the document")
    for char, count in chars.items():
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
    print("--- End of report ---")

report_chars(chars)