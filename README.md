# MFBA
## Magnet Faculty Battle Arena

MFBA is a MOBA-style game written in [Processing.py](https://py.processing.org), with characters you know and love from Magnet High School, like Mr. Sanservino.

## Features

### Object-Oriented Programming
This project makes heavy use of OOP. We can use the example of Attackables. Anything attackable is in the class attackable, and each type of attackable inherits from attackable in the following fasion:

* `Attackable`
    * `Mob`
        * `Player`
        * `Creep`
    * `Structure`
        * `Tower`
        * `Nexus`

This allows for most functions that all attackables do (like attacking, debuff processing, etc.) to be inherited to all classes. Similarly, almost everything inherits from the `Entity` class. That way, movement, collisions, etc. on all objects at once.

We also created classes for "trackers" (like PlayerTracker, StructureStracker, etc.) that are called in the main driver code. Each one of these has a list of all elements it tracks, and processes the relevant functions for those elements every game tick.

### Networking
Processing's [network library](https://www.processing.org/reference/libraries/net/) also works for Processing.py. This allows for us to implement multiplayer. A single server instance to be running, and processing all game actions, while client code renders and displays the game to the players. Server does all computations in order to prevent cheating by tampering with packets.


### Pathfinding
adam you do dis

