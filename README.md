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

an additional hash file with extension .csv would be added to both Dir A and Dir B. Each of these files owuld contain a list of the files within the respective folders with their hashes.

## Use
To run from the commanline Run the main.py file from terminal by typing `python main.py`
To run the GUI version run `python gui.py`

### Work in progress
I'm currenlty working on the following features:
1. **Tkinter GUI** (so you can run it if you're uncomfortable with the commandline
2. **Verification** (so you can take a while that's alrready been hashed with the programe and verify the hashes in the hasfile
