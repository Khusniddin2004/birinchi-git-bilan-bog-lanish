#Constructor class da berilgan sifat va qobilyaotlarga asoslanib obyekt ko'rinishida chiqarib beriladi
# Abstraction

from abc import ABC, abstractclassmethod

class center(ABC):

    def staff(center, name):
        center.name = name

    @abstractclassmethod
    def student(center):
        pass

    def Admin(staff):      


