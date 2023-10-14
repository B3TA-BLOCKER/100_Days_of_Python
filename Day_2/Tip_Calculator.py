from os import system

system('cls')
print("Welcome to tip Calculator")
bill=input("What was the total bill? $")
tip=input("What percentage tip would you like to give? 10%, 12%, 15% ")
people=input("How many people to split the bill? ")

bill_with_tip = float(bill) + (float(bill) * (int(tip)/100))
bill_for_each= bill_with_tip/int(people)
final= round(bill_for_each,2)
final="{:.2f}".format(bill_for_each)
print(f"Each person should pay : ${final}")