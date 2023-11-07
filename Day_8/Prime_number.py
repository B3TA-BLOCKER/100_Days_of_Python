#Function for checking the number 

def prime_checker(number):
  flag = False
  for i in range(2, number):
    if number % i == 0:
      flag = True
      break
  if flag:
    print("It's not a prime number. ")
  else:
    print("It's a prime number. ")


n = int(input("Enter a Number : ")) # Check this number
prime_checker(number=n)