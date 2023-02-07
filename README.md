# 0x00. AirBnB clone - The console

Welcome to part 1 of many projects that make up the beginning
of a clone AirBnB.
This project is hosted by Holberton School.
```
Here we will do a small breakdown on how to open our console 
and how to use interactive mode as well as non-interactive.
```
![hbnb](https://user-images.githubusercontent.com/91517809/176107896-998e3280-f565-4e09-a801-c609984bfed6.png)

## Installation

> Step 1 - Clone the repo locally using this command
```
gh repo clone kkeas/holbertonschool-AirBnB_clone
```
> Step 2 - Navigate to the folder
```
cd holbertonschool-AirBnB_clone
```
> Step 3 - Run the console shell in interactive mode:
```
./console.py
```
> Step 4 - Type a command e.g.
```
(hbnb) help
```
> Step 5 - Exit the shell
```
(hbnb) quit
```

<h2>Objective</h2>

The AirBnB clone project's goal is to deploy on your server a simple copy of the AirBnB website.
You won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.
Beginning with these fundamental steps:

</p>

## TABLE OF CONTENTS
<p>
</details>

<details><summary>Description of Installation </summary>

<p>

<h2>How to Install:</h2>

You will be using Ubuntu 20.04 with python3, you can work locally or through a sandbox.

</details>

<details><summary>Description of The console </summary>

<p>

<h2>The console</h2>

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

</p>
</details>

<details><summary>Description of Interactive Mode </summary>

<p>

<h2>Interactive Mode</h2>

In the interactive mode, the console will display (hbnb) prompting the user to type in and execute a command. After the command is run, the prompt (hbnb) will appear again in a new line waiting for a new command to be entered. As long as the user doesn't quit the shell (by typing quit and pressing enter), this will go indefinitely.
</p>

</details>

<details><summary> Description of Non-interactive Mode</summary>

<p>

<h2>Non-interactive Mode</h2>
In the non-interactive mode, the console is run with a command pipped into into its execution - this way the command is run as soon as the shell starts. In this mode no prompt (hbnb) appears, and no further input is expected from the user.
</details>
</p>


## Files included w/descriptions:
The console contains the entry point of the interpreter, the list of commands
the interpreter supports are as follows:
* `EOF` - exits console
* `quit` - exits console
* `create` - Creates a new instance of`BaseModel`, saves it (to the JSON file) and prints the id
* `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file). 
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representation of all instances based or not on the class name. 
* `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). 


## Testing:
All files, classes and functions can be tested with unit tests.

**Interactive mode:** 
```
python3 -m unittest discover tests
```

**Non-interactive mode** 
```
echo "python3 -m unittest discover tests" | bash
```
## Contributors
Katrina Keas & Johanna Avila
