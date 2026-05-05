import tkinter as tk
from tkinter import messagebox
import random
import json
import os
import time
import pygame

# ---------------------------------
# SOL PUNCH OUT - FIXED VERSION
# Multiple Choice Fixed
# Random Questions
# Spacebar Counter
# Better Stability
# ---------------------------------

pygame.mixer.init()

SAVE_FILE = "sol_punch_out_save.json"

# ---------------------------------
# SAFE SOUND LOADER
# ---------------------------------

def load_sound(filename):
    if os.path.exists(filename):
        return pygame.mixer.Sound(filename)
    else:
        print(f"[WARNING] Missing sound file: {filename}")
        return None

# ---------------------------------
# QUESTIONS
# ---------------------------------

QUESTIONS = {
    "3": {
        "Reading": [
            {
                "q": "What is the main idea of a story?",
                "a": "theme",
                "choices": ["theme", "author", "ending", "setting"],
                "hint": "The lesson or message."
            },
            {
                "q": "Who is the hero of a story?",
                "a": "protagonist",
                "choices": ["protagonist", "villain", "reader", "author"],
                "hint": "The main character."
            },
            {
                "q": "Where does a story happen?",
                "a": "setting",
                "choices": ["setting", "plot", "theme", "chapter"],
                "hint": "Place and time."
            }
        ],

        "Writing": [
            {
                "q": "What punctuation ends a question?",
                "a": "?",
                "hint": "Curved punctuation."
            },
            {
                "q": "What do you put between words?",
                "a": "space",
                "hint": "Use the long keyboard bar."
            },
            {
                "q": "What is an uppercase letter called?",
                "a": "capital",
                "hint": "Starts sentences."
            }
        ],

        "Math": [
            {
                "q": "5 + 5 = ?",
                "a": "10",
                "hint": "Double five."
            },
            {
                "q": "9 - 3 = ?",
                "a": "6",
                "hint": "Half of twelve."
            },
            {
                "q": "3 x 3 = ?",
                "a": "9",
                "hint": "Three groups of three."
            }
        ]
    },

    "4": {
        "Reading": [
            {
                "q": "What is a synonym?",
                "a": "similar",
                "hint": "Means almost the same."
            },
            {
                "q": "What is the opposite of hot?",
                "a": "cold",
                "hint": "Snow is this."
            },
            {
                "q": "Words that sound alike are called?",
                "a": "rhyming",
                "hint": "Cat and hat."
            }
        ],

        "Writing": [
            {
                "q": "What punctuation ends a sentence?",
                "a": ".",
                "hint": "A tiny dot."
            },
            {
                "q": "What is a naming word?",
                "a": "noun",
                "hint": "Person place or thing."
            },
            {
                "q": "What is an action word?",
                "a": "verb",
                "hint": "Run jump play."
            }
        ],

        "Math": [
            {
                "q": "7 x 6 = ?",
                "a": "42",
                "hint": "More than 40."
            },
            {
                "q": "20 / 4 = ?",
                "a": "5",
                "hint": "Half of ten."
            },
            {
                "q": "15 + 25 = ?",
                "a": "40",
                "hint": "A multiple of 10."
            }
        ]
    },

    "5": {
        "Reading": [
            {
                "q": "What does infer mean?",
                "a": "conclude",
                "hint": "Figure out using clues."
            },
            {
                "q": "What is point of view?",
                "a": "perspective",
                "hint": "How someone sees things."
            },
            {
                "q": "What is the main subject called?",
                "a": "topic",
                "hint": "Main idea."
            }
        ],

        "Writing": [
            {
                "q": "What punctuation shows excitement?",
                "a": "!",
                "hint": "Exclamation mark."
            },
            {
                "q": "What describes a noun?",
                "a": "adjective",
                "hint": "Blue fast tall."
            },
            {
                "q": "What begins a story?",
                "a": "introduction",
                "hint": "Comes first."
            }
        ],

        "Math": [
            {
                "q": "9 x 9 = ?",
                "a": "81",
                "hint": "More than 80."
            },
            {
                "q": "100 / 5 = ?",
                "a": "20",
                "hint": "Two tens."
            },
            {
                "q": "50 + 75 = ?",
                "a": "125",
                "hint": "More than 100."
            }
        ]
    }
}

# ---------------------------------
# AVATARS
# ---------------------------------

AVATARS = [
    "🥊 Boxer",
    "🤖 Robot",
    "🐉 Dragon",
    "🦸 Hero",
    "👑 Champion"
]

# ---------------------------------
# GAME CLASS
# ---------------------------------

class SOLPunchOut:

    def __init__(self, root):

        self.root = root
        self.root.title("SOL Punch Out")
        self.root.geometry("1100x700")
        self.root.configure(bg="black")

        # SOUND
        self.sounds = {
            "punch": load_sound("punch.wav"),
            "dodge": load_sound("dodge.wav"),
            "hit": load_sound("hit.wav"),
            "victory": load_sound("victory.wav")
        }

        if os.path.exists("bg_music.mp3"):
            pygame.mixer.music.load("bg_music.mp3")
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(-1)

        # VARIABLES
        self.name = ""
        self.grade = ""
        self.avatar = ""

        self.points = 0
        self.level = 1
        self.correct = 0
        self.question_index = 0
        self.questions = []
        self.pending = []
        self.attempts = 0

        self.player_hits = 0
        self.enemy_hits = 0
        self.expected_dodge = None
        self.dodge_success = False

        # KEY BINDS
        self.root.bind("<Control-p>", self.pause_menu)

        self.root.bind("<Up>", self.up_pressed)
        self.root.bind("<Down>", self.down_pressed)

        # SPACEBAR COUNTER
        self.root.bind("<space>", self.enter_pressed)

        self.start_menu()

    # ---------------------------------
    # SOUND
    # ---------------------------------

    def play_sound(self, key):
        if self.sounds[key]:
            self.sounds[key].play()

    # ---------------------------------
    # SCREEN
    # ---------------------------------

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # ---------------------------------
    # MENU
    # ---------------------------------

    def start_menu(self):

        self.clear_screen()

        tk.Label(
            self.root,
            text="SOL PUNCH OUT",
            font=("Arial", 40, "bold"),
            bg="black",
            fg="gold"
        ).pack(pady=40)

        tk.Button(
            self.root,
            text="New Game",
            font=("Arial", 20),
            width=20,
            bg="green",
            fg="white",
            command=self.new_game
        ).pack(pady=20)

    # ---------------------------------
    # NEW GAME
    # ---------------------------------

    def new_game(self):

        self.clear_screen()

        tk.Label(
            self.root,
            text="Enter Grade (3, 4, or 5)",
            font=("Arial", 20),
            bg="black",
            fg="white"
        ).pack(pady=20)

        self.grade_entry = tk.Entry(self.root, font=("Arial", 20))
        self.grade_entry.pack()

        tk.Label(
            self.root,
            text="Enter Name",
            font=("Arial", 20),
            bg="black",
            fg="white"
        ).pack(pady=20)

        self.name_entry = tk.Entry(self.root, font=("Arial", 20))
        self.name_entry.pack()

        # AVATAR
        tk.Label(
            self.root,
            text="Choose Avatar",
            font=("Arial", 20),
            bg="black",
            fg="yellow"
        ).pack(pady=20)

        self.avatar_var = tk.StringVar(value=AVATARS[0])

        for avatar in AVATARS:
            tk.Radiobutton(
                self.root,
                text=avatar,
                variable=self.avatar_var,
                value=avatar,
                font=("Arial", 16),
                bg="black",
                fg="white",
                selectcolor="darkblue"
            ).pack()

        tk.Button(
            self.root,
            text="START",
            font=("Arial", 20),
            bg="red",
            fg="white",
            command=self.start_questions
        ).pack(pady=30)

    # ---------------------------------
    # QUESTIONS
    # ---------------------------------

    def prepare_questions(self):

        self.questions = []

        for subject in QUESTIONS[self.grade]:
            for question in QUESTIONS[self.grade][subject]:
                self.questions.append((subject, question))

        # RANDOMIZE QUESTIONS
        random.shuffle(self.questions)

        self.question_index = 0

    def start_questions(self):

        self.grade = self.grade_entry.get()
        self.name = self.name_entry.get()
        self.avatar = self.avatar_var.get()

        if self.grade not in ["3", "4", "5"]:
            messagebox.showerror("Error", "Grade must be 3, 4, or 5")
            return

        self.prepare_questions()
        self.show_question()

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

        tk.Label(
            self.root,
            text=f"{self.avatar} {self.name}",
            font=("Arial", 20),
            bg="black",
            fg="gold"
        ).pack()

        tk.Label(
            self.root,
            text=f"Points: {self.points}",
            font=("Arial", 18),
            bg="black",
            fg="cyan"
        ).pack()

        tk.Label(
            self.root,
            text=subject,
            font=("Arial", 28, "bold"),
            bg="black",
            fg="orange"
        ).pack(pady=20)

        tk.Label(
            self.root,
            text=question["q"],
            font=("Arial", 24),
            bg="black",
            fg="white",
            wraplength=900
        ).pack(pady=30)

        self.selected_answer = tk.StringVar()

        # FIXED MULTIPLE CHOICE
        if "choices" in question:
            options = question["choices"][:]

        else:

            correct = question["a"]

            wrong_pool = [
                "theme",
                "setting",
                "plot",
                "noun",
                "verb",
                "adjective",
                "cold",
                "hot",
                "42",
                "40",
                "5",
                "20",
                "81",
                "125",
                "topic",
                "perspective",
                "rhyming",
                "capital"
            ]

            wrong_answers = random.sample(
                [x for x in wrong_pool if x.lower() != correct.lower()],
                3
            )

            options = [correct] + wrong_answers

        random.shuffle(options)

        for option in options:

            tk.Radiobutton(
                self.root,
                text=option,
                variable=self.selected_answer,
                value=option,
                font=("Arial", 20),
                bg="black",
                fg="white",
                selectcolor="darkblue"
            ).pack(pady=10)

        tk.Button(
            self.root,
            text="Submit",
            font=("Arial", 20),
            bg="green",
            fg="white",
            command=self.check_answer
        ).pack(pady=30)

    def check_answer(self):

        answer = self.selected_answer.get()

        # PREVENT BLANK ANSWERS
        if answer == "":
            messagebox.showwarning(
                "No Answer",
                "Please select an answer."
            )
            return

        answer = answer.lower().strip()

        correct_answer = self.current_question["a"].lower()

        if answer == correct_answer:

            self.correct += 1
            self.points += 5

            self.play_sound("victory")

            self.question_index += 1
            self.attempts = 0

            self.show_meter()

            self.root.after(2000, self.show_question)

        else:

            self.attempts += 1

            messagebox.showinfo(
                "Hint",
                self.current_question["hint"]
            )

            if self.attempts >= 2:

                move = messagebox.askyesno(
                    "Next Question",
                    "Move to next question?"
                )

                if move:
                    self.pending.append(
                        self.questions[self.question_index]
                    )

                    self.question_index += 1
                    self.attempts = 0
                    self.show_question()

    # ---------------------------------
    # METER
    # ---------------------------------

    def show_meter(self):

        self.clear_screen()

        tk.Label(
            self.root,
            text="CORRECT!",
            font=("Arial", 40, "bold"),
            bg="black",
            fg="lime"
        ).pack(pady=40)

        canvas = tk.Canvas(
            self.root,
            width=800,
            height=100,
            bg="black",
            highlightthickness=0
        )

        canvas.pack(pady=40)

        canvas.create_rectangle(
            50,
            30,
            750,
            70,
            outline="white",
            width=4
        )

        width = (self.correct / 9) * 700

        canvas.create_rectangle(
            50,
            30,
            50 + width,
            70,
            fill="lime"
        )

    # ---------------------------------
    # BOXING
    # ---------------------------------

    def start_boxing(self):

        self.clear_screen()

        self.player_hits = 0
        self.enemy_hits = 0

        self.canvas = tk.Canvas(
            self.root,
            width=1000,
            height=500,
            bg="darkred"
        )

        self.canvas.pack(pady=20)

        self.canvas.create_rectangle(
            150,
            180,
            300,
            420,
            fill="blue"
        )

        self.canvas.create_rectangle(
            700,
            180,
            850,
            420,
            fill="red"
        )

        self.status = tk.Label(
            self.root,
            text="FIGHT!",
            font=("Arial", 24),
            bg="black",
            fg="white"
        )

        self.status.pack()

        self.hit_label = tk.Label(
            self.root,
            text="Player Hits: 0 | Enemy Hits: 0",
            font=("Arial", 20),
            bg="black",
            fg="yellow"
        )

        self.hit_label.pack()

        self.root.after(2000, self.enemy_attack)

    def enemy_attack(self):

        attack = random.choice(["face", "body"])

        self.expected_dodge = attack
        self.dodge_success = False

        self.status.config(
            text=f"Enemy attacks your {attack.upper()}!"
        )

        self.root.after(
            1500,
            self.evaluate_attack
        )

    def evaluate_attack(self):

        if not self.dodge_success:

            self.enemy_hits += 1

            self.play_sound("hit")

            self.status.config(text="YOU GOT HIT!")

        else:

            self.play_sound("dodge")

            self.status.config(
                text="DODGED! PRESS SPACEBAR!"
            )

        self.update_boxing()

    def update_boxing(self):

        self.hit_label.config(
            text=f"Player Hits: {self.player_hits} | Enemy Hits: {self.enemy_hits}"
        )

        if self.player_hits >= 3:

            messagebox.showinfo(
                "Victory",
                "You won the fight!"
            )

            self.level += 1
            self.prepare_questions()
            self.show_question()

            return

        if self.enemy_hits >= 3:

            messagebox.showinfo(
                "Defeat",
                "You lost the fight!"
            )

            self.start_boxing()

            return

        self.root.after(1500, self.enemy_attack)

    def up_pressed(self, event):

        if self.expected_dodge == "face":

            self.dodge_success = True

            self.play_sound("dodge")

            self.status.config(
                text="Dodged face attack!"
            )

    def down_pressed(self, event):

        if self.expected_dodge == "body":

            self.dodge_success = True

            self.play_sound("dodge")

            self.status.config(
                text="Dodged body attack!"
            )

    # SPACEBAR
    def enter_pressed(self, event):

        if self.dodge_success:

            self.player_hits += 1

            self.play_sound("punch")

            self.dodge_success = False

            self.status.config(
                text="COUNTER PUNCH!"
            )

            self.update_boxing()

    # ---------------------------------
    # PAUSE
    # ---------------------------------

    def pause_menu(self, event=None):

        messagebox.showinfo(
            "Pause",
            "Game Paused"
        )

# ---------------------------------
# RUN GAME
# ---------------------------------

root = tk.Tk()

game = SOLPunchOut(root)

root.mainloop()