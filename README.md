[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/d_w3ds2H)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21360705)

# Jane the Ripper

Jane the Ripper is a python script that will attempt to crack the hashes in a hash list you provide, and compare it against all the possible passwords in the wordlist you provide.
The script runs in the terminal and allows you to provide paths to the hash and wordlist files, as well as the hashing algorithm that the hash file used

## Requirements

- Python 3 or higher
- Git
- Pytest

## Installation

1. Clone the Repository
```bash
git clone https://github.com/WTCSC/jane-the-ripper-ZoltanHari
```
2. Open the Cloned Repository
```bash
cd jane-the-ripper-ZoltanHari
```
## Usage

1. Start the program with the command **`python3 jane-the-ripper.py`** in the terminal

2. Type in the path to the wordlist you want to use

3. Type in the path to the hashes you want to use

4. Type in type of hash your hashes file is using

## Usage Example

![Image showing the script being run](images/jane.png)

## Testing

To run the tests for Jane the Ripper, you need to enter **`pytest`**  or **`pytest path/to/jane-the-ripper-ZoltanHari`** in the terminal, wait for the tests to finish, and see the result

## Testing Example

![Image showing the command to run the tests and the tests all passing](images/jane_tests.png)

## Decision Tree 
