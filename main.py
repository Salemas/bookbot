with open("books/frankenstein.txt") as file:
    file_content = file.read()

words = file_content.split()
print(len(words))
