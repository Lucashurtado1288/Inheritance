import b_AthleteClass as ac

# Creating an instance of the superclass Athlete (ht,wt,bodyfat)
generic_athlete = ac.Athlete(6,220,0.2)

# Creating an instance of the subclass (ht,wt,bodyfat,position,team)
quarterback = ac.Football_Player(6.2,250,0.15,'quarterback','offense')

#Printing ht of superclass
print("The height for the generic athlete is:",generic_athlete.get_ht())

# Printing team of superclass, WONT WORK 
# print("The team of the generic athlete is:",generic_athlete.get_team())

# Printing wt of subclass
print("The weight for the football player is:",quarterback.get_wt())

# Printing position of subclass
print("The position of the football player is:",quarterback.get_position())
