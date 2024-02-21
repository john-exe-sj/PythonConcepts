class Animal(): 
    def __init__(self, color, name):
        self.color = color
        self.name = name

creature1 = Animal("black", "Chuck")
creature2 = Animal("Neon Green", "Michael")

class House():
    def __init__(self, animals):
        self.animals = animals


house1 = House([creature1, creature2])

print(house1.animals[0].name)


my_first_dict = {
    'a': 'Pikachu', 
    'b': 'Charmander', 
    'c': 'Squirtle', 
    'd': 'Bulbasaur'
}



def setPokemon(pokemon): 
    # Put code here to give player a pokemon
    pass

usrinput = ''
while usrinput not in my_first_dict: 
    usrinput = input("choose\n")
    if usrinput not in my_first_dict: 
        print("pokemon not available, try again")
    else: 
        print("you've chosen", my_first_dict[usrinput])
        setPokemon(my_first_dict[usrinput])


