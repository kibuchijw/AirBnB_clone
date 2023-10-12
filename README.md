# 0x00. AirBnB clone - The console

| Task | File |
| ---- | ---- |
| 0. README, AUTHORS | [README.md](./README.md) [AUTHORS](./AUTHORS) |
| 1. Be pycodestyle compliant! | [AirBnB_clone](./AirBnB_clone) |
| 2. Unittests | [tests/](./tests/) |
| 6. Console 0.0.1 | [console.py](./console.py) |
| 7. Console 0.1 | [console.py](./console.py) |

## Tasks
### 0. README, AUTHORS
#### README.md
* Desription of the project
* Description of the command interpretor
	* How to start it
	* How to use it
	* examples
#### AUTHORS
* Contributors to the repository
### 1. Be pycodestyle compliant!
* All the code should pass pycodestyle checks
### 2. Unittests
* All files, calsses, functions must be tested with unit tests
### 6. Console 0.0.1
* Program called `console.py` that contains the entry point of the command interpreter
* Command intepreter implements:
	* `quit` and `EOF` to exit the program
	* `help` (provided by default by `cmd`), to be updated and documents throughout the tasks
	* Custom prompt: `(hbnb)`
	* Empty line + `ENTER` shouldn't execute anything
* Code shouldn't be executed when imported
### 7. Console 0.1
* Updated `console.py` to handle the commands:
	* `create`: Creates new instance of `BaseModel`, saves it (to the JSON file) and prints the `id`. Ex: `$ create BaseModel`
		* If the class name is missing, print `** class name missing **` (ex: `$ create`)
		* If the class name doesn’t exist, print `** class doesn't exist **` (ex: `$ create MyModel`)
	* `show`: Prints the string representation of an instance based on the class name and `id`. Ex: `$ show BaseModel 1234-1234-1234`.
		* If the class name is missing, print `** class name missing **` (ex: `$ show`)
		* If the class name doesn’t exist, print `** class doesn't exist **` (ex: `$ show MyModel`)
		* If the id is missing, print `** instance id missing **` (ex: `$ show BaseModel`)
		* If the instance of the class name does not exist for the `id`, print `** no instance found **` (ex: `$ show BaseModel 121212`)
