# TODO Написать 3 класса с документацией и аннотацией типов

# Абстрактный класс CarVAZ (Машина марки ВАЗ)

from abc import ABC, abstractmethod

class CarVAZ(ABC):
    def __init__(self, model: str, yearCreate: int, fuel_cap: float):
        if yearCreate < 1977 :  # Первая машина марки ВАЗ была сделана в 1970  году
            raise ValueError("Год выпуска машины марки Ваз должен быть не меньше 1970")
        if fuel_cap <= 0:
            raise ValueError("Объем топливного бака должен быть больше 0")
        self.model = model                # Модель машины
        self.yearCreate = yearCreate                  # Год выпуска
        self.fuel_cap = fuel_cap  # Объем топливного бака

    @abstractmethod
    def start_engine(self) -> None:
        """
        Метод для запуска двигателя.
        >>> carVAZ.start_engine()
        """
        ...

    @abstractmethod
    def drive(self, distance: float) -> None:
        """
        Метод для подсчета пробега машины.
        Аргументы:
        - distance: Расстояние, которое машина проехала.

        >>> carVAZ.drive(10.5)
        """
        ...

    @abstractmethod
    def refuel(self, liters: float) -> None:
        """
        Метод для подсчета затрат топлива.
        Аргументы:
        - liters: Количество литров топлива для заправки.
        >>> carVAZ.refuel(20.0)
        """
        ...

# Абстрактный класс Scooter (Самокат)

from abc import ABC, abstractmethod

class Scooter(ABC):
    def __init__(self, model: str, bat_cap: float, power_reserve: float):
        if bat_cap < 10:
            raise ValueError("Емкость батареи должна быть больше 10")
        if power_reserve <= 0:
            raise ValueError("Запас хода должен быть быть больше 0")
        self.model = model  # Модель самоката
        self.bat_cap = bat_cap  # Емкость батареи
        self.power_reserve = power_reserve  # Запас хода на одной зарядке

    @abstractmethod
    def charge(self, hours: int) -> None:
        """
        Метод для зарядки самоката.
        Аргументы:
        - hours: Количество часов для заряядки.
        >>> scooter.charge(3)
        """
        ...

    @abstractmethod
    def ride(self, distance: float) -> None:
        """
        Метод для опредедения пробега.
        Аргументы:
        - distance: Расстояние в километрах.
        >>> scooter.ride(15.0)
        """
        ...

    @abstractmethod
    def check_battery(self) -> float:
        """
        Метод для проверки уровня заряда батареи, покажет уровень заряда в процентах.
        >>> scooter.check_battery()
        85.0
        """
        ...

# Абстрактный класс Fridge (Холодильник)

from abc import ABC, abstractmethod

class Fridge(ABC):
    def __init__(self, brand: str, volume: float, temp: float):
        if volume < 100:
            raise ValueError("Объем холодильника должен быть более 100л")
        if not (4 <= temp <= 6):
            raise ValueError("Температура холодильника должна быть от +4 до +6 градусов")
        self.brand = brand  # Бренд холодильника
        self.volume = volume    # Объем холодильника
        self.temp = temp  # Температура  холодильника

    @abstractmethod
    def set_temp(self, temperature: float) -> None:
        """
        Метод для установки температуры внутри морозильного отделения.
        Аргументы:
        - temperature: Желаемая температура.
        >>> fridge.set_temp(-18.0)
        """
        ...

    @abstractmethod
    def quant(self, item: float) -> None:
        """
        Количество полок в холодильнике.
        Считает, скольео осталось свободных полок исходя из веса продуктов
        Аргументы:
        - item: Количество продуктов.

        >>> fridge.quant("milk")
        """
        ...

    @abstractmethod
    def check_prod(self) -> list[str]:
        """
        Метод для подсчета списка продуктов, которых осталось мало

        >>> fridge.check_prod()
        ['milk', 'eggs', 'butter']
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
