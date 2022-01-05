# **startup process**
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













# **lines called on startup**

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