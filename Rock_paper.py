import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("500x620")
        self.root.configure(bg="#2a2d3e")
        self.root.resizable(False, False)

        self.user_score = 0
        self.computer_score = 0
        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_choice = None
        self.computer_choice = None

        self._build_ui()

    def _build_ui(self):
        # Title
        tk.Label(
            self.root, text="🕹 Rock Paper Scissors",
            font=("Segoe UI", 22, "bold"), bg="#2a2d3e", fg="#f4f4f4"
        ).pack(pady=10)

        # Instructions
        tk.Label(
            self.root,
            text="📋 Instructions:\nChoose Rock, Paper, or Scissors to play against the computer.\nRock beats Scissors, Scissors beats Paper, Paper beats Rock.",
            font=("Segoe UI", 11),
            bg="#2a2d3e",
            fg="#d6d6d6",
            justify="center",
            wraplength=460
        ).pack(pady=5)

        # Result Display
        self.result_label = tk.Label(
            self.root, text="", font=("Segoe UI", 14),
            bg="#2a2d3e", fg="#f1faee", justify="center"
        )
        self.result_label.pack(pady=15)

        # Buttons Frame
        self.choice_frame = tk.Frame(self.root, bg="#2a2d3e")
        self.choice_frame.pack(pady=20)

        self.buttons = {}
        button_styles = {
            "Rock": "#ff9f1c",
            "Paper": "#2ec4b6",
            "Scissors": "#e71d36"
        }

        for idx, choice in enumerate(self.choices):
            btn = tk.Button(
                self.choice_frame,
                text=choice,
                font=("Segoe UI", 13, "bold"),
                width=12,
                height=2,
                bg=button_styles[choice],
                fg="white",
                activebackground="#ffffff",
                activeforeground="#000000",
                relief="flat",
                bd=3,
                cursor="hand2",
                command=lambda c=choice: self._play(c)
            )
            btn.grid(row=0, column=idx, padx=12)
            self.buttons[choice] = btn

        # Scoreboard
        self.score_label = tk.Label(
            self.root, text="", font=("Segoe UI", 15, "bold"),
            bg="#2a2d3e", fg="#a6d189"
        )
        self.score_label.pack(pady=10)

        # Reset Button
        tk.Button(
            self.root, text="🔄 Reset Game", font=("Segoe UI", 12, "bold"),
            bg="#6c5ce7", fg="white", width=15,
            activebackground="#a29bfe", relief="flat", cursor="hand2",
            command=self._reset_game
        ).pack(pady=15)

        self._update_scoreboard()

    def _play(self, user_choice):
        self.user_choice = user_choice
        self.computer_choice = random.choice(self.choices)

        result = self._determine_winner(self.user_choice, self.computer_choice)

        if result == "tie":
            message = "🤝 It's a tie!"
        elif result == "user":
            message = "🎉 You win this round!"
            self.user_score += 1
        else:
            message = "💻 Computer wins this round!"
            self.computer_score += 1

        self.result_label.config(
            text=f"You chose: {self.user_choice}\nComputer chose: {self.computer_choice}\n{message}"
        )
        self._animate_choice(self.user_choice)
        self._update_scoreboard()

        self._ask_play_again()

    def _determine_winner(self, user, computer):
        win_map = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
        if user == computer:
            return "tie"
        elif win_map[user] == computer:
            return "user"
        else:
            return "computer"

    def _animate_choice(self, choice):
        button = self.buttons[choice]
        original_color = button.cget("bg")
        button.config(bg="#b8f2e6")
        self.root.after(300, lambda: button.config(bg=original_color))

    def _update_scoreboard(self):
        self.score_label.config(
            text=f"📊 Score - You: {self.user_score} | Computer: {self.computer_score}"
        )

    def _reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.result_label.config(text="")
        self._update_scoreboard()

    def _ask_play_again(self):
        answer = messagebox.askyesno("Play Again?", "Do you want to play another round?")
        if not answer:
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
