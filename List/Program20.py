books = ["Python", "Java", "C++"]

new_book = input("Enter a new book: ")
books.append(new_book)

search_book = input("Enter book to search: ")

if search_book in books:
    print("Book is available.")
else:
    print("Book is not available.")

remove_book = input("Enter book to remove: ")

if remove_book in books:
    books.remove(remove_book)
else:
    print("Book not found.")

print("All books:", books)
print("Total books:", len(books))
