import abc
import enum

"""
Abstract Factory
=======================================================
カレーとラーメンを作る手順は異なる。
しかし、Client側は、料理の種類分作り方を覚えるのではなく、
cookというメソッドを呼び出すだけでどんな料理でも作れるようにしたい。
それを実現するのがAbstractFactory。cookの中身は料理ごとに異なるが、
Client側はそれを気にする必要はない。
=======================================================
"""


class AbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def cook(self):
        return NotImplementedError


class Food(metaclass=abc.ABCMeta):
    def get_calorie(self) -> int:
        return NotImplementedError


class Carry(Food):
    def __init__(self) -> None:
        self.__calorie = 700

    def get_calorie(self):
        return self.__calorie


class CarryFactory(AbstractFactory):
    def cook(self):
        carry = Carry()
        """
        カレーを作る処理
        """
        return carry


class Ramen(Food):
    def __init__(self) -> None:
        self.__calorie = 800

    def get_calorie(self) -> int:
        return self.__calorie


class RamenFactory(AbstractFactory):
    def cook(self):
        ramen = Ramen()
        """
        ラーメンを作る処理
        """
        return ramen


class FoodType(enum.Enum):
    RAMEN = "Ramen"
    CARRY = "Carry"


def getFactory(food: FoodType):
    f = FoodType
    food_dict = {
        f.RAMEN.value: RamenFactory(),
        f.CARRY.value: CarryFactory()
    }

    return food_dict.get(food)


if __name__ == "__main__":
    f = getFactory("Ramen")
    print(f.cook())
