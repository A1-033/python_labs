class Book:
    """Базовый класс книги"""
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Вернет  название книги (неизменяемое свойство)"""
        return self._name

    @property
    def author(self) -> str:
        """Вернет автора книги (неизменяемое свойство)."""
        return self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс бумажных книг"""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        """Вернет количество страниц"""
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        """Установит количество страниц с проверкой, что это положительное целое число."""
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целое число")
        if value <= 0:
            raise ValueError("Количество страниц должно быть > 0")
        self._pages = value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    """Класс аудиокниг"""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        """Вернет продолжительность аудиокниг"""
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        """Установит продолжительность аудиокниг с проверкой, что это положительное число с плавающей запятой."""
        if not isinstance(value, (float, int)):
            raise TypeError("Продолжительность должна быть не целым числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть > 0")
        self._duration = float(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"
