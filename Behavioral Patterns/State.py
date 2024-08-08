from abc import ABC, abstractmethod

# interface
class State(ABC):

    def __init__(self, phone):
        self._phone = phone

    # abstract method 
    def onHome(self):
        pass

    # abstract method
    def onOffOn(self):
        pass


class Phone:
    
    def __init__(self):
        self._state = OffState(self)

    def setState(self, state):
        self._state = state
    
    def lock(self):
        return "Locking phone and turning off the screen"
    
    def home(self):
        return "Going to home screen"
    
    def unlock(self):
        return "Unlocking the phone to home"
    
    def turnOn(self):
        return "Turning screen on, device still locked"
    
    def clickHome(self):
        return self._state.onHome()
    
    def clickPower(self):
        return self._state.onOffOn()


class ReadyState(State):
    
    def __init__(self, phone):
        super().__init__(phone)

    
    # override 
    def onHome(self):
        return self._phone.home()
    
    # override
    def onOffOn(self):
        self._phone.setState((OffState(self._phone)))
        return self._phone.lock()
    

class OffState(State):

    def __init__(self, phone):
        super().__init__(phone)
    
    # override
    def onHome(self):
        self._phone.setState(LockedState(self._phone))
        return self._phone.turnOn()
    
    # override
    def onOffOn(self):
        self._phone.setState(LockedState(self._phone))
        return self._phone.turnOn()
    

class LockedState(State):

    def __init__(self, phone):
        super().__init__(phone)

    #override
    def onHome(self):
        self._phone.setState(ReadyState(self._phone))
        return self._phone.unlock()
    
    #override
    def onOffOn(self):
        self._phone.setState(OffState(self._phone))
        return self._phone.lock()
    

if __name__ == "__main__":
    phone = Phone()

    print(phone.clickPower())
    print(phone.clickPower())
    print(phone.clickHome())
    print(phone.clickHome())
    print(phone.clickHome())
    print(phone.clickPower())
    print(phone.clickPower())
    print(phone.clickHome())