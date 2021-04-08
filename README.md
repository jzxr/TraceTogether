# TraceTogether

#CSC1008 Project

## README Description
  - This README files contatins the following:
    - Installation instructions.
    - Running instructions.
    - Algorithms Details.
    - 

## Installation instructions.
  - The following modules needs to be install on python
    - pip install networkx
    - pip install matplotlib
    - pip install scipy
    - pip install selenium

## Running instructions.
### Python CLI
  - The program can be run by executing main.py
    - Two inputs are needed from User: SG Phone No without country code. Date in 13/2/2021 Format.
### Web Ui
  

## Technical Note of HashMap for Presentation 
### HashMap 
  - Implicit linked link 
  - Linked List component is abstracted out and implemented in HashMap 

### Linear Probing
  - HashMap is implemented using a list (as compared to a dictionary used in lecture slides)
  - List has O(n) lookup time, while Dict has O(1) lookup time
  - Use a List to implement a HashTable using Linear (switch to quadratic? - to reduce clustering) probing to simulate a dictionary implementation 
  - Using Date as Key: Date is converted to integer for linear probing 

### Removing Duplicate in HashMap 
  - Linear search requires O(n) on linked link upon each search
  - Frequency of search: N
  - Total: O(n^2)
  - Is there a better way?



