# This program demonstrates polymorphism.

import f_animals as animals

def main():
    # Create a Mammal object, a Dog object, and
    # a Cat object.
    bear = animals.Mammal('bear')
    dog = animals.Dog()
    cat = animals.Cat()


    # Display information about each one.
    print('Here are some animals and')
    print('the sounds they make.')
    print('--------------------------')
    
    show_mammal_info(bear)
    print()

    show_mammal_info(dog)
    print()

    show_mammal_info(cat)
    print()

    show_mammal_info('bird')
    print()


def show_mammal_info(creature):
    if isinstance(creature,animals.Mammal):
        creature.show_species()
        creature.make_sound()
    else:
        print('That is not a mammal!')


# Call the main function.
main()


name = 'John'

if isinstance(name,str):
    print('This is a string')
else:
    print('This is not a string')