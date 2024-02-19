class Library:
    def _init_(self):
        self.books = {}
        self.users = {}

    def add_book(self, book_id, title, author):
        if book_id not in self.books:
            self.books[book_id] = {"title": title, "author": author, "available": True}
            print(f"Book '{title}' by {author} added to the library.")
        else:
            print("Book ID already exists. Please use a different ID.")

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print("Book removed from the library.")
        else:
            print("Book not found.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book_id, details in self.books.items():
                print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Available: {details['available']}")

    def add_user(self, user_id, name):
        if user_id not in self.users:
            self.users[user_id] = {"name": name, "books_borrowed": []}
            print(f"User '{name}' added to the library.")
        else:
            print("User ID already exists. Please use a different ID.")

    def remove_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            print("User removed from the library.")
        else:
            print("User not found.")

    def display_users(self):
        if not self.users:
            print("No users in the library.")
        else:
            print("Users in the library:")
            for user_id, details in self.users.items():
                print(f"ID: {user_id}, Name: {details['name']}, Books Borrowed: {details['books_borrowed']}")

    def borrow_book(self, user_id, book_id):
        if user_id in self.users and book_id in self.books:
            if self.books[book_id]["available"]:
                self.books[book_id]["available"] = False
                self.users[user_id]["books_borrowed"].append(book_id)
                print(f"Book '{self.books[book_id]['title']}' borrowed by {self.users[user_id]['name']}.")
            else:
                print("Book not available for borrowing.")
        else:
            print("User or book not found.")

    def return_book(self, user_id, book_id):
        if user_id in self.users and book_id in self.books:
            if book_id in self.users[user_id]["books_borrowed"]:
                self.books[book_id]["available"] = True
                self.users[user_id]["books_borrowed"].remove(book_id)
                print(f"Book '{self.books[book_id]['title']}' returned by {self.users[user_id]['name']}.")
            else:
                print("Book not borrowed by the user.")
        else:
            print("User or book not found.")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Display Books")
        print("4. Add User")
        print("5. Remove User")
        print("6. Display Users")
        print("7. Borrow Book")
        print("8. Return Book")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            library.add_book(book_id, title, author)
        elif choice == "2":
            book_id = input("Enter Book ID to remove: ")
            library.remove_book(book_id)
        elif choice == "3":
            library.display_books()
        elif choice == "4":
            user_id = input("Enter User ID: ")
            name = input("Enter User Name: ")
            library.add_user(user_id, name)
        elif choice == "5":
            user_id = input("Enter User ID to remove: ")
            library.remove_user(user_id)
        elif choice == "6":
            library.display_users()
        elif choice == "7":
            user_id = input("Enter User ID: ")
            book_id = input("Enter Book ID to borrow: ")
            library.borrow_book(user_id, book_id)
        elif choice == "8":
            user_id = input("Enter User ID: ")
            book_id = input("Enter Book ID to return: ")
            library.return_book(user_id, book_id)
        elif choice == "9":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__== "_main_":
    main()
