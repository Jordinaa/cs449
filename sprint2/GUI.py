
# Sprint-0
# Author: Jordan Taranto
# Reference: https://medium.com/@fareedkhandev/modern-gui-using-tkinter-12da0b983e22

import tkinter as tk

# function for new game
def start_new_game():
    pass

# function for replay game
def replay_game():
    pass

# root window and size
root = tk.Tk()
root.geometry("500x450") 
root.title("SOS")

# board size
board_size = tk.IntVar(value=8)
# record game
record_game = tk.BooleanVar()

# board 
top_frame = tk.Frame(root)
top_frame.pack(side="top", fill="x", padx=10, pady=5)

# game type at the top
game_type_frame = tk.Frame(top_frame)
game_type_frame.pack(side="left", fill="x", expand=True)
tk.Radiobutton(game_type_frame, text="Simple game", value="simple").pack(side="left")
tk.Radiobutton(game_type_frame, text="General game", value="general").pack(side="left")

# board size
board_size_frame = tk.Frame(top_frame)
board_size_frame.pack(side="right", fill="x")
tk.Label(board_size_frame, text="Board size").pack(side="left")
tk.Entry(board_size_frame, textvariable=board_size, width=3).pack(side="left")

# blue player and radio buttons
blue_player_frame = tk.LabelFrame(root, text="Blue", padx=10, pady=10)
blue_player_frame.pack(side="left", fill="y", padx=10, pady=5)
blue_player_type = tk.StringVar(value="human")
blue_player_letter = tk.StringVar(value="S")
tk.Radiobutton(blue_player_frame, text="Human", variable=blue_player_type, value="human").pack(anchor="w")
tk.Radiobutton(blue_player_frame, text="S", variable=blue_player_letter, value="S").pack(anchor="w")
tk.Radiobutton(blue_player_frame, text="O", variable=blue_player_letter, value="O").pack(anchor="w")
tk.Radiobutton(blue_player_frame, text="Computer", variable=blue_player_type, value="computer").pack(anchor="w")
tk.Checkbutton(blue_player_frame, text="Record game", variable=record_game).pack(anchor="w")

# red player and radio buttons
red_player_frame = tk.LabelFrame(root, text="Red", padx=10, pady=10)
red_player_frame.pack(side="right", fill="y", padx=10, pady=5)
red_player_type = tk.StringVar(value="human")
red_player_letter = tk.StringVar(value="S")
tk.Radiobutton(red_player_frame, text="Human", variable=red_player_type, value="human").pack(anchor="w")
tk.Radiobutton(red_player_frame, text="S", variable=red_player_letter, value="S").pack(anchor="w")
tk.Radiobutton(red_player_frame, text="O", variable=red_player_letter, value="O").pack(anchor="w")
tk.Radiobutton(red_player_frame, text="Computer", variable=red_player_type, value="computer").pack(anchor="w")

# replay and new game buttons
tk.Button(red_player_frame, text="Replay", command=replay_game).pack(fill="x", pady=2)
tk.Button(red_player_frame, text="New Game", command=start_new_game).pack(fill="x")

# main loop
root.mainloop()
