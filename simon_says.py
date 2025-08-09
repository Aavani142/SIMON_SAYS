import tkinter as tk
import random
import time

# Colors from your palette
COLORS = {
    "cream": "#efdbbf",
    "cherry": "#ac3030",
    "deep_red": "#68181f",
    "midnight": "#121211"
}

# Game variables
pattern = []
player_pattern = []
level = 0
buttons = {}
root = tk.Tk()
root.title("Simon Says")
root.configure(bg=COLORS["cream"])
root.geometry("600x650")

# Title label
title_label = tk.Label(
    root, text=" Simon Says ",
    font=("Helvetica", 28, "bold"),
    bg=COLORS["cream"],
    fg=COLORS["midnight"]
)
title_label.pack(pady=20)

# Info label
info_label = tk.Label(
    root, text="Press Start to Play",
    font=("Helvetica", 18),
    bg=COLORS["cream"],
    fg=COLORS["midnight"]
)
info_label.pack(pady=10)

# Create game frame
game_frame = tk.Frame(root, bg=COLORS["cream"])
game_frame.pack(pady=30)

def flash_button(color):
    """Glow effect for the button."""
    original_color = color
    buttons[color].config(bg="white", relief="sunken")
    root.update()
    time.sleep(0.3)
    buttons[color].config(bg=original_color, relief="raised")
    root.update()
    time.sleep(0.2)

def play_pattern():
    """Play the sequence of colors."""
    for color in pattern:
        flash_button(color)

def check_choice(color):
    """Check the player's choice."""
    global player_pattern, pattern, level
    player_pattern.append(color)
    flash_button(color)
    if player_pattern[-1] != pattern[len(player_pattern) - 1]:
        info_label.config(text=f" Game Over! Final Level: {level}", fg=COLORS["cherry"])
        return
    if len(player_pattern) == len(pattern):
        root.after(1000, next_round)

def next_round():
    """Go to the next round."""
    global level, player_pattern
    level += 1
    info_label.config(text=f"Level {level}", fg=COLORS["midnight"])
    player_pattern = []
    pattern.append(random.choice(list(COLORS.values())[1:]))  # Avoid cream
    root.after(500, play_pattern)

def start_game():
    """Start the game."""
    global pattern, player_pattern, level
    pattern = []
    player_pattern = []
    level = 0
    info_label.config(text="Get Ready!", fg=COLORS["midnight"])
    next_round()

# Function to create styled buttons
def create_button(color):
    return tk.Button(
        game_frame,
        bg=color,
        activebackground=color,
        width=15,
        height=6,
        bd=5,
        relief="raised",
        command=lambda: check_choice(color)
    )

# Create buttons with your palette
buttons[COLORS["cherry"]] = create_button(COLORS["cherry"])
buttons[COLORS["deep_red"]] = create_button(COLORS["deep_red"])
buttons[COLORS["midnight"]] = create_button(COLORS["midnight"])
buttons[COLORS["cream"]] = create_button(COLORS["cream"])

# Arrange buttons in grid
buttons[COLORS["cherry"]].grid(row=0, column=0, padx=15, pady=15)
buttons[COLORS["deep_red"]].grid(row=0, column=1, padx=15, pady=15)
buttons[COLORS["midnight"]].grid(row=1, column=0, padx=15, pady=15)
buttons[COLORS["cream"]].grid(row=1, column=1, padx=15, pady=15)

# Start button
start_btn = tk.Button(
    root, text="▶ Start Game",
    font=("Helvetica", 18, "bold"),
    bg=COLORS["midnight"],
    fg=COLORS["cream"],
    activebackground=COLORS["cherry"],
    activeforeground=COLORS["cream"],
    relief="raised",
    bd=5,
    command=start_game
)
start_btn.pack(pady=20)

root.mainloop()
