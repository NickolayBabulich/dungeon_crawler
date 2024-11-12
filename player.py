from enum import Enum
from typing import List, Tuple


class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


class Player:
    """ Класс игрока """
    MAX_HEALTH = 100
    MAX_ATTACK = 10
    MAX_DEFENSE = 50
    MAX_INVENTORY_SIZE = 10
    MAX_POSITION_VALUE_X, MAX_POSITION_VALUE_Y = 10, 10

    def __init__(self, name: str, attack: int, defense: int, position: Tuple[int, int]):
        """
        Конструктор игрока
        :param name: имя
        :param attack: атака
        :param defense: защита
        :param position: позиция на карте
        """
        self.name: str = name
        self.health: int = self.MAX_HEALTH
        self.attack: int = attack
        self.defense: int = defense
        self.inventory: List[str] = []
        self.position: Tuple[int, int] = position

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError("Имя игрока не может быть пустым")
        if not value.isalpha():
            raise ValueError("Имя игрока должно содержать только буквы")
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value: int):
        if value < 0 or value > self.MAX_HEALTH:
            raise ValueError(f"Здоровье не может быть меньше 0 и больше {self.MAX_HEALTH}")
        self.__health = value

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, value: int):
        if value < 0 or value > self.MAX_ATTACK:
            raise ValueError(f"Атака не может быть меньше 0 и больше {self.MAX_ATTACK}")
        self.__attack = value

    @property
    def defense(self):
        return self.__defense

    @defense.setter
    def defense(self, value: int):
        if value < 0 or value > self.MAX_DEFENSE:
            raise ValueError(f"Защита не может быть меньше 0 и больше {self.MAX_DEFENSE}")
        self.__defense = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value: Tuple[int, int]):
        if (value[0] or value[1]) < 0 or (value[0] > self.MAX_POSITION_VALUE_X or value[1] > self.MAX_POSITION_VALUE_Y):
            raise ValueError("Координаты позиции не могут быть меньше нуля")
        if value[0] > self.MAX_POSITION_VALUE_X:
            raise ValueError(f"Координаты позиции X не могут быть больше {self.MAX_POSITION_VALUE_X}")
        if value[1] > self.MAX_POSITION_VALUE_Y:
            raise ValueError(f"Координаты позиции Y не могут быть больше {self.MAX_POSITION_VALUE_Y}")
        self.__position = value

    # Методы для работы с инвентарем
    def add_to_inventory(self, item: str):
        """
        Добавляет предмет в инвентарь
        :param item: предмет
        """
        if item in self.inventory:
            raise ValueError(f"В инвентаре уже есть {item}")
        if not isinstance(item, str):
            raise ValueError("Предмет должен быть строковым литералом")
        if len(self.inventory) < self.MAX_INVENTORY_SIZE:
            self.inventory.append(item)
        else:
            raise ValueError(f"Ваш инвентарь полон")

    def remove_from_inventory(self, item: str):
        """
        Удаляет предмет из инвентаря
        :param item: предмет
        """
        if item not in self.inventory:
            raise ValueError("Такого предмета нет в вашем инвентаре")
        self.inventory.remove(item)

    def inventory_is_full(self):
        """
        Проверяет полон ли инвентарь
        :return: True если заполнен, False если нет
        """
        return len(self.inventory) == self.MAX_INVENTORY_SIZE

    def is_alive(self) -> bool:
        """
        Проверяет жив ли персонаж
        :return: Вернет True если жив, False - мертв
        """
        return self.health > 0

    def take_damage(self, value: int):
        """
        Наносит урон персонажу
        :param value: количество урона
        :return: количество нанесенного урона
        """
        if value < 0:
            raise ValueError("Урон не может быть отрицательным")

        if not self.is_alive():
            raise ValueError("Персонаж уже мертв")

        if self.defense == 100:
            return 0

        damage = max(1, int(value * (1 - self.defense / 100)))
        self.health -= damage

        if self.health <= 0:
            self.health = 0
        return damage

    def move(self, direction: Direction) -> bool:
        """
        Перемещает персонажа
        :param direction: направление
        :return: True если переместился, False если нет
        """
        current_player_position = self.position
        new_position_x = current_player_position[0] + direction.value[0]
        new_position_y = current_player_position[1] + direction.value[1]
        new_position = (new_position_x, new_position_y)
        try:
            self.position = new_position
            return True
        except ValueError:
            return False

    def __repr__(self):
        return f'<Игрок {self.name} - (здоровье - {self.health}, атака - {self.attack}, защита - {self.defense})>'

    def __str__(self):
        return (f"Персонаж: {self.name}\n"
                f"Здоровье: {self.health}\n"
                f"Атака: {self.attack}\n"
                f"Защита: {self.defense}\n"
                f"Текущая позиция: {self.position}")


player1 = Player('Odin', 10, 50, (0, 0))
player1.move(Direction.DOWN)
print(player1)
