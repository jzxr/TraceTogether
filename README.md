# CSC1008 Project - TraceTogether

---

## README Description

---

- This README files contains the following:
  - Installation instructions
  - Running instructions
  - Algorithms Details

---

## Installation instructions

---

- The following modules needs to be install on python
  - pip install networkx
  - pip install matplotlib
  - pip install scipy
  - pip install selenium

---

## Running instructions

---

### Python CLI

- The program can be run by executing main.py
  - Two inputs are needed from User: SG Phone No without country code. Date in 13/2/2021 Format

### Web Ui

- Files
  - index.html
  - map.html

- To run website on localhost, use localhost:8000 by typing in the command in Terminal:
  - For windows:
    - py -m http.server
  - For Mac:
    - python -m SimpleHTTPServer

- Then:
  - in browser, type in <http://localhost:8000>

---

## Algorithms Details

---

### 1. HashMap with Separate Chaining & Linear Probing (Integrated with AVL Tree)

- Files:
  - DataStructuresandAlgorithms/HashMapwAVL.py
  - DataStructuresandAlgorithms/SeperateChaining.py

- Time complexity:
  - Search/Insert:
    - Avg/Worst Case: O(log n)

- Example of usage:
  - Use to combine data from multiple CSV/Data.
  - Use to remove duplicated data when merging CSV/Data
  - Inorder return to retrieve sorted data
    - contactCT.py: Line 111
    - FindContacted_SE.py: Line 256

### 2. AVL Tree

- Files:
  - DataStructuresandAlgorithms/AVL.py

- Time complexity
  - Search/Insert:
    - Avg/Worst Case: O(log n)

- Example of usage:
  - Use to remove duplicated data when merging CSV/Data.
  - Inorder return to retrieve sorted data,
    - contactCT.py: Line 196
    - sms.py: Line 58

### 3.  Linked List

- Files:
  - DataStructuresandAlgorithms/linked_list.py

- Time complexity
  - Search:
    - Avg/Worst Case: O(n)
  - Insertion/Deletion:
    - Avg/Worst Cse: O(1)

- Example of usage:
  - Used as data processing to add attributes for plotting of HeatMap
    - dataPrep_HeatMap.py: Line 6

### 4. Queue

- Files:
  - DataStructuresandAlgorithms/queue.py

- Time complexity
  - Enqueue/Qequeue:
    - Avg/Worst Case: O(1)

- Example of usage:
  - used to add phone number in a queue and ensure all contact received SHN Notice.
    - sms.py: Line 67

### 5. Stack

- Files:
  - DataStructuresandAlgorithms/stack.py

- Time complexity
  - Push/Pop:
    - Avg/Worst Case: O(1)

- Example of usage:
  - Used to store location data in stack and together with ADT.
    - clusterTable.py: Line 56

### 6. Abstract Data Type

- Files:
  - clusterTable.py

- Time complexity
  - Insert/Search:
    - Avg Case: O(1)
    - Worst Case: O(n)

- Example of usage:
  - Used to keep track of each location contact type count.
    - clusterTable.py: Line 59
  