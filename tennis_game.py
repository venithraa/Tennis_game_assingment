import tkinter as tk
from tkinter import messagebox

class TennisGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tennis Scoring System")

        # GUI Elements
        self.instructions = tk.Label(root, text="Enter each players points")
        self.instructions.pack(pady=10, padx=10)

        self.score_frame = tk.Frame(root)
        self.score_frame.pack(pady=5, padx=30)

        self.player1_label = tk.Label(self.score_frame, text="Player 1:")
        self.player1_label.grid(row=0, column=0, padx=5)
        self.player1_score = tk.Entry(self.score_frame, width=15)
        self.player1_score.grid(row=0, column=1, padx=5)

        self.player2_label = tk.Label(self.score_frame, text="Player 2:")
        self.player2_label.grid(row=1, column=0, padx=5)
        self.player2_score = tk.Entry(self.score_frame, width=15)
        self.player2_score.grid(row=1, column=1, padx=5)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.calculate_button = tk.Button(self.button_frame, text="Calculate Score", command=self.calculate_score)
        self.calculate_button.grid(row=0, column=0, padx=5)

        self.refresh_button = tk.Button(self.button_frame, text="Refresh", command=self.refresh_inputs)
        self.refresh_button.grid(row=0, column=1, padx=5)

        self.result_label = tk.Label(root, text="Result: ",font=("Arial", 12, "italic"), bg="lightyellow", width=30, height=2, relief="solid", anchor="center")
        self.result_label.pack(pady=10,padx=5)

    def display_score(self, p1, p2):
        # Handle win condition
        if max(p1, p2) >= 4 and abs(p1 - p2) >= 2:
            winner = "Player 1" if p1 > p2 else "Player 2"
            return f"Win for {winner}"

        # Handle deuce
        if p1 >= 3 and p2 >= 3 and p1 == p2:
            return "Deuce"

        # Handle advantage
        if p1 >= 3 and p2 >= 3 and abs(p1 - p2) == 1:
            leader = "Player 1" if p1 > p2 else "Player 2"
            return f"Advantage for {leader}"

        # Handle regular scoring
        point_names = ["Love", "Fifteen", "Thirty", "Forty"]
        p1_score = point_names[p1] if p1 < 4 else "Forty"
        p2_score = point_names[p2] if p2 < 4 else "Forty"
        return f"{p1_score}-{p2_score}"

    def calculate_score(self):
        try:
            # Retrieve scores from the input fields
            p1 = int(self.player1_score.get())
            p2 = int(self.player2_score.get())
            if p1 < 0 or p2 < 0:
                self.result_label.config(text="Result: ")
                messagebox.showerror("Invalid Input", "Scores cannot be negative. Please enter valid non-negative integers.")
                return
            # Display the calculated result
            result = self.display_score(p1, p2)
            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            self.result_label.config(text="Result: ")
            messagebox.showerror("Invalid Input", "Please enter valid integers for both scores.")

    def refresh_inputs(self):
        # Clear input fields and reset result label
        self.player1_score.delete(0, tk.END)
        self.player2_score.delete(0, tk.END)
        self.result_label.config(text="Result: ")

if __name__ == "__main__":
    root = tk.Tk()
    app = TennisGameGUI(root)
    root.mainloop()
