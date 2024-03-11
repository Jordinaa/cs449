# Sprint-2
# Author: Jordan Taranto

import tkinter as tk

class GUI:
    def __init__(self):
        # root window and size
        self.root = tk.Tk()
        self.root.geometry("750x500") 
        self.root.title("SOS")

        # init player turn - blue starts first
        self.current_turn = "blue"

        # record game init to false
        self.record_game = tk.BooleanVar(value=False)

        # board frame
        self.top_frame = tk.Frame(self.root)
        self.top_frame.pack(side="top", fill="x", padx=10, pady=5)
        # board size
        self.board_size = tk.IntVar(value=5)
        self.board_size_frame = tk.Frame(self.top_frame)
        self.board_size_frame.pack(side="right", fill="x")
        tk.Label(self.board_size_frame, text="Board size").pack(side="left")
        tk.Entry(self.board_size_frame, textvariable=self.board_size, width=3).pack(side="left")

        # game type at the top
        self.game_type_frame = tk.Frame(self.top_frame)
        self.game_type_frame.pack(side="left", fill="x", expand=True)
        tk.Radiobutton(self.game_type_frame, text="Simple game", value="simple").pack(side="left")
        tk.Radiobutton(self.game_type_frame, text="General game", value="general").pack(side="left")

        # blue player and radio buttons
        self.blue_player_frame = tk.LabelFrame(self.root, text="Blue", padx=10, pady=10)
        self.blue_player_frame.pack(side="left", fill="none", padx=10, pady=5)
        self.blue_player_type = tk.StringVar(value="human")
        self.blue_player_letter = tk.StringVar(value="S")
        tk.Radiobutton(self.blue_player_frame, text="Human", variable=self.blue_player_type, value="human").pack(anchor="w")
        tk.Radiobutton(self.blue_player_frame, text="S", variable=self.blue_player_letter, value="S").pack(anchor="w")
        tk.Radiobutton(self.blue_player_frame, text="O", variable=self.blue_player_letter, value="O").pack(anchor="w")
        tk.Radiobutton(self.blue_player_frame, text="Computer", variable=self.blue_player_type, value="computer").pack(anchor="w")

        # red player and radio buttons
        self.red_player_frame = tk.LabelFrame(self.root, text="Red", padx=10, pady=10)
        self.red_player_frame.pack(side="right", fill="none", padx=10, pady=5)
        self.red_player_type = tk.StringVar(value="human")
        self.red_player_letter = tk.StringVar(value="S")
        tk.Radiobutton(self.red_player_frame, text="Human", variable=self.red_player_type, value="human").pack(anchor="w")
        tk.Radiobutton(self.red_player_frame, text="S", variable=self.red_player_letter, value="S").pack(anchor="w")
        tk.Radiobutton(self.red_player_frame, text="O", variable=self.red_player_letter, value="O").pack(anchor="w")
        tk.Radiobutton(self.red_player_frame, text="Computer", variable=self.red_player_type, value="computer").pack(anchor="w")

        # replay, record, and new game buttons
        tk.Button(self.root, text="Replay", command=self.replay_game).pack(fill="x", pady=2)
        tk.Button(self.root, text="New Game", command=self.start_new_game).pack(fill="x")
        tk.Checkbutton(self.root, text="Record game", variable=self.record_game).pack(anchor="w")

        # grid frame for the root window to hold the grid buttons
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack(expand=True, padx=10, pady=5)
        # create grid buttons
        self.grid_buttons = []
        for row in range(self.board_size.get()):
            row_buttons = []
            for col in range(self.board_size.get()):
                button = tk.Button(self.grid_frame, text="", width=2, height=1, command=lambda r=row, c=col: self.handle_grid_click(r, c))
                button.grid(row=row, column=col, padx=2, pady=2)
                row_buttons.append(button)
            self.grid_buttons.append(row_buttons)

    # handling the clicks for the grid
    def handle_grid_click(self, row, col):
        # this doesn't allow overwriting of moves on the same grid button
        if self.grid_buttons[row][col]['text'] == "":
            if self.current_turn == "blue":
                # set button color to blue
                self.grid_buttons[row][col].config(text=self.blue_player_letter.get(), fg="blue")
                # change turn to red because its reds turn after blue goes
                self.current_turn = "red"
            else:
                # set button color to red
                self.grid_buttons[row][col].config(text=self.red_player_letter.get(), fg="red")
                # change the players turn back to blue
                self.current_turn = "blue"

    # function for new game
    def start_new_game(self):
        # clear grid set them back to empty string
        for row in self.grid_buttons:
            for button in row:
                button.config(text="")

        # new grid button holder
        self.grid_buttons = []
        # get new board size
        new_size = self.board_size.get()
        # recreate grid buttons with new size upon new game
        for row in range(new_size):
            row_buttons = []
            for col in range(new_size):
                button = tk.Button(self.grid_frame, text="", width=2, height=1, command=lambda r=row, c=col: self.handle_grid_click(r, c))
                button.grid(row=row, column=col, padx=2, pady=2)
                row_buttons.append(button)
            self.grid_buttons.append(row_buttons)
        # reset the turn back to blue when new game is clicked
        self.current_turn = "blue"

    # replay game
    def replay_game(self):
        pass

    # main loop
    def run(self):
        self.root.mainloop()