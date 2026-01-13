## Task0

**Description**: This task is about finding the numbers of first record of texts and last record of calls

**Approach**: Find the right number through list indexing

**Complexity Analysis**:
- **Algorithm**: Direct list indexing
- **Big O Notation**: O(1)
- **Justification**: Each elements are directly accessed through indexing, , constant time complexity regardless of input size

## Task1

**Description**: This probles is about counting the phone numbers in the records.

**Approach**: Adding different numbers to the list by iteration 

**Complexity Analysis**:
- **Algorithm**: 4 loops runs through each column to find different numbers and add it to the list
- **Big O Notation**: O(n)
- **Justification**: Iteration makes the time complexity proportional to the input size.

## Task2
**Description**: This problem is about identifying the phone number with longest record, and that time.

**Approach**: Use dictionary to store phone numbers with its time spent, add times, find the longest using max function

**Complexity Analysis**:
- **Algorithm**: separate loops to gather phone numbers, and add the time to its value in dictionary
- **Big O Notation**: O(n)
- **Justification**: iteration with no nested loops

## Task3
**Description**: Part A is about finding the area codes and mobile prefixes which got called by Bangalores '(080)'. Part B is finding the percentage of Bangalore to Bangalore calls to the calls made from Bangalore.

**Approach**: Gather phone numbers that received from-bangalore calls, and extracting there prefixes or area codes by iteration.

**Complexity Analysis**:
- **Algorithm**: A loop runs through the data to gather targeted numbers, extract area codes and prefixes through iteration. 
- **Big O Notation**: O(n)
- **Justification**: iteration without nested loops

## Task4

**Description**: This problem is about making lists of possible telemarketer numbers.

**Approach**: Select possible candidates, and remove some not satisfying the condition.

**Complexity Analysis**:
- **Algorithm**: 4 separate loops accessing each element.
- **Big O Notation**: O(n)
- **Justification**: iteration without nested loops
