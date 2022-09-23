########################################################################
##
## CS 101 Lab
## Program #4
## Name: Marco Mera
## Email: mmv7v@umsystem.edu
##
## PROBLEM : Towards the end I coudn't figure out how to unite the Lab and the LabTest in order to Check it. Found many errors in the LabTest. Fixing these errors finally let me run the test.
##
## ALGORITHM : 
##       1. def play_again()->bool:
##       2. def get_wager(bank:int)->int:
##       3. def get_slot_results()->tuple: 
##       4. def get_matches(reela,reelb,reelc)->int: 
##       5. def get_bank()->int:
##       6. def get_payout(wager,matches):
##       7. if __name__=="__main__":
##       8. print("You lost all",start_chips,"in",count,"spins")
##       9. print("The most chips you had was",most) 
##       10. playing = play_again()
## ERROR HANDLING:
##      Didn't recieve any uncommon errors, most where just syntax errors.
##
## OTHER COMMENTS:
##      I liked this Lab, it was challenging and also due to this it took a longer time to comoplete. 
##
########################################################################
from random import randint
def play_again()->bool:       #Play again button(with options)
   play = input("Do you want to play again? ==> ").lower()
   options = ["n","y","no","yes"]      #Multiple choices for multiple answers
   if play not in options:
      print("\nYou must enter Y/YES/N/NO to continue. Please try again")
      return play_again()
   if (play=="yes" or play=="y"):
      return True
   return False
def get_wager(bank:int)->int:       #Amount of coins you want to bet
   chips = int(input("How many chips do you want to wager? ==> "))
   if(chips < 1):
      print("The wager amount must be greater than 0. Please enter again.")         #Wager can not be negative
      return get_wager(bank)
   elif (chips>bank):
      print("The wager amount cannot be greater than how much you have.",bank)      #Wager can not be above 100
      return get_wager(bank)
   return chips
def get_slot_results()->tuple:      #Function for the 3 numbers the reel will produce
   reel1 = randint(0,9)             #Number 1
   reel2 = randint(0,9)             #Number 2
   reel3 = randint(0,9)             #Number 3
   return reel1,reel2,reel3
def get_matches(reela,reelb,reelc)->int:     #The reel match for the outcome
   if (reela==reelb==reelc):
      return 3
   elif (reela==reelb or reela==reelc or reelb==reelc):
      return 2
   return 0
def get_bank()->int:       #Asking how many coins you want to have in your bank
   chips = int(input("How many chips do you want to start with? ==> "))
   if (chips<1):
      print("Too low a value, you can only choose 1 - 100 chips")
      return get_bank()
   elif (chips>100):
      print("Too high a value, you can only choose 1 - 100 chips")
      return get_bank()
   return chips
def get_payout(wager,matches):  #Checking what reels match in order to multiply to get the prize(Coins)
   if matches==3:
      return (wager*10)+(wager*-1)
   elif matches==2:
      return (wager*3)+(wager*-1)
   return wager*-1            #If no reels match then you lose all the coins you bet this round
if __name__=="__main__":
   playing = True          
   while playing:             #if still playing game will continue
      bank = get_bank()
      start_chips = bank
      most = bank
      count = 0
      while True:
         wager = get_wager(bank)
         reel1,reel2,reel3 = get_slot_results()
         matches = get_matches(reel1,reel2,reel3)
         payout = get_payout(wager,matches)
         bank = bank+payout
         print("Your spin",reel1,reel2,reel3)
         print("You matched",matches,"reels")
         print("You won/lost",payout)
         print("Current bank",bank)
         print()
         count = count+1
         if most<bank:
            most = bank
         if bank<1:           #If coins is less than 1 the game ends and the function stops
            break
      print("You lost all",start_chips,"in",count,"spins")        #Summary of your game and rounds 
      print("The most chips you had was",most)                    #The most amount of chips you had in a round
      playing = play_again()
