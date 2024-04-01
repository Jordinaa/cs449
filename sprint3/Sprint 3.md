Jordan Taranto
CS449
Sprint-2 
https://github.com/Jordinaa/cs449/tree/main/sprint3

### 1. Demonstration (9 points) 
Submit a video of no more than five minutes, clearly demonstrating the following features. 
(a) A simple game that the blue player is the winner 
(b) A simple draw game with the same board size as (a) 
(c) A general game that the red player is the winner, and the board size is different from (a) 
(d) A general draw game with the same board size as (c) 
(e) Some automated unit tests for the simple game mode 
(f) Some automated unit tests for the general game mode

In the video, you must explain what is being demonstrated.
### Summary of Source Code (1 points)

| Source code file name | Production or Test Code? | # Lines of Code |
| --------------------- | ------------------------ | --------------- |
| GUI.py                | Production               | 145             |
| test_GUI.py           | Test                     | 73              |
| main.py               | Production               | 9               |
| Total                 |                          | 227             |
### 3. Production Code vs User stories/Acceptance Criteria (3 points)


### 4. Tests vs User stories/Acceptance Criteria (3 points)

4.1 Automated tests directly corresponding to some acceptance criteria

| User Story ID | AC ID | Class Name(s) of the Test Code | Method Name(s) of the Test Code | Description                           |
| ------------- | ----- | ------------------------------ | ------------------------------- | ------------------------------------- |
| 1             | 1.1   | TestGUI                        | test_GUI_state                  | Ensures initial GUI state is correct. |
| ...           |       |                                |                                 |                                       |


4.2 Manual tests directly corresponding to some acceptance criteria

| User Story ID | AC ID | Test Case Input                | Test Oracle (Expected Output)    | Notes                                            |
|---------------|-------|--------------------------------|----------------------------------|--------------------------------------------------|
| 1             | 1.1   | Choose board size as 5x5       | Board initializes with 5x5 size  | Tested through GUI interactions.                 |
| ...           |       |                                |                                  |                                                  |


4.3 Other automated or manual tests not corresponding to the acceptance criteria

| Number | Test Input | Expected Result | Class Name of the Test Code | Method Name of the Test Code |
| ------ | ---------- | --------------- | --------------------------- | ---------------------------- |
| 1      |            |                 |                             |                              |

### 5. Describe how the class hierarchy in your design deals with the common and different requirements of the Simple Game and the General Game? (4 points)