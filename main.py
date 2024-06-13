def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)

    characters_counted = get_character_count(text)

    converted_list = convert_to_list(characters_counted)

    sorted_list = sort_characters_by_frequency(converted_list)

    print_report(sorted_list, book_path, num_words)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_character_count(text):
    character_dictionary = {}
    text = text.lower()
    for character in text:
        if character.isalpha():
            if character in character_dictionary:
                character_dictionary[character] += 1
            else:
                character_dictionary[character] = 1
    return character_dictionary


def convert_to_list(character_dictionary):
    character_list = []
    for char, count in character_dictionary.items():
        character_list.append({"char": char, "num": count})
    return character_list


def sort_characters_by_frequency(character_list):
    def sort_on(dictionary):
        return dictionary["num"]
    character_list.sort(reverse=True, key=sort_on)
    return character_list


def print_report(sorted_list, book_path, num_words):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for item in sorted_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")


main()