def howMuchLetters(file):
    ...

def main():
    with open("./books/frankenstein.txt") as file:
        file_content = file.read()

    lower_case = file_content.lower()
    words = lower_case.split()
    print(len(words))
    print(words[0])

if __name__ == "__main__":
    main()