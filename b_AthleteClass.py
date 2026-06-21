# Superclass Athlete
class Athlete:
    # initializing the Athlete attributes
    def __init__(self,ht,wt,bodyfat):
        self.__ht = ht
        self.__wt = wt
        self.__bf = bodyfat

    # Acessor methods for each attribute
    def get_ht(self):
        return self.__ht

    def get_wt(self):
        return self.__wt

    def get_bf(self):
        return self.__bf


# Subclass Football Player
class Football_Player(Athlete):
    # initializing all attributes from superclass then adding two more (position,team)
    def __init__(self,ht,wt,bodyfat,position,team):
        # Call the init method of the superclass 
        Athlete.__init__(self,ht,wt,bodyfat)
        # adding the attributes of the subclass
        self.__position = position
        self.__team = team


    def get_position(self):
        return self.__position

    def get_team(self):
        return self.__team










    
