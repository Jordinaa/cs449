# Sprint-3
# Author: Jordan Taranto

import tkinter as tk
from tkinter import messagebox
import random 


class GUI:
    def __init__(self):
        # had to rewrite a lot because of logic was setup in sprint 2 so gui is slightly different 
        self.root = tk.Tk()
        self.root.geometry("750x500")
        self.root.title("SOS")

        self.blue_color = "blue"
        self.red_color = "red"

        self.current_turn = "blue"
        self.record_game = tk.BooleanVar(value=True)

        self.top_frame = tk.Frame(self.root)
        self.top_frame.pack(side="top", fill="x", padx=10, pady=5)

        self.board_size = tk.IntVar(value=3)
        self.board_size_frame = tk.Frame(self.top_frame)
        self.board_size_frame.pack(side="right", fill="x")
        tk.Label(self.board_size_frame, text="Board size").pack(side="left")
        tk.Entry(self.board_size_frame, textvariable=self.board_size, width=3).pack(side="left")

        self.game_type = tk.StringVar(value="simple")
        self.game_type_frame = tk.Frame(self.top_frame)
        self.game_type_frame.pack(side="left", fill="x", expand=True)
        tk.Radiobutton(self.game_type_frame, text="Simple game", variable=self.game_type, value="simple").pack(side="left")
        tk.Radiobutton(self.game_type_frame, text="General game", variable=self.game_type, value="general").pack(side="left")

        self.blue_player_frame = tk.LabelFrame(self.root, text="Blue", padx=10, pady=10)
        self.blue_player_frame.pack(side="left", fill="none", padx=10, pady=5)
        self.blue_player_type = tk.StringVar(value="human")
        self.blue_player_letter = tk.StringVar(value="S")
        tk.Radiobutton(self.blue_player_frame, text="Human", variable=self.blue_player_type, value="human").pack(anchor="w")
        tk.Radiobutton(self.blue_player_frame, text="S", variable=self.blue_player_letter, value="S").pack(anchor="w")
        tk.Radiobutton(self.blue_player_frame, text="O", variable=self.blue_player_letter, value="O").pack(anchor="w")
        tk.Radiobutton(self.blue_player_frame, text="Computer", variable=self.blue_player_type, value="computer").pack(anchor="w")

        self.red_player_frame = tk.LabelFrame(self.root, text="Red", padx=10, pady=10)
        self.red_player_frame.pack(side="right", fill="none", padx=10, pady=5)
        self.red_player_type = tk.StringVar(value="human")
        self.red_player_letter = tk.StringVar(value="S")
        tk.Radiobutton(self.red_player_frame, text="Human", variable=self.red_player_type, value="human").pack(anchor="w")
        tk.Radiobutton(self.red_player_frame, text="S", variable=self.red_player_letter, value="S").pack(anchor="w")
        tk.Radiobutton(self.red_player_frame, text="O", variable=self.red_player_letter, value="O").pack(anchor="w")
        tk.Radiobutton(self.red_player_frame, text="Computer", variable=self.red_player_type, value="computer").pack(anchor="w")

        tk.Button(self.root, text="Replay", command=self.replay_game).pack(fill="x", pady=2)
        tk.Button(self.root, text="New Game", command=self.start_new_game).pack(fill="x")
        tk.Checkbutton(self.root, text="Record game", variable=self.record_game).pack(anchor="w")

        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack(expand=True, padx=10, pady=5)

        self.grid_buttons = []
        self.create_grid()

        self.blue_score = 0
        self.red_score = 0

    def handle_grid_click(self, row, col):
        if self.grid_buttons[row][col]['text'] == "":
            current_letter = self.blue_player_letter.get() if self.current_turn == "blue" else self.red_player_letter.get()
            current_color = self.blue_color if self.current_turn == "blue" else self.red_color
            self.grid_buttons[row][col].config(text=current_letter, fg=current_color)
            sos_created = self.check_for_sos(row, col)
            self.game_moves.append((row, col, current_letter))

            if sos_created:
                if self.game_type.get() == "simple":
                    messagebox.showinfo("Game Over", f"{self.current_turn.capitalize()} wins!")
                    return
                else:
                    if self.current_turn == "blue":
                        self.blue_score += 1
                    else:
                        self.red_score += 1
            else:
                self.current_turn = "red" if self.current_turn == "blue" else "blue"

            if all(self.grid_buttons[r][c]['text'] != "" for r in range(self.board_size.get()) for c in range(self.board_size.get())):
                if self.game_type.get() == "simple":
                    messagebox.showinfo("Game Over", "It's a draw!")
                else:
                    winner = "Blue" if self.blue_score > self.red_score else ("Red" if self.red_score > self.blue_score else "No one, it's a draw")
                    messagebox.showinfo("Game Over", f"{winner} wins!")

            if self.current_turn == "blue" and self.blue_player_type.get() == "computer":
                self.make_computer_move()
            elif self.current_turn == "red" and self.red_player_type.get() == "computer":
                self.make_computer_move()

    def make_computer_move(self):
        empty_cells = [(row, col) for row in range(self.board_size.get()) for col in range(self.board_size.get()) if self.grid_buttons[row][col]['text'] == ""]

        if empty_cells:
            row, col = random.choice(empty_cells)
            computer_letter = random.choice(['S', 'O'])
            current_color = self.blue_color if self.current_turn == "blue" else self.red_color
            self.grid_buttons[row][col].config(text=computer_letter, fg=current_color)
            self.game_moves.append((row, col, computer_letter))
            # check for SOS and handle the game logic
            sos_created = self.check_for_sos(row, col)

            if sos_created:
                if self.game_type.get() == "simple":
                    messagebox.showinfo("Game Over", f"{self.current_turn.capitalize()} wins!")
                    return
                else:
                    if self.current_turn == "blue":
                        self.blue_score += 1
                    else:
                        self.red_score += 1
            else:
                self.current_turn = "red" if self.current_turn == "blue" else "blue"

            # check if board is full
            if all(self.grid_buttons[r][c]['text'] != "" for r in range(self.board_size.get()) for c in range(self.board_size.get())):
                if self.game_type.get() == "simple":
                    messagebox.showinfo("Game Over", "It's a draw!")
                else:
                    winner = "Blue" if self.blue_score > self.red_score else ("Red" if self.red_score > self.blue_score else "No one, it's a draw")
                    messagebox.showinfo("Game Over", f"{winner} wins!")

            # Make the next computer move if it's the computer's turn
            if (self.current_turn == "blue" and self.blue_player_type.get() == "computer") or (self.current_turn == "red" and self.red_player_type.get() == "computer"):
                self.root.after(100, self.make_computer_move)

    def check_for_sos(self, row, col):
        sos_found = False
        current_letter = self.grid_buttons[row][col]['text']
        board_size = self.board_size.get()
        
        # define range to check for sos
        range_to_check = [-2, -1, 0]
        
        # horizantal check
        for dx in range_to_check:
            # ensure its in bounds
            if 0 <= col + dx < board_size - 2:
                string = ''.join(self.grid_buttons[row][col + dx + offset]['text'] for offset in range(3))
                if string == "SOS":
                    sos_found = True
                    # stop checking is sos is found
                    break
        
        # vertical check
        for dy in range_to_check:
            # ensure its in bounds
            if 0 <= row + dy < board_size - 2:
                string = ''.join(self.grid_buttons[row + dy + offset][col]['text'] for offset in range(3))
                if string == "SOS":
                    sos_found = True
                    # stop checking is sos is found
                    break

        return sos_found

    def start_new_game(self):
        self.game_moves = []
        self.current_turn = "blue"
        self.blue_score = 0
        self.red_score = 0

        # Clear the grid buttons
        for row in range(self.board_size.get()):
            for col in range(self.board_size.get()):
                self.grid_buttons[row][col].config(text="", bg="SystemButtonFace")

        # Make computer move if it's the computer turn
        if self.current_turn == "blue" and self.blue_player_type.get() == "computer":
            self.make_computer_move()
        elif self.current_turn == "red" and self.red_player_type.get() == "computer":
            self.make_computer_move()
    
    def create_grid(self):
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
        self.grid_buttons = []
        for row in range(self.board_size.get()):
            row_buttons = []
            for col in range(self.board_size.get()):
                button = tk.Button(self.grid_frame, text="", width=2, height=1, command=lambda r=row, c=col: self.handle_grid_click(r, c))
                button.grid(row=row, column=col, padx=2, pady=2)
                row_buttons.append(button)
            self.grid_buttons.append(row_buttons)

    def replay_game(self):
        if not self.game_moves:
            messagebox.showinfo("Replay", "No recorded game available.")
            return

        self.start_new_game()

        for move in self.game_moves:
            row, col, letter = move
            current_color = self.blue_color if letter == self.blue_player_letter.get() else self.red_color
            self.grid_buttons[row][col].config(text=letter, fg=current_color)
            self.root.update()
            self.root.after(100)
        # self.game_moves = [] 

    def run(self):
        self.root.mainloop()
