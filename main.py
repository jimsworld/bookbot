def main():
# Data Import
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words, word_list = get_num_words_and_words(text)

# Main Tasks
    characters_counted = get_character_count(text)
    converted_list = convert_to_list(characters_counted)
    sorted_list = sort_characters_by_frequency(converted_list)

# Print Main Tasks
    print_report(sorted_list, book_path, num_words)

# Mini Tasks
    first_100_chars = first_100_characters(text)
    digits_counted = get_digit_count(text)
    converted_list_digits = convert_to_list(digits_counted)
    sorted_list_digits = sort_characters_by_frequency(converted_list_digits)

# Print Mini Tasks
    print_minitasks(first_100_chars, word_list[:10], sorted_list_digits)


########## Main Tasks ##########
def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words_and_words(text):
    words = text.split()
    return len(words), words


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
    print(f"\n- Word count:\n{num_words} words found in the document")
    print("\n- Character count:")
    for item in sorted_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")


########## Mini Tasks ##########
def first_100_characters(text):
    return text[:100]


def get_digit_count(text):
    digit_dictionary = {}
    for digit in text:
        if digit.isdigit():
            if digit in digit_dictionary:
                digit_dictionary[digit] += 1
            else:
                digit_dictionary[digit] = 1
    return digit_dictionary


def print_minitasks(first_100_chars, sample_words, sorted_list_digits):
    print("\n--- Mini Tasks Report ---")
    print(f"\n- First 100 characters:\n{first_100_chars}")
    print("\n- Sample of the first 10 words:")
    print(", ".join(sample_words))
    print("\n- Digit count:")
    for item in sorted_list_digits:
        print(f"The '{item['char']}' digit was found {item['num']} times")
    print("--- End Mini Tasks report ---")


main()