# Author: Jordan Taranto
## Sprint 1 Report

#### Requirements
- [ ] Choosing the board size
- [ ] Choosing the game mode
  - [ ] Simple
  - [ ] General
- [ ] Starting a new game
- [ ] Making a move
- [ ] Determining is a simpe or general game is over

---
# 1. User Stories (3 points)
#### Subject to change before Sprint 3
#### Once sprint 3 is done all changes are final
| ID | User Story Name | User Story Description | Priority | Estimated Time (hours) | 
| ----------- | ----------- | ----------- | ----------- | ----------- | 
| 1 | Choose a board size | As a player, I want the board size to be fixed, so when I play with others the rules are universal and we can share strategy. | High | 2 |
| 2 | Choose the game mode | As a player, I want to be able to choose between a simple or general game mode so that I can play for a shorter or longer amount of time. | Medium | 3 |
| 3 | Start a new game of the chosen game mode | As a player, I want to start a new game with the game mode I choose so I can begin playing. | High | 2 |
| 4 | Make a move in a simple game | As a player, I want to be able to make a move in a simple SOS game. | High | 4 |
| 5 | A simple game is over | As a player, I want to know when the game is over and who won the simple game | Medium | 2 |
| 6 | Make a move in a general game | As a player I want to be able to make a move in a general game. | High | 2 |
| 7 | A general game is over | As a player, I want to know when the game is over and who won the general game. | High | 1 |
## Estimated development time: 16 hours

# 2. Sprint Backlog (3 points)
#### Subject to change before Sprint 3
#### Once sprint 3 is done all changes are final
| User Story ID and Name | AC ID | Description of Acceptance Criterion | Status (To-Do, In-Progress Completed) |
| ---- | ---- | ---- | ---- |
| 1. Choose a board size | AC 1.1 | **Given** the game is launched, **when** the player has a fixed board size **then** the system presents the user with the the board size 8x8 and the user confirms | To-Do |
| 2. Choose the game mode | AC 2.1 | **Given** the player agrees they know the board size is fixed, **when** the player selects the option to choose the game mode, **then** the system presents the options for a simple or general game mode, and the player can choose one of the game modes. | To-Do |
| | AC 2.2 | **Given** the player selects a game mode and the selected game mode is either simple or general, **when** the selection is confirmed, **then** the system updates the game settings with the chosen game mode, and the game is reset or initialized to start with the selected mode. | To-Do |
| 3. Start a new game with a chosen game mode | AC 3.1 | **Given** the player has made a move, **when** the player selects the option to start a new game, **then** the system initializes a new game with the selected game mode, and the game board populates and is ready for play, and the player is asked to make the first move | To-Do |
| 4. Make a move in a simple game | AC 4.1 | **Given** a simple SOS game is in progress and it's the player's turn, **when** the player selects a cell to place either 'S' or 'O', **then** the system validates the move, and if valid, updates the board with the player's move, and if invalid, displays an error message and asks for a valid move. | To-Do |
| 5. A simple game is over | AC 5.1 | **Given** a simple SOS game is in progress, **when** there are no more moves left to make, **then** the system calculates the scores, and determines a winner, a draw, or a loser, and notifies the player of outcome. | To-Do |
| 6. Make a move in a general game | AC 6.1 | **Given** a general SOS game is in progress and it's the player's turn, **when** the player selects a cell to place either 'S' or 'O', **then** the system validates the move, and if valid, updates the board with the player's move, and if invalid, displays an error message and prompts for a valid move. | To-Do |
| 7. A general game is over | AC 7.1 | **Given** a general SOS game is in progress, **when** there are no more moves left to make, **then** the system calculates the scores, and determines a winner, a draw, or a loser, and notifies the player of outcome. | To-Do |
