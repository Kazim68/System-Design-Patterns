
""" Lets you compose objects into tree structures and then work with these structures as 
if they were individual objects. """

from abc import ABC, abstractmethod

# Interface
class Box(ABC):
    @abstractmethod
    def calculatePrice(self) -> float:
        pass



class CompositeBox(Box):
    def __init__(self, boxes: list):
        self.__children = boxes

    # override
    def calculatePrice(self) -> float:
        return sum([box.calculatePrice() for box in self.__children])
    

# abstract class
class Product(Box):
    def __init__(self, title, price: float):
        self._price = price
        self._title = title


# products
class Book(Product):
    def __init__(self, title, price: float):
        super().__init__(title, price)

    # override
    def calculatePrice(self) -> float:
        return self._price
    

class VideoGame(Product):
    def __init__(self, title, price: float):
        super().__init__(title, price)

    # override
    def calculatePrice(self) -> float:
        return self._price
    


# client interface class
class DeliveryService():
    def __init__(self):
        self.__box = None

    def setupOrder(self, boxes: list) -> None:
        self.__box = CompositeBox(boxes)

    def calculateOrderPrice(self) -> float:
        return self.__box.calculatePrice()
    

if __name__ == "__main__":
    service = DeliveryService()
    service.setupOrder([CompositeBox([VideoGame("GTA", 100), Book("Python", 50)]), CompositeBox([Book("Java", 40), VideoGame("FIFA", 100)])])
    print(service.calculateOrderPrice())  # 290.0