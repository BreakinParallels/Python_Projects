



# Creating a class = Members, with private and protected attributes

class Members:
    def __init__(self):
        self._lastName = "Jones"
        self.__employeeID = 123

    def getPrivate(self):
        print(self.__employeeID)

    def setPrivate(self, private):
        self.__employeeID = private

    def getProtected(self):
        print(self._lastName)

    def setProtected(self, protected):
        self._lastName = protected

# Making use of our private and protected attributes

obj = Members()
obj.getPrivate()
obj.setPrivate(456)
obj.getProtected()
obj.setProtected("Jackson")
