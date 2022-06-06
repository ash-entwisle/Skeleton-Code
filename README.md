# **How to Use**

This is a general document that outlines information for the Skeleton Code _(found in gamefiles\skeleton\_code.py)_ and a rundown of how it works and what it can be used for.  
Further information about the code can be found in _preliminary\_material.pdf_.  
If you have any examples you want me to go through, feel free to DM me on twitter, or send me an email

**Links to Sections:**
1. [timestamped notes on progress](https://github.com/async-def-init/Skeleton-Code#notes)
2. [outline of requirements and checklist](https://github.com/async-def-init/Skeleton-Code#overview)
3. [tutorial on how to use the python file](https://github.com/async-def-init/Skeleton-Code#how-to-play)
4. [breakdown of all the classes](https://github.com/async-def-init/Skeleton-Code#class-breakdown)
5. [trace of how the application starts up](https://github.com/async-def-init/Skeleton-Code#application-startup)
6. [predictions on possible questions](https://github.com/async-def-init/Skeleton-Code#predictions)

# **Notes**

```
[2021/12/15 14:00]: Taking first looks at code, added .md
[2021/12/15 14:20]: This code is not the worst, but awful
[2021/12/30 xx:xx]: Tried adding comments to code but gave up, started hand tracing
[2021/12/31 13:15]: Hand traced startup to __SetupGame() and can be found in run.md
[2022/01/05 17:00]: After forgetting to commit stuff for abt an hr, it is all up to date
[2022/06/01 11:39]: ive not been here for a while, a whole bunch of stuff has been updated and happy pride month 🏳️‍🌈🏳️‍⚧️ 
                    new stuff includes example questions (commented out in the code)
[2022/06/06 14:35]: Added another example to fix the error caused (see ln:312)
```
# **Overview**

This is the AQA A-Level skeleton code and ZigZag material
The code is the source code to a game called 'breakthrough'

This application is coded in python and is a text-based card game
The application uses OOP as the application is divided up into classes.

Parameters are values passed into the function, an example is in __LoadGame("Game1.txt") where the parameter is the value you put into FileName
An argument is the name of the variable used inside the function, an example of this is in __LoadGame(FileName) where FileName is the variable argument filled by the parameter which is used later in the function.



# **How to Play**




# **Class Breakdown**

```
Breakthrough()
    Requires no aditional parameters when initialised
    Initialises 4 instances of CardCollection()
    PlayGame() sets up all the game by calling __SetupGame() 
    PlayGame() also displays the main menu while __GameOver == False __LockSolved == False
    PlayGame() also handles all calls to private functions that make the game playable
    __PricessLockSolved() updates users points tally...
    __CheckIfPlayerHasLost() checks if cards left in deck, if not it ends game + shows score
    __SetupGame() can load a game from file
    __SetupGame() if not loads a game, gives player a deck, hand and sets difficulty



```



# Class: Breakthrough

This class is the main class of the application.
when initialised it creates 4 instances of CardCollection() (deck, hand, discard and solved)
it also sets score to 0 and gameOver to False
it initialises an empty list of locks
...

```py
class Breakthrough():
    def __init__(self):
        self.__Deck = CardCollection("DECK")            # * Deck is a CardCollection object
        self.__Hand = CardCollection("HAND")            # * Hand is a CardCollection object
        self.__Sequence = CardCollection("SEQUENCE")    # * Sequence is a CardCollection object
        self.__Discard = CardCollection("DISCARD")      # * Discard is a CardCollection object 
        self.__Score = 0                                # * Score is an integer (default 0)
        self.__Locks = []                               # * Locks is a list of Lock objects (default empty)
        self.__GameOver = False                         # * GameOver is a boolean  (True if game is over)
        self.__CurrentLock = Lock()                     # * CurrentLock is a Lock object
        self.__LockSolved = False                       # * LockSolved is a boolean (used to make sure no problems caused by LockSolved being True)
        self.__LoadLocks()                              # * LoadLocks is a method that loads the locks from the file "locks.txt"
```

the class has a PlayGame() method.
if there are locks in the game, it will call __SetupGame()


```py
    def PlayGame(self):
        if len(self.__Locks) > 0:                                                                   #* If length of the locks file is greater than 0:
            self.__SetupGame()                                                                      #* Call __SetupGame() method (else feedback that there are no locks in the file)
            while not self.__GameOver:
                self.__LockSolved = False                                                           #* Attibute modified to make sure no problems caused by LockSolved being True
                while not self.__LockSolved and not self.__GameOver:
                    print()                                                                         #? unrelated but why line break like this???
                    print("Current score:", self.__Score)
                    print(f"Cards Left: {self.__Deck.GetNumberOfCards()}")                          #* Bunch of printed details from methods
                    print(self.__CurrentLock.GetLockDetails())                                      #* GetLockDetails Line 300
                    print(self.__Sequence.GetCardDisplay())                                         #* GetCardDisplay Line 
                    print(self.__Hand.GetCardDisplay())                                             #* GetCardDisplay Line 
                    MenuChoice = self.__GetChoice()                                                 #* GetChoice from usr
                    if MenuChoice == "D":                                                           #* If user chooses to discard a card
                        print(self.__Discard.GetCardDisplay())                                      #* Display the discard pile and discard card
                    elif MenuChoice == "U":                                                         #* If user chooses to use a card
                        CardChoice  = self.__GetCardChoice()                                        #* GetCardChoice from user
                        DiscardOrPlay = self.__GetDiscardOrPlayChoice()                             #* GetDiscardOrPlayChoice from user
                        if DiscardOrPlay == "D":                                                    #* If user chooses to discard card
                            self.__MoveCard(self.__Hand, self.__Discard, self.__Hand.GetCardNumberAt(CardChoice - 1)) #* Move card from hand to discard
                            self.__GetCardFromDeck(CardChoice)                                      #* Get card from deck
                        elif DiscardOrPlay == "P":                                                  #* If user chooses to play card
                            self.__PlayCardToSequence(CardChoice)                                   #* Play card to sequence
                    if self.__CurrentLock.GetLockSolved():                                          #* If current lock is solved
                        self.__LockSolved = True                                                    #* Attribute modified to make sure no problems caused by LockSolved being True
                        self.__ProcessLockSolved()                                                  #* Call __ProcessLockSolved() method, saying that the lock has been solved
                self.__GameOver = self.__CheckIfPlayerHasLost()                                     #* Check if player has lost
        else:                                                                                       #* Else:
            print("No locks in file.")                                                              #* Print that there are no locks in the file
```



