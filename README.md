# 0x00. AirBnB clone - The console
# 0x00. AirBnB clone - The console

Welcome to part 1 of many projects that make up the beginning
of a clone AirBnB.
This project is hosted by Holberton School.
```
Here we will do a small breakdown on how to open our console 
and how to use interactive mode as well as non-interactive.
```
![hbnb](https://user-images.githubusercontent.com/91517809/176107896-998e3280-f565-4e09-a801-c609984bfed6.png)

<h2>Objective</h2>

The AirBnB clone project's goal is to deploy on your server a simple copy of the AirBnB website.
You won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.
Beginning with these fundamental steps:

</p>
# TABLE OF CONTENTS
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

<h2>Interactive Mode</h2>

In the interactive mode, the console will display (hbnb) prompting the user to type in and execute a command. After the command is run, the prompt (hbnb) will appear again in a new line waiting for a new command to be entered. As long as the user doesn't quit the shell (by typing quit and pressing enter), this will go indefinitely.
</p>

</details>

<details><summary> Description of interactive mode</summary>

<p>

<h2>Non-interactive Mode</h2>
In the non-interactive mode, the console is run with a command pipped into into its execution - this way the command is run as soon as the shell starts. In this mode no prompt (hbnb) appears, and no further input is expected from the user.
</p>

</details>

<details><summary> Description of non-interative mode</summary>

<p>

<h2>Installation:</h2>
You can use a sandbox or your local env, you will be cloning from github.
This project was completed through Ubuntu 20.04 in python3.

</p>

</details>

<details><summary> Description of installation</summary>

<p>

<h2>Files included:</h2>
Files and commands used to complete this project.

</p>

</details>

<details><summary> Description of Files included</summary>

<p>


## Files included w/descriptions:
### [console.py]
The console contains the entry point of the interpreter, the list of commands
the interpreter supports are as follows:
* `EOF` - exits console
* `quit` - exits console
* `create` - Creates a new instance of`BaseModel`, saves it (to the JSON file) and prints the id
* `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file). 
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representation of all instances based or not on the class name. 
* `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). 
| FILES TO INHERIT FROM BASEMODEL  | DESCRIPTION   | ATTRIBUTES                                                                                                                           |
|----------------------------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [user.py](/models/user.py)       | user class    | email, password, first_name, last_name                                                                                               |
| [amenity.py](/models/amenity.py) | amenity class | name                                                                                                                                 |
| [place.py](/models/place.py)     | place class   | city_id, user_id, name, description, number_of_rooms, longitude, latitude, max_guests, number_bathrooms, price_by_night, amenity_ids |
| [review.py](/models/review.py)   | review class  | place_id, user_id, text                                                                                                              |
| [state.py](/models/state.py)     | state class   | name                                                                                                                                 |
| [city.py](/models/city.py)       | city class    | state_id, name                                                                                                                       |
