Jordan Taranto
CS449
Sprint #2
https://github.com/Jordinaa/cs449/tree/main/sprint2

Implement the following features of the SOS game: 
1.  the basic components for the game options (board size and game mode) and initial game 
2. S/O placement for human players without checking for the formation of SOS or determining the winner.

## Sample Interface
![[Pasted image 20240310205554.png]]
# 1 Demonstration (8 points)

|     | Feature                                             |     |
| :-: | --------------------------------------------------- | --- |
|  1  | Choose board size                                   |     |
|  2  | Choose game mode                                    |     |
|  3  | Initial game of the chosen board size and game mode |     |
|  4  | "S" moves                                           |     |
|  5  | "O" moves                                           |     |
|  6  | Automated unit tests                                |     |
# 2 Summary of Source Code
| Source code file name | Production code or test code? | # lines of code |
| --------------------- | ----------------------------- | --------------- |
| GUI.py                | Production Code               | 116             |
| Logic.py              | Production Code               | 5               |
| main.py               | Production Code               | 9               |
| UnitTest.py           | Test Code                     | 51              |
|                       |                               | Total: 180      |

# 3 Production Code vs User stories/acceptance Criteria

| User Story ID | User Story Name                                         |
| :-----------: | ------------------------------------------------------- |
|       1       | Choose a board size                                     |
|       2       | Choose the game mode of a chosen board                  |
|       3       | Start a new game of the chosen board size and game mode |
|       4       | Make a move in a simple game                            |
|       5       | Make a move in a general game                           |

| User Story ID and Name | AC ID | Class Name(s) | Method Name(s)                                    | Status (complete or not) | Notes (optional)      |
| :--------------------: | :---: | ------------- | ------------------------------------------------- | ------------------------ | --------------------- |
|           1            |  1.1  | `GUI`         | `self.board_size = tk.IntVar(value=5)`            | Complete                 |                       |
|           2            |  2.1  | `GUI`         | `self.game_type_frame = tk.Frame(self.top_frame)` | Complete                 | Dynamic board added   |
|                        |  2.2  | `GUI`         |                                                   | Complete                 |                       |
|           3            |  3.1  | `GUI`         | `start_new_game(self)`                            | Complete                 |                       |
|           4            |  4.1  | `GUI`         | `handle_grid_click(self, row, col)`               | Complete                 |                       |
|           5            |  5.1  | `Logic`       | N/A                                               | Not                      |                       |
|           6            |  6.1  | `GUI`         | N/A                                               | Complete                 | Moving to Logic later |
|           7            |  7.1  | `Logic`       | N/A                                               | Not                      |                       |
# 4 Tests vs User Stories/Acceptance Criteria

| User Story ID | User Story Name                                         |
| :-----------: | ------------------------------------------------------- |
|       1       | Choose a board size                                     |
|       2       | Choose the game mode of a chosen board                  |
|       3       | Start a new game of the chosen board size and game mode |
|       4       | Make a move in a simple game                            |
|       5       | Make a move in a general game                           |

#### 4.1 Automated test directly corresponding to the acceptance criteria of the above user stories

| User Story ID and Name | **Acceptance Criterion ID** | **Class Name (s) of the Test Code** | **Method Name(s) of the Test Code** | **Description of the Test Case (input & expected output)**                                                                                                                          |
| :--------------------: | --------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|           1            | 1.1                         | `TestGUI`                           | None                                | None                                                                                                                                                                                |
|           2            | 2.1                         | `TestGUI`                           | `test_inital_state`                 | None                                                                                                                                                                                |
|                        | 2.2                         | `TestGUI`                           |                                     |                                                                                                                                                                                     |
|           3            | 3.1                         | `TestGUI`                           | `test_inital_state`                 | Checks initial state of application it verifies that the current turn is set to 'blue' and default board size is 5                                                                  |
|           4            | 4.1                         | `TestGUI`                           | `test_handle_grid_click`            | - updates the cells to the currently selected letter in my case 'S'<br>- Change text color to match current player<br>- switches turns between players after each click on the grid |

#### 4.2 Manual test directly corresponding to the acceptance criteria of the above user stories 
 - **Video - for manual test** 
#### 4.3 Other automated or manual tests not corresponding to the acceptance criteria of the above user stories

| Number | Test Input | Expected Result | Class Name of the Test Code | Method Name of the Test Code |
| ------ | ---------- | --------------- | --------------------------- | ---------------------------- |
|        |            |                 |                             |                              |
|        |            |                 |                             |                              |
|        |            |                 |                             |                              |
|        |            |                 |                             |                              |
