# Skeleton Program code for the AQA A Level Paper 1 Summer 2022 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.9 programming environment
#! Best read in BetterComments because nice colours yay!

import random
import os                                           # import os 

#! main program function
#! ThisGame is defined as using the Breakthrough() class, therefore later calling PlayGame

def Main():
    ThisGame = Breakthrough()
    ThisGame.PlayGame()


#* Breakthrough class
#* init a bunch of attributes for later use including using the call to the CardCollection class
#* which takes the input and enters it as an attribute

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

#* PlayGame method

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

    def __ProcessLockSolved(self):                                                                  #* ProcessLockSolved method
        self.__Score += 10                                                                          #* Score is incremented by 10
        print("Lock has been solved.  Your score is now:", self.__Score)                            #* Print that the lock has been solved and the new score
        while self.__Discard.GetNumberOfCards() > 0:                                                #* While there are cards in the discard pile 
            self.__MoveCard(self.__Discard, self.__Deck, self.__Discard.GetCardNumberAt(0))         #* Move the card from the discard pile to the deck
        self.__Deck.Shuffle()                                                                       #* Shuffle the deck
        self.__CurrentLock = self.__GetRandomLock()                                                 #* Get a random lock and set it as the current lock

    def __CheckIfPlayerHasLost(self):                                                               #* CheckIfPlayerHasLost method
        if self.__Deck.GetNumberOfCards() == 0:                                                     #* If there are no cards in the deck
            print("You have run out of cards in your deck.  Your final score is:", self.__Score)    #* Print that you have run out of cards and the final score
            return True                                                                             #* Return True (game over)
        else:                                                                                       #* Else:
            return False                                                                            #* Return False (game not over)
    
    def __SetupGame(self):                                                                          #* SetupGame method
        Choice = input("Enter L to load a game from a file, anything else to play a new game:> ").upper() #* Get user input, convert to uppercase
        #! A QUESTION COULD BE ASKED HERE TO IMPLEMENT A SYSTEM TO IMPORT A GAME FROM A USER SPECIFIED FILE 
        if Choice == "L":                                                                           #* If user chooses to load a game
            if not self.__LoadGame("game1.txt"):                                                    #* load game1.txt 
                self.__GameOver = True                                                              #* GameOver is set to True
        
        else:                                                                                       #* if user chooses to play a new game
            self.__CreateStandardDeck()                                                             #* Call __CreateStandardDeck() method (creates a new deck)
            self.__Deck.Shuffle()                                                                   #* shuffles deck
            for Count in range(5):                                                                  #* draws top 5 cards
                self.__MoveCard(self.__Deck, self.__Hand, self.__Deck.GetCardNumberAt(0))           #* Move card from deck to hand
            self.__AddDifficultyCardsToDeck()                                                       #* Call __AddDifficultyCardsToDeck() method (adds difficulty cards to deck)
            self.__Deck.Shuffle()                                                                   #* re-shuffle deck
            self.__CurrentLock = self.__GetRandomLock()                                             #* sets current lock to random lock
    
    def __PlayCardToSequence(self, CardChoice):                                                     #? idfk what this func is, please help. this is a mess lol
        if self.__Sequence.GetNumberOfCards() > 0:                                                  #* If there are cards in the sequence
            if self.__Hand.GetCardDescriptionAt(CardChoice - 1)[0] != self.__Sequence.GetCardDescriptionAt(self.__Sequence.GetNumberOfCards() - 1)[0]:  #* If the card in the hand is not the same as the last card in the sequence
                self.__Score += self.__MoveCard(self.__Hand, self.__Sequence, self.__Hand.GetCardNumberAt(CardChoice - 1))  #* Move card from hand to sequence
                self.__GetCardFromDeck(CardChoice)                                                  #* Get card from deck
        else:                                                                                       #* Else:
            self.__Score += self.__MoveCard(self.__Hand, self.__Sequence, self.__Hand.GetCardNumberAt(CardChoice - 1))  #* Move card from hand to sequence
            self.__GetCardFromDeck(CardChoice)                                                      #* Get card from deck
        if self.__CheckIfLockChallengeMet():                                                        #* If the lock challenge is met
            print()                                                                                 #* Print a blank line
            print("A challenge on the lock has been met.")                                          #* Print that the lock challenge has been met
            print()                                                                                 #* Print a blank line
            self.__Score += 5                                                                       #* Score is incremented by 5

    def __CheckIfLockChallengeMet(self):                                                            #* checks if lock is is met from sequence 
        SequenceAsString = ""                                                                       #* creates a string to store the sequence
        for Count in range(self.__Sequence.GetNumberOfCards() - 1, max(0, self.__Sequence.GetNumberOfCards() - 3) -1, -1): #* loops through the sequence
            if len(SequenceAsString) > 0:                                                           #* if there is already a string
                SequenceAsString = ", " + SequenceAsString # bad string practices                   #* add a comma and a space to the string
            SequenceAsString = self.__Sequence.GetCardDescriptionAt(Count) + SequenceAsString       #* add the card to the string
            if self.__CurrentLock.CheckIfConditionMet(SequenceAsString):                            #* if the lock is met
                return True                                                                         #* return true
        return False                                                                                #* return false
    
    def __SetupCardCollectionFromGameFile(self, LineFromFile, CardCol):                             #* SetupCardCollectionFromGameFile method
        if len(LineFromFile) > 0:                                                                   #* If there is a line in the file
            SplitLine = LineFromFile.split(",")                                                     #* Split the line into a list around the commas
            for Item in SplitLine:                                                                  #* For each item in the list
                if len(Item) == 5:                                                                  #* If the item is 5 characters long
                    CardNumber = int(Item[4])                                                       #* Set the card number to the last character of the item
                else:                                                                               #* Else:
                    CardNumber = int(Item[4:6])                                                     #* Set the card number to the last two characters of the item
                if Item[0: 3] == "Dif":                                                             #* If the first three characters are "Dif"
                    CurrentCard = DifficultyCard(CardNumber)                                        #* Create a difficulty card
                    CardCol.AddCard(CurrentCard)                                                    #* Add the card to the collection
                else:                                                                               #* Else:
                    CurrentCard = ToolCard(Item[0], Item[2], CardNumber)                            #* Create a tool card
                    CardCol.AddCard(CurrentCard)                                                    #* Add the card to the collectionb
    
    def __SetupLock(self, Line1, Line2):
        SplitLine = Line1.split(";")                                                                #* Split the line into a list around the semicolons
        for Item in SplitLine:                                                                      #* For each item in the list
            Conditions = Item.split(",")                                                            #* Split the item into a list around the commas
            self.__CurrentLock.AddChallenge(Conditions)                                             #* Add the conditions to the lock
        SplitLine = Line2.split(";")                                                                #* Split the line into a list around the semicolons
        for Count in range(0, len(SplitLine)):                                                      #* For each item in the list
            if SplitLine[Count] == "Y":                                                             #* If the item is "Y"
                self.__CurrentLock.SetChallengeMet(Count, True)                                     #* Set the challenge met to true
    
    def __LoadGame(self, FileName):
        try:                                                                            #*Attempts to run the following, treating the filename as valid and workable
            with open(FileName) as f:
                LineFromFile = f.readline().rstrip()                                    #*f represents the line number incremented, and readline reads this and rstrip remove all whitespace
                self.__Score = int(LineFromFile)                                        #*Sets default score from txt
                LineFromFile = f.readline().rstrip()
                LineFromFile2 = f.readline().rstrip()
                self.__SetupLock(LineFromFile, LineFromFile2)
                LineFromFile = f.readline().rstrip()
                self.__SetupCardCollectionFromGameFile(LineFromFile, self.__Hand)
                LineFromFile = f.readline().rstrip()
                self.__SetupCardCollectionFromGameFile(LineFromFile, self.__Sequence)
                LineFromFile = f.readline().rstrip()
                self.__SetupCardCollectionFromGameFile(LineFromFile, self.__Discard)
                LineFromFile = f.readline().rstrip()
                self.__SetupCardCollectionFromGameFile(LineFromFile, self.__Deck)
                return True
        except:
        
            print("File not loaded")
            return False

    def __LoadLocks(self): #! Question could be asked here to load custom locks
        FileName = "locks.txt"                                                          #* Sets the file name
        self.__Locks = []                                                               #* Creates a list to store the locks
        try:                                                                            #*Attempts to run the following, treating the filename as valid and workable
            with open(FileName) as f:                                                   #* opens the file
                LineFromFile = f.readline().rstrip()                                    #* read and strip the first line
                while LineFromFile != "":                                               #* while the line is not empty
                    Challenges = LineFromFile.split(";")                                #* split the line into a list around the semicolons
                    LockFromFile = Lock()                                               #* create a lock
                    for C in Challenges:                                                #* for each challenge
                        Conditions = C.split(",")                                       #* split the challenge into a list around the commas
                        LockFromFile.AddChallenge(Conditions)                           #* add the challenge to the lock
                    self.__Locks.append(LockFromFile)                                   #* add the lock to the list
                    LineFromFile = f.readline().rstrip()                                #* read and strip the next line
        except:                                                                         #* if the file is not found
            print("File not loaded")                                                    #* print that the file was not loaded
        
    def __GetRandomLock(self): #* picks random lock
        return self.__Locks[random.randint(0, len(self.__Locks) - 1)]

    def __GetCardFromDeck(self, CardChoice): # idfk what to do here lo  l
        if self.__Deck.GetNumberOfCards() > 0:                                          #* if there are cards in the deck
            if self.__Deck.GetCardDescriptionAt(0) == "Dif":                            #* if the first card is a difficulty card
                CurrentCard = self.__Deck.RemoveCard(self.__Deck.GetCardNumberAt(0))    #* remove the card from the deck
                print()                                                                 #* print a new line
                print("Difficulty encountered!")                                        #* print that a difficulty card was encountered
                print(self.__Hand.GetCardDisplay())                                     #* print the hand
                print("To deal with this you need to either lose a key ", end='')       #* print that you need to lose a key
                Choice = input("(enter 1-5 to specify position of key) or (D)iscard five cards from the deck:> ")   #* ask the user to choose a key
                print()                                                                 #* print a new line
                self.__Discard.AddCard(CurrentCard)                                     #* add the card to the discard pile
                CurrentCard.Process(self.__Deck, self.__Discard, self.__Hand, self.__Sequence, self.__CurrentLock, Choice, CardChoice)  #* process the card
        while self.__Hand.GetNumberOfCards() < 5 and self.__Deck.GetNumberOfCards() > 0:    #* while the hand is less than 5 cards and there are cards in the deck
            if self.__Deck.GetCardDescriptionAt(0) == "Dif":                            #* if the first card is a difficulty card
                self.__MoveCard(self.__Deck, self.__Discard, self.__Deck.GetCardNumberAt(0))    #* move the card to the discard pile
                print("A difficulty card was discarded from the deck when refilling the hand.") #* print that a difficulty card was discarded
            else:                                                                       #* else
                self.__MoveCard(self.__Deck, self.__Hand, self.__Deck.GetCardNumberAt(0))   #* move the card to the hand
        if self.__Deck.GetNumberOfCards() == 0 and self.__Hand.GetNumberOfCards() < 5:  #* if there are no cards in the deck and the hand is less than 5 cards
            self.__GameOver = True                                                      #* set the game over flag to true

    def __GetCardChoice(self):                                                          #* specifies what card choice
        Choice = None                                                                   #* sets the choice to none  
        while Choice is None:                                                           #* while the choice is none
            try:                                                                        #* try
                Choice = int(input("Enter a number between 1 and 5 to specify card to use:> ")) #* ask the user to enter a number between 1 and 5
            except:                                                                     #* if the user enters something other than a number
                pass                                                                    #* do nothing
        return Choice                                                                   #* return the choice

    def __GetDiscardOrPlayChoice(self):                                                 #* choice of discard/play
        Choice = input("(D)iscard or (P)lay?:> ").upper()                               #* ask the user to choose discard or play
        return Choice                                                                   #* return the choice

    def __GetChoice(self):                                                              #* use/discard
        print()                                                                         #* print a new line
        Choice = input("(D)iscard inspect, (U)se card:> ").upper()                      #* ask the user to choose discard or use
        return Choice                                                                   #* return the choice
    
    def __AddDifficultyCardsToDeck(self): # idfk abt this sorta stuff
        for Count in range(5):
            self.__Deck.AddCard(DifficultyCard())

    def __CreateStandardDeck(self): #* init deck
        for Count in range(5):
            NewCard = ToolCard("P", "a")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("P", "b")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("P", "c")
            self.__Deck.AddCard(NewCard)
        for Count in range(3):
            NewCard = ToolCard("F", "a")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("F", "b")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("F", "c")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("K", "a")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("K", "b")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("K", "c")
            self.__Deck.AddCard(NewCard)
    
    def __MoveCard(self, FromCollection, ToCollection, CardNumber): #* moves card from set to set (i.e. deck to hand)
        Score  = 0
        if FromCollection.GetName() == "HAND" and ToCollection.GetName() == "SEQUENCE":
            CardToMove = FromCollection.RemoveCard(CardNumber)
            if CardToMove is not None:
                ToCollection.AddCard(CardToMove)
                Score = CardToMove.GetScore()
        else:
            CardToMove = FromCollection.RemoveCard(CardNumber)
            if CardToMove is not None:
                ToCollection.AddCard(CardToMove)
        return Score


#* getter/setter for challenge conditions
#* challenge initialised -> condition set  
class Challenge():
    def __init__(self):
        self._Met = False
        self._Condition = []
    
    def GetMet(self): 
        return self._Met

    def GetCondition(self):
        return self._Condition

    def SetMet(self, NewValue):
        self._Met = NewValue

    def SetCondition(self, NewCondition):
        self._Condition = NewCondition


class Lock():
    def __init__(self):
        self._Challenges = []                                                   #* initialises challenges var
        
    def AddChallenge(self, Condition):                                          #* inherits from Challenge(), sets condition and appends val
        C = Challenge()
        C.SetCondition(Condition)
        self._Challenges.append(C)

    def __ConvertConditionToString(self, C):                                    #* formatting to be able to use condition as string
        ConditionAsString = ""                                                  #* initialises string
        for Pos in range(0, len(C) - 1):                                        #* -1 to avoid comma at end
            ConditionAsString += C[Pos] + ", "                                  #* adds condition to string
        ConditionAsString += C[len(C) - 1]                                      #* adds last element
        return ConditionAsString                                                #* returns string

    def GetLockDetails(self):
        LockDetails = "\n" + "CURRENT LOCK" + "\n" + "------------" + "\n"      #* Basic variable to assist with formatting
        for C in self._Challenges:                                              #* C is an attribute of the AddChallenge method
            if C.GetMet():
                LockDetails += "Challenge met: "                                #* Prints if challenge met/not met
            else:
                LockDetails += "Not met:       "                                #* Prints if challenge met/not met
            LockDetails += self.__ConvertConditionToString(C.GetCondition()) + "\n" #* getslock details
        LockDetails += "\n"                                                     # formatting
        return LockDetails                                                      #* Finally returns the details of the lock stored in above variables

    def GetLockSolved(self):                                                    # not sure what this bit does
        for C in self._Challenges:                                              #* for C in challenges
            if not C.GetMet():                                                  #* if not met
                return False                                                    #* return false
        return True                                                             #* else return true
    
    def CheckIfConditionMet(self, Sequence):                                    # same here as well
        for C in self._Challenges:                                              #* for C in challenges
            if not C.GetMet() and Sequence == self.__ConvertConditionToString(C.GetCondition()): #* if not met and sequence is same as condition
                C.SetMet(True)                                                  #* set met to true
                return True                                                     #* return true
        return False                                                            #* else return false

    def SetChallengeMet(self, Pos, Value):
        self._Challenges[Pos].SetMet(Value)                                     #* sets met to value
    
    def GetChallengeMet(self, Pos): 
        return self._Challenges[Pos].GetMet()                                   #* returns if met or not met
    
    def GetNumberOfChallenges(self): 
        return len(self._Challenges)                                            #* returns number of challenges

class Card():
    _NextCardNumber = 0
    
    def __init__(self):
        self._CardNumber = Card._NextCardNumber                                 #* sets card number 
        Card._NextCardNumber += 1                                               #* increments card number 
        self._Score = 0                                                         #* sets score to 0

    def GetScore(self):
        return self._Score                                                      #* returns score

    def Process(self, Deck, Discard, Hand, Sequence, CurrentLock, Choice, CardChoice):
        pass                                                                      #* abstract method to be overridden by subclasses     

    def GetCardNumber(self): 
        return self._CardNumber                                                 #* returns card number

    def GetDescription(self):
        if self._CardNumber < 10:                                               #* if card number is less than 10, 
            return " " + str(self._CardNumber)                                  #* adds a space before the number
        else:                                                                   #* otherwise
            return str(self._CardNumber)                                        #* returns the number

class ToolCard(Card):
    def __init__(self, *args):                                                  #* initialises tool card
        self._ToolType = args[0]                                                #* sets tool type to first argument
        self._Kit = args[1]                                                     #* sets kit to second argument
        if len(args) == 2:                                                      #* if no score is given
            super(ToolCard, self).__init__()                                    #* initialises card
        elif len(args) == 3:                                                    #* if score is given    
            self._CardNumber = args[2]                                          #* sets card number to third argument
        self.__SetScore()                                                       #* sets score
        
    def __SetScore(self):
        if self._ToolType == "K":                                               #* if tool type is K
            self._Score = 3                                                     #* sets score to 3
        elif self._ToolType == "F":                                             #* if tool type is F
            self._Score = 2                                                     #* sets score to 2
        elif self._ToolType == "P":                                             #* if tool type is P
            self._Score = 1                                                     #* sets score to 1
            
    def GetDescription(self):                                                   #* returns description of tool card
        return self._ToolType + " " + self._Kit                                 #* returns tool type and kit

class DifficultyCard(Card):                                                 
    def __init__(self, *args):                                                  #* initialises difficulty card
        self._CardType = "Dif"                                                  #* sets card type to Dif
        if len(args) == 0:                                                      #* if no args are given
            super(DifficultyCard, self).__init__()                              #* initialises card
        elif len(args) == 1:                                                    #* if score is given
            self._CardNumber = args[0]
        
    def GetDescription(self):
        return self._CardType                                                   #* returns description of difficulty card

    def Process(self, Deck, Discard, Hand, Sequence, CurrentLock, Choice, CardChoice):
        ChoiceAsInteger = None                                                  #* initialises choice as integer
        try:                                                                    #* tries to convert choice to integer
            ChoiceAsInteger = int(Choice)                                       #* if it can, sets choice as integer
        except:                                                                 #* if it can't,
            pass                                                                #* does nothing
        if ChoiceAsInteger is not None:                                         #* if choice is an integer
            if ChoiceAsInteger >= 1 and ChoiceAsInteger <= 5:                   #* if choice is between 1 and 5
                if ChoiceAsInteger >= CardChoice:                               #* if choice is greater than or equal to card choice
                    ChoiceAsInteger -= 1                                        #* subtracts 1 from choice
                if ChoiceAsInteger > 0:                                         #* if choice is greater than 0
                    ChoiceAsInteger -= 1                                        #* subtracts 1 from choice
                if Hand.GetCardDescriptionAt(ChoiceAsInteger)[0] == "K":        #* if choice is a kit
                    CardToMove = Hand.RemoveCard(Hand.GetCardNumberAt(ChoiceAsInteger)) #* removes card from hand
                    Discard.AddCard(CardToMove)                                 #* adds card to discard
                    return
        Count = 0                                                               #* initialises count
        while Count < 5 and Deck.GetNumberOfCards() > 0:                        #* while count is less than 5 and deck has cards
            CardToMove = Deck.RemoveCard(Deck.GetCardNumberAt(0))               #* removes card from deck
            Discard.AddCard(CardToMove)                                         #* adds card to discard
            Count += 1                                                          #* increments count

class CardCollection():
    def __init__(self, N):                                                      #* initialises card collection
        self._Name = N                                                          #* sets name to N
        self._Cards = []                                                        #* sets cards to empty list

    def GetName(self):                                                          #* returns name
        return self._Name                                                       #* returns name

    def GetCardNumberAt(self, X):                                               #* returns card number at X
        return self._Cards[X].GetCardNumber()                                   #* returns card number at X

    def GetCardDescriptionAt(self, X):                                          #* returns card description at X
        return self._Cards[X].GetDescription()                                  #* returns card description at X

    def AddCard(self, C):                                                       #* adds card C to collection
        self._Cards.append(C)                                                   #* adds card C to collection
    
    def GetNumberOfCards(self):                                                 #* returns number of cards
        return len(self._Cards)                                                 #* returns number of cards

    def Shuffle(self):                                                          #* shuffles collection
        for Count in range(10000):                                              #* for each count
            RNo1 = random.randint(0, len(self._Cards) - 1)                      #* sets random number 1
            RNo2 = random.randint(0, len(self._Cards) - 1)                      #* sets random number 2
            TempCard = self._Cards[RNo1]                                        #* sets temp card to random number 1
            self._Cards[RNo1] = self._Cards[RNo2]                               #* sets random number 1 to random number 2
            self._Cards[RNo2] = TempCard                                        #* sets temp card to random number 1

    def RemoveCard(self, CardNumber):                                           #* removes card with card number CardNumber
        CardFound  = False                                                      #* initialises card found
        Pos  = 0                                                                #* initialises pos
        while Pos < len(self._Cards) and not CardFound:                         #* while pos is less than length of cards and card not found
            if self._Cards[Pos].GetCardNumber() == CardNumber:                  #* if card at pos has card number CardNumber
                CardToGet = self._Cards[Pos]                                    #* sets card to get to card at pos
                CardFound = True                                                #* sets card found to true
                self._Cards.pop(Pos)                                            #* removes card at pos
            Pos += 1                                                            #* increments pos
        return CardToGet                                                        #* returns card to get

    def __CreateLineOfDashes(self, Size):                                       #* creates line of dashes of size Size
        LineOfDashes = ""                                                       #* initialises line of dashes
        for Count in range(Size):                                               #* for each count
            LineOfDashes += "------"                                            #* adds dash to line of dashes
        return LineOfDashes                                                     #* returns line of dashes
    
    def GetCardDisplay(self):                                                   #* returns card display
        CardDisplay = "\n" + self._Name + ":"                                   #* Variable steals the name of the card given (defined in the class' attribute from use of class elsewhere)
        if len(self._Cards) == 0:                                               #* if no cards
            return CardDisplay + " empty" + "\n" + "\n"                         #* Returns card values
        else:                                                                   #* if cards
            CardDisplay += "\n" + "\n"                                          #* adds new line
        LineOfDashes = ""           #? Yet again why this janky formatting??? *later edit - predefining variable for later use
        CARDS_PER_LINE  = 10                                                    #* Maximum cards defined here
        if len(self._Cards) > CARDS_PER_LINE:                                   #* If length of cards is greater than 10 state length of line of dashes = 10
            LineOfDashes = self.__CreateLineOfDashes(CARDS_PER_LINE)            #* LineOfDashes line is set to current CARDS_PER_LINE variable
        else:                                                                   #* else        
            LineOfDashes = self.__CreateLineOfDashes(len(self._Cards))          #* LineOfDashes line is set to current length of cards
        CardDisplay += LineOfDashes + "\n"                                      #* Adds line of dashes to card display and new line
        Complete = False                                                        #* initialises complete
        Pos  = 0                                                                #* initialises pos
        while not Complete:                                                     #* while not complete
            CardDisplay += "| " + self._Cards[Pos].GetDescription() + " "       #* adds card description to card display
            Pos += 1                                                            #* increments pos
            if Pos % CARDS_PER_LINE == 0:                                       #* if pos is divisible by 10
                CardDisplay += "|" + "\n" + LineOfDashes + "\n"                 #* adds new line and line of dashes
            if Pos == len(self._Cards):                                         #* if pos is equal to length of cards
                Complete = True                                                 #* sets complete to true
        if len(self._Cards) % CARDS_PER_LINE > 0:                               #* if length of cards is not divisible by 10
            CardDisplay += "|" + "\n"                                           #* adds new line
            if len(self._Cards) > CARDS_PER_LINE:                               #* if length of cards is greater than 10
                LineOfDashes = self.__CreateLineOfDashes(len(self._Cards) % CARDS_PER_LINE) #* LineOfDashes line is set to current length of cards modulo CARDS_PER_LINE
            CardDisplay += LineOfDashes + "\n"                                  #* Adds line of dashes to card display and new line
        return CardDisplay                                                      #* returns card display

if __name__ == "__main__":                                                      #* if main
    Main()                                                                      #* runs main
