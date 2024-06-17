from abc import ABC, abstractmethod


# interface
class Product(ABC):

    @abstractmethod
    def assemble(self):
        # business logic
        pass


# components
class Gpu(Product):
    pass


class Monitor(Product):
    pass


# company products
class AsusGpu(Gpu):

    def assemble(self):
        print('Assembling Asus Gpu...')


class AsusMonitor(Monitor):

    def assemble(self):
        print('Assembling Asus Monitor...')


class MsiGpu(Gpu):

    def assemble(self):
        print('Assembling Msi Gpu...')

class MsiMonitor(Monitor):

    def assemble(self):
        print('Assembling Msi Monitor...')


# Now the Factories
class Company(ABC):

    @abstractmethod
    def createGpu(self):
        pass

    @abstractmethod
    def createMonitor(self):
        pass


class AsusManufacturer(Company):

    def createGpu(self):
        return AsusGpu()
    
    def createMonitor(self):
        return AsusMonitor()
    

class MsiManufacturer(Company):

    def createGpu(self):
        return MsiGpu()
    
    def createMonitor(self):
        return MsiMonitor()
    


if __name__ == "__main__":
    msi = MsiManufacturer()
    asus = AsusManufacturer()

    msi.createGpu().assemble()
    msi.createMonitor().assemble()

    asus.createGpu().assemble()
    asus.createMonitor().assemble()