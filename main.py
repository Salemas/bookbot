def howMuchLetters(file):
    ...

def main():
    with open("./books/frankenstein.txt") as file:
        file_content = file.read()

    words = file_content.split()
    print(len(words))

if __name__ == "__main__":
    main()