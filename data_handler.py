import os

DATA_FILE = "library_data.txt"

def load_data():
    """Load books from data file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        books = [line.strip().split("|") for line in f if line.strip()]
    return books

def save_data(books):
    """Save books to data file."""
    with open(DATA_FILE, "w") as f:
        for book in books:
            f.write("|".join(book) + "\n")
