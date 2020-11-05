"""CRUD operations"""

from model import db, User, Book, BookCopy, Author, Category, BookCategory, connect_to_db


def create_user(email, password, full_name=None, gender=None, created_at):
    """Create and return a new user."""

    user = User(email=email,
                password=password
                full_name=full_name,
                gender=gender,
                created_at=created_at)

    db.session.add(user)
    db.session.commit()

    return user

def create_book(title, liked=None, categories=None)
    """Create and return a new book."""

    book = Book(title=title,
                liked=liked,
                catrgories=categories)

    db.session.add(book)
    db.session.commit()

    return book


def create_book_copy(book)
    """Create a copy of a particular book."""

    book_copy = BookCopy(book=book)

    db.session.add(book_copy)
    db.session.commit()

    return book_copy

def create_author(fname, lname, book)

    author = Author(fname=fname,
                    lname=lname,
                    book=book)

if __name__ == '__main__':
    from server import app
    connect_to_db(app)


