class ApplicationState:
    instance = None         # static variable

    # private constructor
    def __init__(self):
        self.isLoggedIn = False

    @staticmethod
    def getAppState():
        if not ApplicationState.instance:  
            ApplicationState.instance = ApplicationState()
        return ApplicationState.instance
    

# usage
if __name__ == "__main__":
    appState1 = ApplicationState.getAppState()
    print(appState1.isLoggedIn)     # False

    appState2 = ApplicationState.getAppState()
    appState1.isLoggedIn = True

    print(appState1.isLoggedIn)     # True
    print(appState2.isLoggedIn)     # True

# single object is globally accessible within the program.