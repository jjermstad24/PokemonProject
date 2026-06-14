import tkinter as tk

from src.battle import Battle


class BattleGUI:
    def __init__(self, battle: Battle):
        self.battle = battle
        self.root = tk.Tk()
        self.root.title("Pokemon Battle")

        tk.Label(self.root, text="Pokemon Battle", font=("Arial", 18, "bold")).pack(pady=20)
        tk.Label(self.root, text="Build the battle here!", font=("Arial", 12)).pack(pady=10)
        tk.Button(self.root, text="Quit", command=self.root.destroy).pack(pady=10)

    def run(self):
        self.root.mainloop()
