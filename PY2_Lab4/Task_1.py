if __name__ == "__main__":
    class Computer:
        """
        Базовый класс компьютеров.
        Атрибуты:
        brand : str - бренд
        model : str - модель
        ram : int - кол-во озу
        storage : int  жесткий диск
        """

        def __init__(self, brand: str, model: str, ram: int, storage: int):
            """
            Инициализация базового компьютера.
            :param brand: бренд
            :param model: модель
            :param ram: кол-во озу гб
            :param storage: жесткий диск гб
            """
            self.brand = brand
            self.model = model
            self.ram = ram
            self.storage = storage

        def __str__(self) -> str:
            """Возвращает строковое представление объекта."""
            return f"Компьютер {self.brand} {self.model}, ОЗУ: {self.ram} ГБ, Память: {self.storage} ГБ"

        def __repr__(self) -> str:
            """Возвращает строку, по которой можно создать аналогичный экземпляр."""
            return f"Computer(brand={self.brand!r}, model={self.model!r}, ram={self.ram!r}, storage={self.storage!r})"

        def upgrade_ram(self, add_ram: int) -> None:
            """
            Увеличение озу
            :param add_ram: Количество доп озу
            """
            self.ram += add_ram
            print(f"ОЗУ увеличена до {self.ram} ГБ.")


    class Laptop(Computer):
        """
        Класс для ноутбуков, наследуется от Computer.
        Атрибуты:
        ----------
        screen : float диагональ
        battery : int время работы
        """

        def __init__(self, brand: str, model: str, ram: int, storage: int, screen: float, battery: int):
            """
            Инициализация ноутбука.
            :param brand: бренд
            :param model: модель
            :param ram: озу
            :param storage: жесткий диск
            :param screen: диагоеналь
            :param battery: время работы
            """
            # Вызов конструктора базового класса Computer
            super().__init__(brand, model, ram, storage)
            self.screen = screen
            self.battery = battery

        def __str__(self) -> str:
            """Возвращает строковое представление объекта."""
            return (f"Ноутбук {self.brand} {self.model}, ОЗУ: {self.ram} гб, Память: {self.storage} гб, "
                    f"Экран: {self.screen}\" дюймов, Время работы: {self.battery} ч.")

        def __repr__(self) -> str:
            """Возвращает строку, по которой можно создать аналогичный экземпляр."""
            return (f"Laptop(brand={self.brand!r}, model={self.model!r}, ram={self.ram!r}, "
                    f"storage={self.storage!r}, screen={self.screen!r}, battery={self.battery!r})")

        def upgrade_ram(self, add_ram: int) -> None:
            """
            Перегрузка метода для увеличения объема оперативной памяти.
            Обоснование: в ноутбуках доступа к ОЗУ нет(распаяна) и ОЗУ не может быть увеличена.
            Поэтому метод будет проверять, можно или нет увеличить озу

            :param add_ram: доп озу
            :raises ValueError: Ошибка если расширение ОЗУ невозможно.
            """
            if self.ram + add_ram > 32:
                raise ValueError("Максимум ОЗУ 32 гб")
            super().upgrade_ram(add_ram)

        def check_battery(self) -> None:
            """
            проверка заряда
            """
            print(f"Остаток заряда батареи: {self.battery} часов.")

        """
        Примечание по инкапс.
        Не вижу явной необходимости делать какие-либо атрибуты или методы 
        непубличными. Но если это надо, то можно добавить префикс к атрибуту, 
        например  _battery, чтобы указать, что прямое изменение этих
         атрибутов пользователем нежелательно.
        """