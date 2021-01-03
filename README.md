# MFBA - Magnet Faculty Battle Arena

MFBA is a MOBA-style game written in [Processing.py](https://py.processing.org), with characters you know and love from Magnet High School, like Mr. Sanservino.

![map example](/img/MapExample.PNG)

### Presentation

The presentation can be found [here](https://docs.google.com/presentation/d/1IYn48w6rhyWR2i4wQwp98KQwt2uIdncMYtXzNo8GIo4/edit?usp=sharing).

### MLA Works Cited

The MLA works cited can be found [here](https://docs.google.com/document/d/1yPlwbJphD4gEpndE1LGwYaXe-jZQnb_xqFxa9Q-K_MU/edit?usp=sharing).

### Flowchart
Flowchart can be found [here](docs/flowchart)

# Features

### Object-Oriented Programming
This project makes heavy use of OOP. We can use the class `Entity` as an example. `Entity` is an object largely inherited to represent anything drawn on the screen. Entity's subclasses are used in the following fashion:

* `Entity` 
   * `Tree`
   * `Attackable`
       * `Mob`
           * `Player`
           * `Creep`
       * `Structure`
           * `Tower`
           * `Nexus`

This allows for most functions that all `Attackable` objects do (like attacking, debuff processing, etc.) to be inherited to all classes. The `Entity` class is used for movement and collisions checking on all objects at once.

Object "trackers" (like `PlayerTracker`, `StructureTracker`, `CreepTracker`, etc.) have a list of all elements they track and process the relevant functions for those elements every game tick.

### Networking
Processing's [network library](https://www.processing.org/reference/libraries/net/) also works for Processing.py. This allows for us to implement multiplayer. A single server instance to be running, and processing all game actions, while client code renders and displays the game to the players. Server does all computations in order to prevent cheating by tampering with packets.

### Pathfinding
![pathfinding example](/img/PathFind.PNG)
The map has a series of nodes throughout all of the lanes. The blue alliance creep traverse up the graph from node to node and the red alliance creep traverse downwards. If a player of an opposing alliance intercepts a creep, the creep will pathfind towards them. If the distance between the aggressor is too large, the creep will return to the previous node it was at.

# Download and Setup

## 1. Download Relevant Software 
### a. Download [processing](https://processing.org)

### b. Install Python Mode
* In the top right corner, select "Java", then add Mode:

![Adding Python Mode](img/Processing_mode.png)

* select Python Mode, then click "Install":

![Select Python Mode](img/Add_Python_Mode.png)

### c. Clone the Repository
```
git clone https://github.com/Azamlynny/MFBA.git
```

## 2. Start Server

### a. Open Server Code in Processing IDE
Server code found at [/src/Server/Driver](/src/Server/Driver)
### b. Run Server Code
Look for the play button in the top right corner of Processing IDE
### c. Note down Server IP
The IP is printed in the IDE console, but may indicate a loopback address. in this case, open your command prompt

#### i. Find IPv4 in Windows with cmd
Execute
```
ipconfig
```

![ipconfig on cmd](/img/Windows_cmd_ip.png)

#### ii. Find IPv4 in Linux (Bash)
Execute
```
ifconfig
```

![ifconfig on bash](/img/Linux_Bash_ip.png)

#### iii. Find IPv4 in MacOS
Execute
```
ifconfig
```

![ifconfig on MacOS](/img/MacOS_ip.png)

#### iv. Find IPv4 in Powershell
Execute
```
Get-NetIPAddress | Format-Table
```

![Get-NetIPAddress on Powershell](/img/windows_powershell.png)



Keep in mind that your local IP will look like one of the following:

![Credit to Wikipedia for the chart](/img/local_ips.png)



## 3. Start Client(s)

### a. Open Client Code in Processing IDE
* Client code found at [/src/Client/Driver](/src/Client/Driver)
### b. Run Client Code
* Running Client Code is the same as Server code. Just remember to replace the `ip` variable in Driver.pyde with the server's ip address.

## Controls
* __Mouse__
    * __Right Click__ will move your character. If you right click an Attackable (Player, Creep, Tower), your player will pathfind to attack it.
    * __Left Click__ will show the health of the object clicked on in the GUI.
    * __Middle Click__ + __Drag__ pans the camera.
* __Keyboard__
    * __W,A,S,D__ will pan the camera.
    * __Space__ will pan the camera onto your player
* __Developer Mode__ (Server only)
    * Tree editing
        * __J, K, L (simultaneously)__ will toggle tree editing mode.
        * __Left Click__ will place trees
        * __T__ will delete the trees saved in memory (Holding down for too long can result in mass tree deletion)
        * __O__ will write your current tree configuration to a txt file.
    * Pathfinding Node editing
        * __H, J, K (simultaneously)__ will toggle node editing mode.
        * __Left Click__ will place nodes
        * __P__ will save your current node configuration to a txt file.
