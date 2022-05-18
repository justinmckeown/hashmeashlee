<<<<<<< HEAD
# About

This is a simple python 3+ tool that walks through a series of directories and produces a .csv file containing a list of hashes for each file it finds on both the main directory and its subidrectories. 
Therfore, for a directory with the following subfolder and file and structures:
- Dir A
  - file_A1
  - file_A2
  - file_A3
  - Dir B
    - file_B1
    - file_B2
    - file_B3

an additional file with extension .csv would be added to both Dir A and Dir B. Each of added file will contain a list of the files within the respective folders with their hashes and the time at which the has value was generated.
 

## Use
To run from the commanline navigate to the folder containing the code, then do either of the following:
 - Run the main.py file from terminal by typing `python main.py`
 - Run the GUI version by typing `python gui.py`

### Work in progress
I'm currenlty working on the following features:
1. **Verification** (so you can take a file that has alrready been hashed with the programe and verify the details in the report file)
=======
# About

This is a simple python 3+ tool that walks through a series of directories and produces a .csv file containing a list of hashes for each file it finds on both the main directory and its subidrectories. 
Therfore, for a directory with the following subfolder and file and structures:
- Dir A
  - file_A1
  - file_A2
  - file_A3
  - Dir B
    - file_B1
    - file_B2
    - file_B3

an additional file with extension .csv would be added to both Dir A and Dir B. Each of added file will contain a list of the files within the respective folders with their hashes and the time at which the has value was generated.
 

## Use
To run from the commanline navigate to the folder containing the code, then do either of the following:
 - Run the main.py file from terminal by typing `python main.py`
 - Run the GUI version by typing `python gui.py`

### Work in progress
I'm currenlty working on the following features:
1. **Verification** Take a file that's alrready been hashed with the programe and verify the hashes in the hashfile
>>>>>>> 83e7e9dc94c207a255c4ac55b784cd9cc6c12f22
