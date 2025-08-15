import os
import shutil
from data_handler import load_data, save_data

LIBRARY_DIR = "MyLibrary"


if not os.path.exists(LIBRARY_DIR):
    os.makedirs(LIBRARY_DIR)

def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    year = input("Enter publication year: ").strip()

    folder_name = title.replace(" ", "_")
    book_path = os.path.join(LIBRARY_DIR, folder_name)

    if os.path.exists(book_path):
        print("❌ Book already exists!")
        return

    os.makedirs(book_path)
    with open(os.path.join(book_path, "details.txt"), "w") as f:
        f.write(f"Title: {title}\nAuthor: {author}\nYear: {year}\n")

    books = load_data()
    books.append([title, author, year])
    save_data(books)

    print(f"✅ '{title}' added successfully.")

def remove_book():
    title = input("Enter book title to remove: ").strip()
    folder_name = title.replace(" ", "_")
    book_path = os.path.join(LIBRARY_DIR, folder_name)

    books = load_data()
    updated_books = [b for b in books if b[0].lower() != title.lower()]

    if len(updated_books) == len(books):
        print("❌ Book not found!")
        return

    save_data(updated_books)

    if os.path.exists(book_path):
        shutil.rmtree(book_path)

    print(f"🗑 '{title}' removed successfully.")

def search_book():
    title = input("Enter book title to search: ").strip().lower()
    books = load_data()

    for book in books:
        if book[0].lower() == title:
            print("\n📖 Book Found:")
            print(f"Title: {book[0]}")
            print(f"Author: {book[1]}")
            print(f"Year: {book[2]}")
            return
    print("❌ Book not found.")

def list_books():
    books = load_data()
    if books:
        print("\n📚 Books in Library:")
        for b in books:
            print(f"- {b[0]} ({b[1]}, {b[2]})")
    else:
        print("📂 No books found.")

def library_statistics():
    books = load_data()
    if not books:
        print("📊 No books to show statistics.")
        return

    total_books = len(books)
    authors = set(b[1] for b in books)
    years = [int(b[2]) for b in books if b[2].isdigit()]

    print("\n📊 Library Statistics:")
    print(f"Total Books: {total_books}")
    print(f"Unique Authors: {len(authors)}")
    if years:
        print(f"Oldest Year: {min(years)}")
        print(f"Newest Year: {max(years)}")

def main():
    while True:
        print("\n==== 📚 Personal Library Menu ====")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. List All Books")
        print("5. Library Statistics")
        print("6. Exit")
        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            list_books()
        elif choice == "5":
            library_statistics()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    main()
