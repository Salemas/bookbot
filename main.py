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

def converter(dict):
    nice_list = []
    for key in dict:
        if key.isalpha():
            nice_list.append({"letter":key, "count":dict[key]})
    nice_list.sort(reverse=True, key = lambda list: list["count"])
    return nice_list

def report(list, number):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number} words found in the document")   
    for word in list:
        print(f"The '{word['letter']}' character was found {word['count']} times")
    print("--- End report of books/frankenstein.txt ---")

def main():
    with open("./books/frankenstein.txt") as file:
        file_content = file.read()

    lower_case = file_content.lower()
    words = lower_case.split()
 #   print(len(words))
    count = howMuchLetters(words)
 #   print(count)
    
    report(converter(count), len(words))

if __name__ == "__main__":
    main()