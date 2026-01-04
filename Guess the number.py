import random

class guess_game():         #this class create the object of guess game where i can define each piece involved below
    def __init__(self):
        self.number = random.randint(1,10)
        self.count = 5

    def get_guess(self):
        while True:
            try:
             return  int(input("Enter a number between 1 and 10: "))  #if the user enters anything other than a number using a try and except will help to combat the code ending early
            except ValueError:
              print("Try again")

    def check(self,guess):
        if guess < self.number:     #this sections helps to define the loop of the outcomes available
             return "low"
        elif guess > self.number:
            return "high"
        else:
            return "correct"

    def play_again(self):
        while True:
            a = input("To play again type 'yes' and if not type 'no': ").lower() #this section is for the user to play again and defining it
            if a in ("yes","no"):
                return a
            print("Please type 'yes' or 'no':")

while True:   #start of a loop
  s = guess_game() #this defines the class giving s the value of the class to use


  while s.count > 0:      #now i can use s. to define all my class definitions from above
    good = s.get_guess()
    result = s.check(good)


    if result == "correct":
     print(f"Correct, the answer was {s.number}")
     break


    s.count -= 1 #this helps to decrease the attempt by 1 each time

    if result == "low":
      print(f"Too low, {s.count} attempts left") #using the formatted string will allow me to show how many attempts are left
    elif result == "high":
     print(f"Too high, {s.count} attempts left")


  else:
   print(f"Out of attempts, the number was {s.number}")

  if s.play_again() != "yes":   #if this is NOT eqaul to yes then the code will end
     print("Goodbye")
     break