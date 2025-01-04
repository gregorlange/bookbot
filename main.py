def main():
    frankenstein = "books/frankenstein.txt"
    book_content = read_book(frankenstein)
    word_count = count_words(book_content)
    characters = count_characters(book_content)
    book_report(frankenstein, word_count, characters)

def read_book(book_path):
    with open(book_path) as book:
        content = book.read()
        return content

def count_words(book_content):
    words = book_content.split()
    word_count = len(words)
    return word_count

def count_characters(book_content):
    book_string = book_content.lower()
    characters = {}
    for character in book_string:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def book_report(book_path, word_count, characters):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print("")
    character_sort = []
    for character in characters:
        character_sort.append({"character": character, "count": characters[character]})
    character_sort.sort(reverse=True, key=sort_on)
    for dict in character_sort:
        if dict["character"].isalpha():
            print(f"The '{dict["character"]}' character was found {dict["count"]} times")

def sort_on(dict):
    return dict["count"]

main()