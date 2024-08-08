from abc import ABC, abstractmethod


# abstract class
class BaseGameLoader(ABC):
    
    # template method           some methods are implemented and some are not
    def load(self):
        data = self.loadLocalData()
        self.createObject(data)
        self.downloadAdditionalFiles()
        self.cleanTempFiles()   

    @abstractmethod
    def loadLocalData(Self):
        pass

    @abstractmethod
    def createObject(self):
        pass

    @abstractmethod
    def downloadAdditionalFiles(self):
        pass

    # implemented method
    def cleanTempFiles(self):
        print('Cleaning temp files')


class WorldOfWarcraftLoader(BaseGameLoader):
    
    def loadLocalData(self):
        print('Loading local data for World of Warcraft')
        return 'data'

    def createObject(self, data):
        print('Creating object for World of Warcraft')

    def downloadAdditionalFiles(self):
        print('Downloading additional files for World of Warcraft')

    
class DiabloLoader(BaseGameLoader):
    
    def loadLocalData(self):
        print('Loading local data for Diablo')
        return 'data'

    def createObject(self, data):
        print('Creating object for Diablo')

    def downloadAdditionalFiles(self):
        print('Downloading additional files for Diablo')
    


if __name__ == '__main__':
    wow = WorldOfWarcraftLoader()
    wow.load()
    
    diablo = DiabloLoader()
    diablo.load()