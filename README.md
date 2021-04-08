# CSC1008 Project - TraceTogether

---

## README Description

---

- This README files contatins the following:
  - Installation instructions.
  - Running instructions.
  - Algorithms Details.

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
  - Two inputs are needed from User: SG Phone No without country code. Date in 13/2/2021 Format.

### Web Ui

Open folder in visual studio. To allow automate updating for the crawlers:

Run crawlercodev10.py
To run website on localhost, use localhost:8000 by typing in the command in Terminal:

python -m SimpleHTTPServer
in browser, type in http://localhost:8000
Make sure that the .html is in the same folder as other files & folders.

---

## Algorithms Details

---

### 1. HashMap with Separate Chaining & Linear Probing

- Files:
  - DataStructuresandAlgorithms/HashMapwAVL.py
  - DataStructuresandAlgorithms/SeperateChaining.py

- Time complexity:
  - search/Insert:
    - Avg Case: O(1)
    - Worst Case: O(n)

- Example of usage:
  - Use to combine data from multiple CSV/Data.
    - contactCT.py: Line 111
    - FindContacted_SE.py: Line 256

### 2. AVL Tree

- Files:
  - DataStructuresandAlgorithms/AVL.py

- Time complexity
  - search/insert:
    - Avg/Worst Case: O(log n)

- Example of usage:
  - Use to remove duplicated data when merging CSV/Data.
  - Inorder return to retirved sorted data,
    - contactCT.py: Line 196
    - sms.py: Line 58

### 3.  Linked List

- Files:
  - DataStructuresandAlgorithms/linked_list.py

- Time complexity
  - search:
    - Avg/Worst Case: O(n)
  - Insertion/Deletion:
    - Avg/Worst Cse: O(1)

- Example of usage:
  - Used for data processing for adding attributes for plotting of HeatMap
    - dataPrep_HeatMap.py: Line 6

### 4. Queue

- Files:
  - DataStructuresandAlgorithms/queue.py

- Time complexity
  - enqueue/dequeue:
    - Avg/Worst Case: O(1)

- Example of usage:
  - used to phone number in a queue and ensure all contact received SHN Notice.
    - sms.py: Line 67

### 5. Stack

- Files:
  - DataStructuresandAlgorithms/stack.py

- Time complexity
  - push/pop:
    - Avg/Worst Case: O(1)

- Example of usage:
  - Used to store location data in stack and together with ADT.
    - clusterTable.py: Line 56

### 6. Abstract Data Type

- Files:
  - clusterTable.py

- Time complexity
  - insert/search:
    - Avg Case: O(1)
    - Worst Case: O(n)

- Example of usage:
  - Used to keep track of each location contact type count.
    - clusterTable.py: Line 59
  
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
