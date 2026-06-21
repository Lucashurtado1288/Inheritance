# name of the superclass Plant
class Plant:
    def __init__(self,color):
        self.__color = color

    # one method to get color as initialized
    def get_color(self):
        return self.__color

# subclass Flower that is inherating from superclass Plant
    # the init method has to have two arguements one from 
    # the plant superclass and argument for subclass flower: petals
class Flower(Plant):
    def __init__(self,color, petals):   # the init method of the subclass 
        Plant.__init__(self,color)      # has to also call the init method of the super class

        self.__petals = petals          # assigns the subclass

    def get_petals(self):
        return self.__petals
