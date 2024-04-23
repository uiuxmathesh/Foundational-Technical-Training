# Foundational Technical Training 22/04/2024

- *Assignments needs markdown included (.md files)*
- *Entire training is majorly focused on Backend Systems*
- Problem Solving
    
    ### **Steps in Problem Solving**
    
    1. Define the Problem
    2. Analyse the Problem
    3. Planning (or) Designing the solution
    4. Comparison/Analysis of Solution
    5. Deciding right solution
    6. Implementing the solution
    7. Follow-up of Solution
        1. Testing
        2. Deploy
        3. Feedback (Repeat step-1)
    
    ### **Programming Skills**
    
    1. Analytical Ability
    2. Analysis
    3. Design
    4. Technical Knowledge
    5. Programming Ability
    6. Testing
    7. Quality Planning & Practice
    8. Innovation
    9. Team Working (Peer-to-Peer Reviews)
    10. Communication (SME Opinions)
    
    ### **Performance measure**
    
    1. Timeliness
    2. Quality of Work
    3. Customer Orientation
    4. Optimal Solution
    5. Team Satisfaction
    
    ### **Four-types of Problems**
    
    1. Concurrent Problems
    2. Sequential Problems
    3. Distributed Problems
    4. Event-based Problems
    
    ### **Problem-Solving Techniques**
    
    1. Heuristics/Brute-force
    2. Greedy Approach
    3. Divide and Conquer
    4. Dynamic Programming
    
    ### Solution Modelling Tools
    
    1. Flow charts
    2. Data flow diagrams
    3. Entity relationship Diagrams
    4. Unified modeling language
    
- Algorithms
    
    An algorithm is sequence of unambiguous  instructions  for solving a problem, i.e., for any legitimate input in a finite amount of time.
    
    ### Properties of Algorithm
    
    1. Input
    2. Clear Instructions
    3. Language Independent
    4. Output
    5. Finiteness
    6. Workable
    
    ### Patterns in Algorithms
    
    1. Sequence
    2. Selection
    3. Loop
    
    ### **Exercise Algorithms**
    
    - *Find the average marks scored by a student in 3 subjects (SEQUENTIAL)*
        - **BEGIN**
        - Step 1: Accept 3 marks say **Mark1**, **Mark2**, **Mark3**
        - Step 2: **Sum** = **Mark1** + **Mark2** + **Mark3**
        - Step 3: Divide **Sum** by 3 and Find **Average**
        - Step 4: Display **Average**
        - **END**
        
    - *Find the average marks scored by a student in 3 subjects and Verify if student passed or not. A student is considered pass if his/her average is  above 65 (SELECTION)*
        - **BEGIN**
        - Step 1: Accept 3 marks say **Mark1, Mark2, Mark3**
        - Step 2: Sum = **Mark1** + **Mark2** + **Mark3**
        - Step 3: Divide **Sum** by 3 and Find **Average**.
        - Step 4: Check if **Average > 65. If true go-to Step 5. Else go-to Step 6**
        - Step 5: Display `“Student Passed”`. Go-to END.
        - Step 6: Display `“Student Failed”`.
        - **END**
    - *For a given input N, where N defines the no. of . students, Find the average marks scored by a student in 3 subjects and Verify if student passed or not. A student is considered pass if his/her average is  above 65 (SELECTION)*
        - **BEGIN**
        - Step 1: Accept **N** from user
        - Step 2: Initialize **counter** to 1
        - Step 3: Check if counter is equals to N. If true go-to **END.**
        - Step 4: Accept 3 marks say **Mark1, Mark2, Mark3**
        - Step 5: **Sum** = **Mark1** + **Mark2** + **Mark3**
        - Step 6: Divide **Sum** by 3 and Find **Average**.
        - Step 7: Check if **Average > 65. If true go-to Step 5. Else go-to Step 6**
        - Step 8: Display `“Student Passed”`. Go-to Step 10.
        - Step 9: Display `“Student Failed”`.
        - Step 10: Increment **counter** by 1. Go-to step 3.
        - **END**
    
- Data Structures
    
    Data structures is a way to organize the data
    
    ### Types of Data Structures
    
    - Linear Data structure
    - Non-Linear Data structure
    
    ## Different Data structures

    ## 1. Linear Data structures
    
    ### Stack
    ```
    Stack works on the principle of Last-In-First-Out LIFO or First-In-Last-Out -->
    ```
    
    - **Attributes of Stack**
        
        `maxTop` → The max size of the given stack
        
        `Top` → the index or pointer of the element on top of the stack
        
    - Operations of Stack
        
        `isEmpty()` : To check if the stack is empty
        
        `isFull()` : To check if the stack is full
        
        `top()` / `peek()`: To check what is on the top of the stack
        
        `push()` : To put element on top of the stack
        
        `pop()` : To remove element from top of the stack
        
    
    ### Queue
    
    Queue works on the principle of *First-In-First-Out (FIFO)* of *Last-In-Last-Out (LILO)*
    
    - **Attributes of Queue**
        
        `front` → Pointer or index that denotes the front-end of the Queue (Deletion)
        
        `rear` → Pointer or index that denotes the back-end of the Queue (Insertion)
        
        `counter` →Variable to keep track of no. of elements in Queue
        
        `maxSize` → To denote the maximum size of the Queue
        
    - **Operations on Queue**
        
        `isEmpty()` : To check if the Queue is empty
        
        `isFull()` : To check if the Queue is full
        
        `Enqueue()` : To put element on rear of the Queue
        
        `Dequeue()` : To remove element from front of the Queue

    Both the stack and queue data structures can be implemented with help of two other data structures called “array” and “linked list”
    
    ## Algorithms on Data structure
    There are basically two kinds of algorithm
    - Searching
    - Sorting
                

    ## 1. Searching
    - Linear Search
    - Binary Search

    # 2. Sorting
    - Bubble sort
    - Selection sort
    - Insertion sort
    - Merge sort
    - Quick sort


    ## 2. Non-Linear Data structures
    ### Tree
    - Binary Tree
    - Binary Search Tree
    - AVL Tree

    ## Alogrithms on  tree
    ### Tree traversals
    - inorder 
    - preorder
    - postorder
    