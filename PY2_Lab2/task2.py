BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """Возвращает cтроку, где "название_книги" берется с помощью атрибута name"""
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """Возвращает строку, которая ипользуется для создания такого же экземляра класса."""
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"



# TODO написать класс Library
class Library:
    def __init__(self, books=None):
        """
        Инициализирует экземпляр библиотеки.
        Если список книг не передан, то параметр книги = пустой список.
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Возвращает следующий идентификатор для новой книги.
        Если библиотека пуста, то get_next_book_id = 1,
        Если не пуста, то к идентификатору последней книги добавляем 1.
        """
        if not self.books:
            return 1
        else:
            next_id = self.books[-1].id + 1
            return next_id

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги по ее идентификатору.
        Если книги с запрашиваемым id не существует, выдает ошибку ValueError = "Книги с запрашиваемым id не существует"
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError(f"Книги с запрашиваемым id {book_id} не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
