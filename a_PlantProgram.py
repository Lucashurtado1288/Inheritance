import a_PlantClass as pc

#Creating an instance of the superclass Plant
primrose = pc.Plant("Green")

#Creating an instance of the subclass Flower
    # When creating an instance of the subclass you need 2 arguments
    # This was clarified in the PlantClass.py statement below
    # class Flower(Plant):
    #    def __init__(self,color, petals):
sunflower = pc.Flower("Yellow",10)


print(primrose.get_color())

print(sunflower.get_color())
print(sunflower.get_petals())

# primrose is an instance of the superclass
    # get_petals is a method of the subclass
    # an instance of the superclass cannot use a method of the subclass
    # this will error out
print(primrose.get_petals())
