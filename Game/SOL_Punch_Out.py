import tkinter as tk
from tkinter import messagebox
import random
import json
import os
import time

# ---------------------------------
# SOL PUNCH OUT - TKINTER VERSION
# Compatible with Python 3.14
# ---------------------------------

SAVE_FILE = "sol_punch_out_save.json"

QUESTIONS = {
    "3": {
        "Reading": [
            {"q": "What is the main idea of a story?", "a": "theme", "hint": "The lesson or message."},
            {"q": "Who is the hero of a story?", "a": "protagonist", "hint": "The main character."},
            {"q": "Where does a story happen?", "a": "setting", "hint": "Place and time."}
        ],
        "Writing": [
            {"q": "What punctuation ends a question?", "a": "?", "hint": "Curved punctuation."},
            {"q": "What do you put between words?", "a": "space", "hint": "Use the long keyboard bar."},
            {"q": "What is an uppercase letter called?", "a": "capital", "hint": "Starts sentences."}
        ],
        "Math": [
            {"q": "5 + 5 = ?", "a": "10", "hint": "Double five."},
            {"q": "9 - 3 = ?", "a": "6", "hint": "Half of twelve."},
            {"q": "3 x 3 = ?", "a": "9", "hint": "Three groups of three."}
        ]
    },
    "4": {
        "Reading": [
            {"q": "What is a synonym?", "a": "similar", "hint": "Means almost the same."},
            {"q": "What is the opposite of hot?", "a": "cold", "hint": "Snow is this."},
            {"q": "Words that sound alike are called?", "a": "rhyming", "hint": "Cat and hat."}
        ],
        "Writing": [
            {"q": "What punctuation ends a sentence?", "a": ".", "hint": "A tiny dot."},
            {"q": "What is a naming word?", "a": "noun", "hint": "Person place or thing."},
            {"q": "What is an action word?", "a": "verb", "hint": "Run jump play."}
        ],
        "Math": [
            {"q": "7 x 6 = ?", "a": "42", "hint": "More than 40."},
            {"q": "20 / 4 = ?", "a": "5", "hint": "Half of ten."},
            {"q": "15 + 25 = ?", "a": "40", "hint": "A multiple of 10."}
        ]
    },
    "5": {
        "Reading": [
            {"q": "What does infer mean?", "a": "conclude", "hint": "Figure out using clues."},
            {"q": "What is point of view?", "a": "perspective", "hint": "How someone sees things."},
            {"q": "What is the main subject called?", "a": "topic", "hint": "Main idea."}
        ],
        "Writing": [
            {"q": "What punctuation shows excitement?", "a": "!", "hint": "Exclamation mark."},
            {"q": "What describes a noun?", "a": "adjective", "hint": "Blue fast tall."},
            {"q": "What begins a story?", "a": "introduction", "hint": "Comes first."}
        ],
        "Math": [
            {"q": "9 x 9 = ?", "a": "81", "hint": "More than 80."},
            {"q": "100 / 5 = ?", "a": "20", "hint": "Two tens."},
            {"q": "50 + 75 = ?", "a": "125", "hint": "More than 100."}
        ]
    }
}

class SOLPunchOut:

    def __init__(self, root):
        self.root = root
        self.root.title("SOL Punch Out")
        self.root.geometry("1100x700")
        self.root.configure(bg="black")

        self.name = ""
        self.grade = ""
        self.points = 0
        self.level = 1
        self.correct = 0
        self.question_index = 0
        self.pending = []
        self.questions = []
        self.attempts = 0
        self.enemy_speed = 2000
        self.expected_dodge = None
        self.dodge_success = False
        self.player_hits = 0
        self.enemy_hits = 0

        self.root.bind("<Control-p>", self.pause_menu)
        self.root.bind("<Up>", self.up_pressed)
        self.root.bind("<Down>", self.down_pressed)
        self.root.bind("<Return>", self.enter_pressed)

        self.start_menu()

    # -------------------------------
    # SAVE / LOAD
    # -------------------------------

    def save_game(self):
        data = {
            "name": self.name,
            "grade": self.grade,
            "points": self.points,
            "level": self.level,
            "correct": self.correct
        }

        with open(SAVE_FILE, "w") as file:
            json.dump(data, file)

    def load_game(self):
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, "r") as file:
                data = json.load(file)

            self.name = data["name"]
            self.grade = data["grade"]
            self.points = data["points"]
            self.level = data["level"]
            self.correct = data["correct"]

            self.prepare_questions()
            self.show_question()

    # -------------------------------
    # SCREEN CONTROL
    # -------------------------------

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # -------------------------------
    # START MENU
    # -------------------------------

    def start_menu(self):
        self.clear_screen()

        title = tk.Label(self.root, text="SOL PUNCH OUT", font=("Arial", 36, "bold"), bg="black", fg="gold")
        title.pack(pady=40)

        new_button = tk.Button(self.root, text="New Game", font=("Arial", 20), width=20, bg="green", fg="white", command=self.new_game)
        new_button.pack(pady=20)

        load_button = tk.Button(self.root, text="Load Game", font=("Arial", 20), width=20, bg="blue", fg="white", command=self.load_game)
        load_button.pack(pady=20)

    # -------------------------------
    # NEW GAME
    # -------------------------------

    def new_game(self):
        self.clear_screen()

        tk.Label(self.root, text="Enter Grade (3, 4, or 5)", font=("Arial", 20), bg="black", fg="white").pack(pady=20)

        self.grade_entry = tk.Entry(self.root, font=("Arial", 20))
        self.grade_entry.pack(pady=10)

        tk.Label(self.root, text="Enter Character Name", font=("Arial", 20), bg="black", fg="white").pack(pady=20)

        self.name_entry = tk.Entry(self.root, font=("Arial", 20))
        self.name_entry.pack(pady=10)

        start_btn = tk.Button(self.root, text="START", font=("Arial", 20), bg="red", fg="white", command=self.start_questions)
        start_btn.pack(pady=40)

    # -------------------------------
    # QUESTION SETUP
    # -------------------------------

    def prepare_questions(self):
        self.questions = []

        for subject in QUESTIONS[self.grade]:
            for question in QUESTIONS[self.grade][subject]:
                self.questions.append((subject, question))

        self.question_index = 0

    def start_questions(self):
        self.grade = self.grade_entry.get()
        self.name = self.name_entry.get()

        if self.grade not in ["3", "4", "5"]:
            messagebox.showerror("Error", "Grade must be 3, 4, or 5")
            return

        self.prepare_questions()
        self.show_question()

    # -------------------------------
    # QUESTIONS
    # -------------------------------

    def show_question(self):
        if self.question_index >= len(self.questions):

            if self.pending:
                self.questions = self.pending
                self.pending = []
                self.question_index = 0
            else:
                self.start_boxing()
                return

        self.clear_screen()

        subject, question = self.questions[self.question_index]
        self.current_question = question

        header = tk.Label(self.root, text=f"Level {self.level} | Points: {self.points}", font=("Arial", 18), bg="black", fg="cyan")
        header.pack(pady=10)

        meter = tk.Label(self.root, text=f"Correct Answers: {self.correct}/9", font=("Arial", 22), bg="black", fg="lime")
        meter.pack(pady=10)

        subject_label = tk.Label(self.root, text=f"{subject}", font=("Arial", 28, "bold"), bg="black", fg="orange")
        subject_label.pack(pady=20)

        question_label = tk.Label(self.root, text=question["q"], font=("Arial", 24), bg="black", fg="white", wraplength=900)
        question_label.pack(pady=40)

        self.answer_entry = tk.Entry(self.root, font=("Arial", 22), width=25)
        self.answer_entry.pack(pady=20)

        submit_btn = tk.Button(self.root, text="Submit", font=("Arial", 20), bg="green", fg="white", command=self.check_answer)
        submit_btn.pack(pady=20)

    def check_answer(self):
        answer = self.answer_entry.get().lower().strip()
        correct_answer = self.current_question["a"].lower()

        if answer == correct_answer:
            self.correct += 1
            self.show_meter()
            self.question_index += 1
            self.attempts = 0
            self.root.after(3000, self.show_question)

        else:
            self.attempts += 1

            messagebox.showinfo("Hint", self.current_question["hint"])

            if self.attempts >= 2:
                move = messagebox.askyesno("Next Question", "Move to next question and return later?")

                if move:
                    self.pending.append(self.questions[self.question_index])
                    self.question_index += 1
                    self.attempts = 0
                    self.show_question()

    # -------------------------------
    # METER
    # -------------------------------

    def show_meter(self):
        self.clear_screen()

        tk.Label(self.root, text="CORRECT!", font=("Arial", 40, "bold"), bg="black", fg="lime").pack(pady=40)

        canvas = tk.Canvas(self.root, width=800, height=100, bg="black", highlightthickness=0)
        canvas.pack(pady=40)

        canvas.create_rectangle(50, 30, 750, 70, outline="white", width=4)
        width = (self.correct / 9) * 700
        canvas.create_rectangle(50, 30, 50 + width, 70, fill="lime")

        tk.Label(self.root, text=f"{self.correct} out of 9 Correct", font=("Arial", 24), bg="black", fg="yellow").pack(pady=20)

    # -------------------------------
    # BOXING GAME
    # -------------------------------

    def start_boxing(self):
        self.clear_screen()

        self.player_hits = 0
        self.enemy_hits = 0

        self.canvas = tk.Canvas(self.root, width=1000, height=500, bg="darkred")
        self.canvas.pack(pady=30)

        self.canvas.create_rectangle(150, 180, 300, 420, fill="blue")
        self.canvas.create_rectangle(700, 180, 850, 420, fill="red")

        self.status = tk.Label(self.root, text="Get Ready To Fight!", font=("Arial", 24), bg="black", fg="white")
        self.status.pack(pady=20)

        self.hit_label = tk.Label(self.root, text="Player Hits: 0 | Enemy Hits: 0", font=("Arial", 20), bg="black", fg="yellow")
        self.hit_label.pack()

        self.root.after(2000, self.enemy_attack)

    def enemy_attack(self):
        attack = random.choice(["face", "body"])
        self.expected_dodge = attack
        self.dodge_success = False

        self.status.config(text=f"Enemy attacks your {attack.upper()}!")

        self.attack_time = time.time()

        self.root.after(max(700, self.enemy_speed - (self.level * 100)), self.evaluate_attack)

    def evaluate_attack(self):
        if not self.dodge_success:
            self.enemy_hits += 1
            self.status.config(text="YOU GOT HIT!")
        else:
            self.status.config(text="DODGED! PRESS ENTER TO COUNTER!")
            self.root.after(1000, self.missed_counter)
            return

        self.update_boxing()

    def missed_counter(self):
        self.update_boxing()

    def update_boxing(self):
        self.hit_label.config(text=f"Player Hits: {self.player_hits} | Enemy Hits: {self.enemy_hits}")

        if self.player_hits >= 3:
            self.points += 10
            self.level += 1

            if self.points >= 100:
                self.champion_scene()
                return

            messagebox.showinfo("Victory", f"You won! Total Points: {self.points}")
            self.correct = 0
            self.prepare_questions()
            self.show_question()
            return

        if self.enemy_hits >= 3:
            messagebox.showinfo("Defeat", "You lost the boxing match. Try again.")
            self.start_boxing()
            return

        self.root.after(1500, self.enemy_attack)

    def up_pressed(self, event):
        if self.expected_dodge == "face":
            self.dodge_success = True
            self.status.config(text="You dodged the face punch!")

    def down_pressed(self, event):
        if self.expected_dodge == "body":
            self.dodge_success = True
            self.status.config(text="You dodged the body punch!")

    def enter_pressed(self, event):
        if self.dodge_success:
            self.player_hits += 1
            self.dodge_success = False
            self.status.config(text="COUNTER PUNCH LANDED!")
            self.update_boxing()

    # -------------------------------
    # PAUSE MENU
    # -------------------------------

    def pause_menu(self, event=None):
        result = messagebox.askyesnocancel(
            "Paused",
            "Yes = Save and Quit\nNo = Continue Playing"
        )

        if result is True:
            self.save_game()
            self.root.destroy()

    # -------------------------------
    # CHAMPION SCENE
    # -------------------------------

    def champion_scene(self):
        self.clear_screen()

        label = tk.Label(
            self.root,
            text=f"🏆 SOL CHAMPION 🏆\nCongratulations {self.name}!",
            font=("Arial", 36, "bold"),
            bg="black",
            fg="gold"
        )

        label.pack(pady=80)

        dance = tk.Label(self.root, text="💃🕺 CHAMPION DANCE 🕺💃", font=("Arial", 30), bg="black", fg="lime")
        dance.pack(pady=50)

        self.animate_dance(dance, 0)

    def animate_dance(self, widget, count):
        colors = ["red", "blue", "green", "yellow", "purple", "orange"]
        widget.config(fg=random.choice(colors))

        if count < 20:
            self.root.after(500, lambda: self.animate_dance(widget, count + 1))
        else:
            self.root.destroy()

# ---------------------------------
# RUN GAME
# ---------------------------------

root = tk.Tk()
game = SOLPunchOut(root)
root.mainloop()
