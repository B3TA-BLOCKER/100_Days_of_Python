
from os import system

system('cls')
import random
num=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)
if num==0:
   print("    _______")
   print("---'   ____)")
   print("      (_____)")
   print("      (_____)")
   print("      (____)")
   print("---.__(___)")
elif num==1:
    print("    _______")
    print("---'   ____)____")
    print("          ______)")
    print("          _______)")
    print("         _______)")
    print("---.__________)")
elif num==2:
    print("    _______")
    print("---'   ____)____")
    print("          ______)")
    print("       __________)")
    print("      (____)")
    print("---.__(___)")
else :
    print("Error")


print("Computer Choice")

if computer_choice==0:
   print("    _______")
   print("---'   ____)")
   print("      (_____)")
   print("      (_____)")
   print("      (____)")
   print("---.__(___)")
elif computer_choice==1:
    print("    _______")
    print("---'   ____)____")
    print("          ______)")
    print("          _______)")
    print("         _______)")
    print("---.__________)")
elif computer_choice==2:
    print("    _______")
    print("---'   ____)____")
    print("          ______)")
    print("       __________)")
    print("      (____)")
    print("---.__(___)")


if num==0 and computer_choice==2:
    print("You win!")
elif computer_choice>num:
    print("You Lose!")
elif computer_choice==num:
    print("It's a draw")