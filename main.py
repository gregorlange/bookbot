def main():
    frankenstein = "books/frankenstein.txt"
    read_book(frankenstein)

def read_book(book_path):
    with open(book_path) as book:
        content = book.read()
        print(content)
        count_words(content)

def count_words(book_content):
    words = book_content.split()
    word_count = len(words)
    print(f"{word_count} words counted in this text.")

main()