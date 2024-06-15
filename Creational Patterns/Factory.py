from abc import ABC, abstractmethod


# Burger interface
class Burger(ABC):
    
    @abstractmethod
    def prepare(self):
        pass

# types of burgers can be extended without the need of conditionals
class BeefBurger(Burger):

    def prepare(self):
        print('Preparing Beef Burger...')


class PattieBurger(Burger):

    def prepare(self):
        print('Preparing Pattie Burger...')


class Restaurant(ABC):

    @abstractmethod         # This is the Factory Method! *******************8
    def createBurger(self):
        pass

    def orderBurger(self):
        burger = self.createBurger()
        burger.prepare()
        return burger

class BeefBurgerRestaurant(Restaurant):

    def createBurger(self):
        print('creating Beef Burger...')
        return BeefBurger()

class PattieBurgerRestaurant(Restaurant):

    def createBurger(self):
        print('creating Pattie Burger...')
        return PattieBurger()


if __name__ == "__main__":
    beefRestaurant = BeefBurgerRestaurant()
    beefBurger = beefRestaurant.orderBurger()

    pattieRestaurant = PattieBurgerRestaurant()
    pattieBurger = pattieRestaurant.orderBurger()

