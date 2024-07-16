#Shaan Shafi
#Initialization
import random 
#functions

def play():

    guesser = random.randint(1,5)
    if guesser == 1:
         ciaTheoryBait()
    if guesser == 2:
         joeRoganbait()
    if guesser == 3:
         bestJobsBait()
    if guesser == 4:
         fakeMoonLanding()
    if guesser == 5: 
         waitWhosaLizard()

def ciaTheoryBait():
        noun = input("pick a pronoun: (He/She/They)")
        country = input("pick a country")
        verb = input("pick a verb")
        print(noun," over threw the government of ",country,"to ", verb)

def joeRoganbait():
        noun = input("Say a random object or person")
        print(noun," behind the reason of the American Revolution?")

def bestJobsBait():
        number = input("Enter a number:")
        city = input("Enter a city:")
        job = input("Enter anytype of job:")
        print(" top",number, " best", job, "in", city)

def fakeMoonLanding():
        name = input ("Enter any name")
        print(name, "beat the Americans and Soviets to the moon miles ahead?")

def waitWhosaLizard():
        name2 = input("Enter any name")
        print(name2, "is secretly a lizard :3")
#Main
play() 

