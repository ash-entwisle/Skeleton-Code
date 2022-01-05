# **How to Use**

This is a general document that outlines information for the Skeleton Code _(found in gamefiles\skeleton\_code.py)_ and a rundown of how it works and what it can be used for.
Further information about the code can be found in _preliminary\_material.pdf_

**Links to Sections:**
1. [timestamped notes on progress](https://github.com/async-def-init/Skeleton-Code#notes)
2. [outline of requirements and checklist](https://github.com/async-def-init/Skeleton-Code#overview)
3. [tutorial on how to use the python file](https://github.com/async-def-init/Skeleton-Code#how-to-play)
4. [breakdown of all the classes](https://github.com/async-def-init/Skeleton-Code#class-breakdown)
5. [trace of how the application starts up](https://github.com/async-def-init/Skeleton-Code#startup-process)
6. [predictions on possible questions](https://github.com/async-def-init/Skeleton-Code#predictions)

# **Notes**

```
[2021/12/15 14:00]: Taking first looks at code, added .md
[2021/12/15 14:20]: This code is not the worst, but awful
[2021/12/30 xx:xx]: Tried adding comments to code but gave up, started hand tracing
[2021/12/31 13:15]: Hand traced startup to __SetupGame() and can be found in run.md
```
# **Overview**

This document will cover the following:
```
    Identify the requirements of the task
    Analyse of the code:
        Identify the programming techniques used? - #Overview
        Can I use Hierarchy chart to break down the modules so I can understand and see the relation of how the sub routine is called? - #Class_Breakdown + [diagram i]
        Can I explain parameters and arguments within the skeleton code? - #Overview
        Can I identify constant and variables in the skeleton code? Can I explain why and how they are used? Reasons of used? - #Overview
        Can I explain how the code execute? Can I include test data in order to run the code? - steps.md
        Can I explain the object-oriented programming in the skeleton code? - #Overview
        How many classes are used? Can I explain its attributes? Can I explain what it does? - #Class_Breakdown
        Can I use class diagram to describe the relationships between some of the classes? [diagram ii]
        Can I explain aggregation, composition and inheritance? - #Overview
        Can I state the identifier in each class? - #Class_Breakdown

 

    Predicted Questions and answers
        Can I make a prediction of what will be asked of me in terms of modifying the skeleton code to solve a problem? - # Prediction
        Can I make a prediction of what they will ask me to solve using the programming techniques that I have learnt/to learn? - # Prediction
        Can I add a new class? Can I make a prediction about a  class that will be added to the given skeleton code? - ?????
```

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

# **Application Startup**
```
ln 469 checks then calls Main() func on line 9
Main() initialises the class Breakthrough() to ThisGame

__init__ runs and initialises these variables:
__Deck initialises instance CardCollection() wtih _Name == DECK
__Hand initialises instance CardCollection() with _Name == HAND
__Sequence initialises instance CardCollection() with _Name == SEQUENCE
__Discard initialises instance CardCollection() with _Name == DISCARD
__Score == 0
__Locks == []
__GameOver == False
__CurrentLock initialises instance Lock with _Challenges == []
__LockSolved == False
__LoadLocks() called 
    FileName == locks.txt
    sets __Locks == []
    tries:
        open FileName as f
        strips 1st line to LineFromFile
        Challenges == split LineFromFile with ;
        LockFromFile initialises instance Lock _Challenges == []
        Conditions == split Challenges with ,
        for each Challenge, run LocksFromFile.AddChallenge(conditiond)
            C initialised with Challenge() with _Met == False _Condition == []
            _Condition == each condition under Challenge
        Append LockFromFile to __Locks
        repeat from 21 until file is empty
    exept raise error "no file found"

Main() continues to execute 

PlayGame is called: #still working on all of this shit
if no locks in __Locks, raise error and output "File not loaded"
else:
call __SetupGame()
    ask user to load?
    If not loaded:
        
        call __CreateStandardDeck()


    If file loaded:
    __LoadGame("game1.txt") is called
        LineFromFile == line stripped
        __Score == LineFromFile
        LineFromFile == line stripped
        LineFromFile2 == line stripped

```


**lines called on startup**

```
ln 469 checked
ln 470 runs
ln 9 is called
ln 10 inits ln 13
ln 14 run
ln 15-23 init
ln 24 calls ln ln 154
ln 158 loads locks.txt 
```



# **Predictions**

As the OS module is imported but not used _(line 7)_, this could be an indicator of a possible question we may be asked. To fuffil this, it would be reccomended revising the OS module

We could be asked to implement a system to create and store games in .txt files as the game file is currently hard-coded to "game1.txt" _(see line 70-82)_. To fuffil this, it is reccomended to go over file read-write and the format the program stores the code.

Another possibility _(although unlikely)_ is to make a tutorial on how to play the game. Even though you can easily get the hang of the game, its best to know how everything works and be able to put it into words.

A class we could be asked to add is...



