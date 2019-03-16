# Xubo Zhu
# ITP 115
# Assignment 8
# 4/2/2017
# Description: Animals


class Animal(object):
    def __init__(self, hunger, happiness, health, energy, age, name, species):
        self.hunger = hunger
        self.happiness = happiness
        self.health = health
        self.energy = energy
        self.age = age
        self.name = name
        self.species = species

    def play(self):
        if self.happiness < 91:
            self.happiness += 10
        else:
            self.happiness = 100

        if self.hunger < 91:
            self.hunger += 5
        else:
            self.hunger = 100

    def feed(self):
        if self.hunger > 10:
            self.hunger -= 10
        else:
            self.hunger = 0

    def giveMedicine(self):
        if self.happiness > 20:
            self.happiness -= 20
        else:
            self.happiness =0

        if self.health < 80:
            self.health += 20
        else:
            self.health = 100

    def sleep(self):
        if self.energy < 80:
            self.energy += 20
        else:
            self.energy =100

        self.age += 1

    def __str__(self):
        msg = "name: " + self.name + "\nhealth: " + str(self.health) + "\nhappiness: " + str(self.happiness) + "\nhunger: "
        msg += str(self.hunger) + "\nenergy: " + str(self.energy) + "\nage: " + str(self.age) + "\n********************************"
        return msg



def loadAnimals(fileName):
    fileName = "animals.csv"
    fin = open(fileName, "r")
    list = []
    for line in fin:
        line = line.strip()
        dataList = line.split(",")
        hunger = int(dataList[0])
        happiness = int(dataList[1])
        health = int(dataList[2])
        energy = int(dataList[3])
        age = int(dataList[4])
        name = dataList[5]
        species = dataList[6]

        animal = Animal(hunger, happiness, health, energy, age, name, species)
        list.append(animal)

    fin.close()

    return list


def displayMenu():
    print("""
1) Play
2) Feed
3) Give Medicine
4) Sleep
5) Print an Animal's stats
6) View All Animals
7) Exit

""")


def selectAnimal(list):
    fileName = "animals.csv"
    list = loadAnimals(fileName)
    print("""1) Ollie the Bunny
2) Murdock the French Bulldog
3) Socks the Cat
4) Peewee the Turtle
5) Milo the Labrador""")
    choice = int(input("Please select an animal from the list (enter the 1-5): "))
    while choice > 5 or choice < 1:
        print("Invalid input, please try again!")
        choice = int(input("Please select an animal from the list (enter the 1-5): "))
    return choice-1



#####Extra credit
# def fileout():
#     selectAnimal(list)
#     fout = open("out.csv", "w")
#     for i in
#
#     fout.close()



def main():
    fileName = "animals.csv"
    listAnimal = loadAnimals(fileName)
    print("Welcome to the Animal Daycare! Here is what we can do:")
    again = "y"
    while again =="y":
        displayMenu()
        choice = int(input("Pleae make a selection: "))
        while choice > 7 or choice < 1:
            print("*Invalid selection, please try again.")
            displayMenu()
            choice = int(input("Pleae make a selection: "))

        listName = ["Ollie the Bunny", "Murdock the French Bulldog", "Socks the Cat", "Peewee the Turtle", "Milo the Labrador"]
        if choice == 1:
            i = selectAnimal(list)
            Animal.play(listAnimal[i])
            print("You played with", listName[i])
        elif choice == 2:
            i = selectAnimal(list)
            Animal.feed(listAnimal[i])
            print("You fed", listName[i])
        elif choice == 3:
            i = selectAnimal(list)
            Animal.giveMedicine(listAnimal[i])
            print("You gave",listName[i],"some medicine!")
        elif choice == 4:
            i = selectAnimal(list)
            Animal.sleep(listAnimal[i])
            print(listName[i], "took a nap!")
        elif choice == 5:
            i = selectAnimal(list)
            print(listAnimal[i])
        elif choice == 6:
            for animal in listAnimal:
                print(animal)
        elif choice == 7:
            again = "n"
            print("Goodbye!")
            # fout = open("out.csv", "w")
            # for i in listAnimal:
            #     for k in listAnimal[i]:
            #         print(",".join(listAnimal[i]), file = fout)
            #
            # fout.close()




main()

