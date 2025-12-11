cute_animals = ["Pandas",
                "Kittens",
                "Puppies",
                "Bunnies",
                "Red Foxes",
                "Baby Sea Otters",
                "Hedgehogs",
                "Chinchillas",
                "Koalas",
                "Sugar Gliders"]

for animal in cute_animals:
    print(animal)

user_input = input("Choose an animale to eliminate!: ")

if user_input in cute_animals:
    cute_animals.remove(user_input)


for animal in cute_animals:
    print(animal)
