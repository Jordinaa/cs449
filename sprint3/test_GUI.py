# Sprint-3
# Author: Jordan Taranto

import unittest
import tkinter as tk
from GUI import GUI

class TestGUI(unittest.TestCase):

    def setUp(self):
        # inheritance vs. composition? hmmmm
        self.app = GUI()
        # going to make a new root window so it doesn't run in mainloop
        self.app.root = tk.Tk()
        # hide the window
        self.app.root.withdraw()

    # destroy the GUI after each test 
    def tearDown(self):
        self.app.root.destroy()

    # test the state of the GUI
    def test_GUI_state(self):
        self.assertEqual(self.app.current_turn, "blue")
        self.assertEqual(self.app.board_size.get(), 5)

    # test grid clicks and that the state changes like it should
    def test_handle_grid_click(self):
        # simulating blue here 
        # simulate a click on the grid 
        self.app.handle_grid_click(0, 0)
        self.assertEqual(self.app.grid_buttons[0][0]['text'], 'S')
        self.assertEqual(self.app.grid_buttons[0][0]['fg'], 'blue')
        self.assertEqual(self.app.current_turn, 'red')

        # simulating red click on grid
        self.app.handle_grid_click(0, 1)
        self.assertEqual(self.app.grid_buttons[0][1]['text'], 'S')
        self.assertEqual(self.app.grid_buttons[0][1]['fg'], 'red')
        self.assertEqual(self.app.current_turn, 'blue')

    # starting new game resets the grid
    def test_start_new_game(self):
        # make a move like above funciton
        self.app.handle_grid_click(0, 0)
        # start a new game
        self.app.start_new_game()
        # some list comprehension to check if buttons are empty
        all_buttons_empty = all(button['text'] == "" for row in self.app.grid_buttons for button in row)
        self.assertTrue(all_buttons_empty)
        self.assertEqual(self.app.current_turn, "blue")

    def test_simple_game_winner(self):
        self.app.game_type.set("simple")
        # Simulate moves to form an SOS horizontally
        self.app.handle_grid_click(0, 0)  # Blue places 'S'
        self.app.handle_grid_click(0, 1)  # Red places 'S', assume Red also places 'S' for testing purposes
        self.app.handle_grid_click(0, 2)  # Blue places 'O'
        # Blue places another 'S' to form SOS
        self.app.handle_grid_click(0, 3)  # Assuming direct manipulation works, this would ideally form an SOS

        self.assertEqual(self.app.current_turn, "blue")  # Assuming blue wins and game stops here

    def test_general_game_scoring(self):
        self.app.game_type.set("general")

        self.app.handle_grid_click(0, 0)  # Assume an SOS is formed here for Blue
        self.app.handle_grid_click(1, 0)  # Red's turn, assume no SOS
        self.app.handle_grid_click(2, 0)  # Blue's turn, assume another SOS is formed

        self.assertEqual(self.app.blue_score, 2)  # Assuming Blue formed two SOS
        self.assertEqual(self.app.red_score, 0)  # Assuming Red hasn't formed an SOS yet

unittest.main()