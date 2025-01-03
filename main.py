def main():
    frankenstein = "books/frankenstein.txt"
    book_content = read_book(frankenstein)
    count_words(book_content)
    count_characters(book_content)

def read_book(book_path):
    with open(book_path) as book:
        content = book.read()
        print(content)
        return content

def count_words(book_content):
    words = book_content.split()
    word_count = len(words)
    print(f"{word_count} words counted in this text.")

def count_characters(book_content):
    book_string = book_content.lower()
    characters = {}
    for character in book_string:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    print(characters)

main()