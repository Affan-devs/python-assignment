import json
import os

LIBRARY_FILE = "library.txt"


def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as f:
            return json.load(f)
    return []

def save_library(library):
    with open(LIBRARY_FILE, "w") as f:
        json.dump(library, f, indent=4)

def display_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")


def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read_status = True if read_input == "yes" else False

    

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }

    library.append(book)
    print("✅ Book added successfully!")

def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip().lower()
    for book in library:
        if book["title"].lower() == title:
            library.remove(book)
            print("✅ Book removed successfully!")
            return
    print("❌ Book not found.")


def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    query = input("Enter the search term: ").strip().lower()
    results = []

    if choice == "1":
        results = [book for book in library if query in book["title"].lower()]
    elif choice == "2":
        results = [book for book in library if query in book["author"].lower()]
    else:
        print("❌ Invalid choice.")
        return

    if results:
        print("\nMatching Books:")
        for i, book in enumerate(results, 1):
            print(f"{i}. {format_book(book)}")
    else:
        print("❌ No matching books found.")
        
def display_all_books(library):
    if not library:
        print("📚 Your library is empty.")
    else:
        print("\nYour Library:")
        for i, book in enumerate(library, 1):
            print(f"{i}. {format_book(book)}")

# Display statistics
def display_statistics(library):
    total = len(library)
    read = sum(1 for book in library if book["read"])
    percent_read = (read / total) * 100 if total > 0 else 0
    print(f"\n📊 Total books: {total}")
    print(f"📖 Percentage read: {percent_read:.1f}%")

# Format book details
def format_book(book):
    status = "Read" if book["read"] else "Unread"
    return f'{book["title"]} by {book["author"]} ({book["year"]}) - {book["genre"]} - {status}'

# Main loop
def main():
    library = load_library()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("💾 Library saved to file. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
