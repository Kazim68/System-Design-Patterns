
# ========================================================================================
# attach a new behavior to objects by placing these objects inside special wrapper objects 
# that contain the new behavior.
# ========================================================================================

# No inheritance | Use composition


from abc import ABC, abstractmethod


# Interface
class INotifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass

    @abstractmethod
    def getUsername(self) -> str:
        pass


# Concrete class inherits from INotifier
class Notifier(INotifier):
    def __init__(self, username: str):
        self.__username = username

    def send(self, message: str) -> None:
        print(f"Sending message to {self.__username}: {message}")

    def getUsername(self) -> str:
        return self.__username



# Abstract class inherits from INotifier
class BaseDecorator(INotifier):
    def __init__(self, notifier: INotifier):
        self.__notifier = notifier          # wrapper

    def send(self, message: str) -> None:
        self.__notifier.send(message)       # wrapper calls the send method of the wrapped object

    def getUsername(self) -> str:
        return self.__notifier.getUsername()
    

# Now these inherit from BaseDecorator
class FacebookDecorator(BaseDecorator):
    def __init__(self, notifier: INotifier):
        super().__init__(notifier)

    # Overriding the send method
    def send(self, message: str) -> None:
        super().send(message)
        print("Sending message to Facebook")

class WhatsAppDecorator(BaseDecorator):
    def __init__(self, notifier: INotifier):
        super().__init__(notifier)

    # overriding the send method 
    def send(self, message: str):
        super().send(message)
        print("Sending message to WhatsApp")
        

if __name__ == '__main__':
    allNotifier = FacebookDecorator(WhatsAppDecorator(Notifier("John")))
    allNotifier.send("Hello")

    onlyFacebookNotifier = FacebookDecorator(Notifier("John"))
    onlyFacebookNotifier.send("Hello")