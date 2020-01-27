# MFBA - Magnet Faculty Battle Arena

MFBA is a MOBA-style game written in [Processing.py](https://py.processing.org), with characters you know and love from Magnet High School, like Mr. Sanservino.

### Presentation

The presentation can be found [here](https://docs.google.com/presentation/d/1IYn48w6rhyWR2i4wQwp98KQwt2uIdncMYtXzNo8GIo4/edit?usp=sharing).

### MLA Works Cited

The MLA works cited can be found [here](https://docs.google.com/document/d/1yPlwbJphD4gEpndE1LGwYaXe-jZQnb_xqFxa9Q-K_MU/edit?usp=sharing).

## Features

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
adam you do dis

## Play this Game

### 1. Download relevant software 
#### a. Download [processing](https://processing.org)

#### b. Install Python Mode
* In the top right corner, select "Java", then add Mode:

![Adding Python Mode](img/Processing_mode.png)

* select Python Mode, then click "Install":

![Select Python Mode](img/Add_Python_Mode.png)

#### c. Clone our repository
```
git clone https://github.com/Azamlynny/MFBA.git
```

### 2. Start Server

#### a. Open Server Code in Processing IDE
Server code found at [/src/Server/Driver](/src/Server/Driver)
#### b. Run Server Code
Look for the play button in the top right corner of Processing IDE
#### c. Note down Server IP
The IP is printed in the IDE console, but may indicate a loopback address. in this case, open your command prompt
##### i. Find IP in Windows with cmd
Run `ipconfig`:

![ipconfig on cmd](/img/Windows_cmd_ip.png)

##### ii. Find IP in Linux (Bash)
Run `ifconfig`:

![ifconfig on bash](/img/Linux_Bash_ip.png)

##### iii. Find IP in MacOS
Run `ifconfig`:

![ifconfig on MacOS](/img/MacOS_ip.png)

#### iv. Find IP in Powershell
Run `Get-NetIPAddress | Format-Table`:

![Get-NetIPAddress on Powershell](/img/windows_powershell.png)



Keep in mind that your local IP will look like one of the following:

![Credit to Wikipedia for the chart](/img/local_ips.png)



### Start Client(s)

#### a. Open Client Code in Processing IDE
* Client code found at [/src/Client/Driver](/src/Client/Driver)
##### b. Run Client Code
* Running Client Code is the same as Server code. Just remember to replace the `ip` variable in Driver.pyde with the server's ip address.

### Controls
* Mouse
    * __Right Click__ will move your character. If you right click an Attackable (Player, Creep, Tower), your player will pathfind to attack it.
    * __Left Click__ will use a special ability if selected. Otherwise, if you click an Attackable, you can see its GUI.
    * __Middle Click__ pans the camera.
* Keyboard
    * __Q__ will select special ability 1
    * __E__ will select special ability 2
    * __W,A,S,D__ will pan the camera.
    * __Space__ will lock the camera on your player
    * __Grave/Tilde (`/~)__ will deselect abilities
* Developer Mode (Server only)
    * Tree editing
        * __J, K, L (simultaneously)__ will toggle tree editing mode.
        * __Left Click__ will place trees
        * __T__ will delete the last tree placed
        * __O__ will write your current tree configuration to a txt file.
    * Pathfinding Node editing
        * ___H, J, K (simultaneously)__ will toggle node editing mode.
        * __Left Click__ will place nodes
        * __P__ will save your current node configuration to a txt file.
