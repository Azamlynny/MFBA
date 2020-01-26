# MFBA
## Magnet Faculty Battle Arena

MFBA is a MOBA-style game written in [Processing.py](https://py.processing.org), with characters you know and love from Magnet High School, like Mr. Sanservino.

Presentation is found [here](https://docs.google.com/presentation/d/1IYn48w6rhyWR2i4wQwp98KQwt2uIdncMYtXzNo8GIo4/edit?usp=sharing).

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

## Play this Game
To play this game, clone this repository, and make sure you have [Processing](https://processing.org/download/) and its [Python Mode](https://py.processing.org/) installed. 

Then, open and start the server up, and note that computer's local IP address. This computer also has developer priveliges, so you can use the key combination \[Insert key combo\] to edit the map's trees, and \[Insert key combo\] to edit the pathfinding nodes.

Next, open and start the client, replacing the `ip` variable in Driver.pyde to the server's IP address. You will then connect, and be given control of one of 10 players, connecting in ascending order. Players 0-4 are blue team, 5-9 are red team.
