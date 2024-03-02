def howMuchLetters(file):
    letter_count = {}

    for word in file:
#        print(word)
        for letter in word:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

    return letter_count

def main():
    with open("./books/frankenstein.txt") as file:
        file_content = file.read()

    lower_case = file_content.lower()
    words = lower_case.split()
    print(len(words))
    count = howMuchLetters(words)
    print(count)

if __name__ == "__main__":
    main()