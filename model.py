"""Models for book app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True
                        )
    email = db.Column(db.String(50),
                     unique=True,
                     nullable=False,
                     )
    password = db.Column(db.String(25),
                         nullable=False,
                         )
    full_name = db.Column(db.String(50),
                         nullable=False
                          )
    birthday = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    gender = db.Column(db.String(17))

    read_book_collection = db.relationship('ReadBooksCollection')

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'


class Book(db.Model):
    """A book"""

    __tablename__ = 'books'

    book_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True
                        )
    title = db.Column(db.String(250), nullable=False)
    categories = db.relationship('Category',
                                 secondary="books_categories",
                                 backref='books'
    )

    author = db.relationship('Author')
    book_category = db.relationship('BookCategory')


    def __repr__(self):
        return f'<Book book_id={self.book_id} title={self.title}>'


class Author(db.Model):
    """An author"""

    __tablename__ = 'authors'

    author_id = db.Column(db.Integer,
                          primary_key=True,
                          autoincrement=True
                          )
    fname = db.Column(db.String(25),
                      nullable=False)
    lname = db.Column(db.String(40),
                      nullable=False
                      )
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'))

    book = db.relationship('Book')

    def __repr__(self):
        return f'<Author author_id={self.author_id} lname={self.lname}>'


class Category(db.Model):
    """A book category"""

    __tablename__ = 'categories'

    category_id = db.Column(db.Integer,
                            primary_key=True,
                            autoincrement=True
                            )
    category = db.Column(db.String(50), nullable=False, unique=True)


    def __repr__(self):
        return f'<Category category_id={self.category_id} category={self.category}>'


class BookCategory(db.Model):
    """Category of a specific book"""

    __tablename__ = 'books_categories'

    book_category_id = db.Column(db.Integer,
                                   primary_key=True,
                                   autoincrement=True
                                   )
    book_id = db.Column(db.Integer,
                        db.ForeignKey('books.book_id'),
                        nullable=False
                        )
    category_id = db.Column(db.Integer,
                            db.ForeignKey('categories.category_id'),
                            nullable=False
                            )

    book = db.relationship('Book')
    category =db.relationship('Category')

    def __repr__(self):
        return f'<BookCategory book_id={self.book_id} category_id={self.book_category_id}>'


class BookStatus(db.Model):
    """The status of a book in a user's Library"""

    __tablename__ = 'book_statuses'

    book_id = db.Column(db.Integer,
                         db.ForeignKey('books.book_id'),
                         primary_key=True,
                         )
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        primary_key=True
                        )

    read = db.Column(db.Boolean)
    liked = db.Column(db.Boolean)
    to_be_read = db.Column(db.Boolean)

    book = db.relationship('Book')
    user = db.relationship('User')


class Bookshelf(db.Model):
    """A user's bookself"""

    __tablename__ = 'bookshelves'

    bookshelf_id = db.Column(db.Integer,
                             primary_key=True,
                             autoincrement=True)
    name = db.Column(db.String(50),
                     nullable=False)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable=False
                        )
    book = db.Column(db.Integer, db.ForeignKey('books.book_id'))
    #created_at = db.Column(db.DateTime, nullale=False)

    def __repr__(self):
        return f'<Bookshelf bookshelf_id={self.bookshelf_id} name={self.name}>'


class BookInBookshelf(db.Model):
    """A book in a particular book self"""

    __tablename__ = 'books_in_bookshelves'

    book_in_book_shelf_id = db.Column(db.Integer,
                         db.ForeignKey('books.book_id'),
                         primary_key=True,
                         )
    bookshelf_id = db.Column(db.Integer,
                            db.ForeignKey('bookshelves.bookshelf_id'),
                            primary_key=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        primary_key=True
                        )
    liked = db.Column(db.Boolean,
                     db.Foreignkey('books.liked'))


    book = db.relationship('Book')
    user = db.relationship('User')
    liked = db.relationship('Book')

    def __repr__(self):
        return f'<BookInBookShelf book_in_bookself_id={self.book_in_book_shelf_id} bookshelf_id={self.bookshelf_id} user_id={self.user_id}>'



def connect_to_db(flask_app, db_uri='postgresql:///bookslibrary', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__=='__main__':
    from server import app

    connect_to_db(app)
