from abc import ABC, abstractmethod


class Storage(ABC):
    """
    Абстрактный класс хранилища
    """
    @property
    @abstractmethod
    def items(self):
        """
        Предметы
        """
        pass

    @property
    @abstractmethod
    def capacity(self):
        """
        Вместительность
        """
        pass

    @abstractmethod
    def add(self, name, qnt):
        """
        Метод для добавления предметов в хранилище
        """
        pass

    @abstractmethod
    def remove(self, name, qnt):
        """
        Метод для забора предметов из хранилища
        """
        pass

    @abstractmethod
    def _get_free_space(self):
        """
        Метод для получения свободного места
        """
        pass

    @abstractmethod
    def get_items(self):
        """
        Метод для получения содержимого хранилища
        """
        pass

    @abstractmethod
    def _get_unique_items_count(self):
        """
        Метод для получения количества уникальных товаров
        """
        pass


class Store(Storage):
    """
    Класс склада
    """
    def __init__(self, items=None, capacity=200):
        if items is None:
            items = {}
        self._items = items
        self._capacity = capacity

    def __repr__(self):
        return 'склад'

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    def add(self, name, qnt):
        if self._get_free_space() < qnt:
            print("Не хватает места на складе")
            return False
        else:
            self._items[name] = self._items[name] + qnt
            return True

    def remove(self, name, qnt):
        if self._items[name] < qnt:
            print("На складе недостаточно товаров")
            return False
        else:
            self._items[name] = self._items[name] - qnt
            return True

    def _get_free_space(self):
        return self._capacity - sum(self._items.values())

    def get_items(self):
        print('На складе хранится:')
        for name, qnt in self._items.items():
            print(f'{qnt} {name}')

    def _get_unique_items_count(self):
        return len(self._items)


class Shop(Storage):
    """
    Класс магазина
    """
    def __init__(self, items=None, capacity=20):
        if items is None:
            items = {}
        self._items = items
        self._capacity = capacity

    def __repr__(self):
        return 'магазин'

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    def add(self, name, qnt):
        if self._get_free_space() < qnt:
            print("Не хватает места в магазине")
            return False
        elif self._get_unique_items_count() >= 5:
            print("В магазине слишком большой ассортимент")
            return False
        else:
            self._items[name] = self._items.get(name, 0) + qnt
            return True

    def remove(self, name, qnt):
        if self._items[name] < qnt:
            print("В магазине недостаточно товаров")
            return False
        else:
            self._items[name] = self._items[name] - qnt
            return True

    def _get_free_space(self):
        return self._capacity - sum(self._items.values())

    def get_items(self):
        print('В магазине хранится:')
        for name, qnt in self._items.items():
            print(f'{qnt} {name}')

    def _get_unique_items_count(self):
        return len(self._items)


class Request:
    """
    Класс запроса
    """
    def __init__(self, string, store, shop):
        storages = {"склад": store, "магазин": shop}
        request = string.split()
        self._departure = storages[request[-3]]
        self._destination = storages[request[-1]]
        self._product = request[-5]
        self._amount = int(request[-6])

    @property
    def departure(self):
        return self._departure

    @property
    def destination(self):
        return self._destination

    @property
    def product(self):
        return self._product

    @property
    def amount(self):
        return self._amount


def main():
    """
    Функция для выполнения запроса пользователя
    """
    items = {"яблоки": 4, "бананы": 10, "груши": 6}
    store = Store(items)
    shop = Shop()

    # Пример запроса: "Доставить 3 бананы из склад в магазин"
    user_string = input("Введите запрос: ")

    request = Request(user_string, store, shop)
    departure = request.departure
    destination = request.destination
    amount = request.amount
    product = request.product

    if departure.remove(product, amount):
        print(f'Курьер забрал {amount} {product} из {departure}\n'
              f'Курьер везет {amount} {product} из {departure} в {destination}')
        if destination.add(product, amount):
            print(f'Курьер доставил {amount} {product} в {destination}')
            destination.get_items()


if __name__ == '__main__':
    main()


