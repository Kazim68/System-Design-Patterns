from abc import ABC, abstractmethod


class Burger:

    def __init__(self):
        self.buns = None
        self.patty = None
        self.beef = None
        self.cheese = None
        self.veggie = None

    @property.setter
    def setBuns(self, buns):
        self.buns = buns
    
    @property.setter
    def setPatty(self, patty):
        self.patty = patty

    @property.setter
    def setBeef(self, beef):
        self.beef = beef

    @property.setter
    def setCheese(self, cheese):
        self.cheese = cheese

    @property.setter
    def setVeggie(self, veggie):
        self.veggie = veggie


# better to implement a builder interface 
class BurgerBuilder:
    
    def __init__(self):
        self.burger = Burger()

    def reset(self):
        self.burger = Burger()
        return self

    def addBuns(self, bunStyle):
        self.burger.setBuns(bunStyle)
        return self

    def addPatty(self, pattyStyle):
        self.burger.setPatty(pattyStyle)
        return self
    
    def addBeef(self, beefStyle):
        self.burger.setBeef(beefStyle)
        return self

    def addCheese(self, cheeseStyle):
        self.burger.setCheese(cheeseStyle)
        return self
    
    def addVeggie(self, veggieStyle):
        self.burger.setVeggie(veggieStyle)
        return self

    def build(self):
        return self.burger
    

class Director:
    
    def buildBeefBurger(builder):
        builder.reset().addBuns('sesame').addBeef('roasted').addCheese('swiss')

    def buildCheeseBurger(builder):
        builder.reset().addBuns('milk').addBeef('roasted').addPatty('chicken').addCheese('cheddar rolled')

    def buildFishPattyBurger(builder):
        builder.reset().addBuns('whole wheat').addPatty('fish').addCheese('swiss')

    def buildVeggieBurger(builder):
        builder.reset().addBuns('sesame').addVeggie('grilled').addBeef('roasted').addCheese('swiss')
    

if __name__ == "__main__":

    director = Director()

    customBurger = BurgerBuilder().addBuns('whole wheat').addBeef('grilled').addVeggie('roasted').addPatty('chicken').addCheese('swiss').build()

    builder =  BurgerBuilder()
    
    director.buildBeefBurger(builder)
    builder.build()

    director.buildCheeseBurger(builder)
    builder.addCheese('swiss').build()

