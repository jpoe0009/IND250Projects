# =========================================================
# SOL PUNCH OUT 4.0 - FULL FIXED EDITION
# =========================================================
# FIXES INCLUDED
# ---------------------------------------------------------
# ✔ Blocking now REALLY blocks punches
# ✔ Player no longer takes damage after blocking
# ✔ Counter window added after successful block
# ✔ Enemy waits before attacking again
# ✔ Difficulty starts easy and increases each win
# ✔ Better grade-level educational questions
# ✔ Questions do not repeat until exhausted
# ✔ Must WIN boxing before returning to education
# ✔ Improved boxing visuals
# ✔ Clear punch animations
# ✔ Counter punch animation
# ✔ Knockout animations
# ✔ Boss progression
# ✔ Save system CTRL+P
# ✔ Continue game support
# ✔ 10 education wins + 10 boxing wins to beat game
# =========================================================

import tkinter as tk
from tkinter import messagebox
import random
import json
import os

# =========================================================
# OPTIONAL SOUND
# =========================================================

try:
    import winsound
    SOUND_ENABLED = True
except:
    SOUND_ENABLED = False

SAVE_FILE = "sol_punch_out_save.json"

# =========================================================
# EDUCATIONAL QUESTIONS
# =========================================================

QUESTIONS = {

    "3": [

        {
            "subject": "Math",
            "q": "5 + 4 = ?",
            "choices": ["9", "8", "7", "10"],
            "a": "9"
        },

        {
            "subject": "Math",
            "q": "3 x 2 = ?",
            "choices": ["6", "5", "8", "4"],
            "a": "6"
        },

        {
            "subject": "Reading",
            "q": "Who is the main character in a story?",
            "choices": ["protagonist", "villain", "author", "reader"],
            "a": "protagonist"
        },

        {
            "subject": "Writing",
            "q": "What punctuation ends a question?",
            "choices": ["?", ".", "!", ","],
            "a": "?"
        },

        {
            "subject": "Reading",
            "q": "Where a story takes place is called?",
            "choices": ["setting", "theme", "plot", "ending"],
            "a": "setting"
        },

        {
            "subject": "Math",
            "q": "10 - 7 = ?",
            "choices": ["3", "2", "4", "5"],
            "a": "3"
        }
    ],

    "4": [

        {
            "subject": "Math",
            "q": "12 x 3 = ?",
            "choices": ["36", "24", "30", "42"],
            "a": "36"
        },

        {
            "subject": "Math",
            "q": "40 ÷ 5 = ?",
            "choices": ["8", "7", "9", "6"],
            "a": "8"
        },

        {
            "subject": "Reading",
            "q": "Words that sound alike are called?",
            "choices": ["rhyming", "verbs", "themes", "plots"],
            "a": "rhyming"
        },

        {
            "subject": "Writing",
            "q": "What is an action word called?",
            "choices": ["verb", "noun", "adjective", "chapter"],
            "a": "verb"
        },

        {
            "subject": "Reading",
            "q": "The opposite of cold is?",
            "choices": ["hot", "cool", "warm", "ice"],
            "a": "hot"
        },

        {
            "subject": "Math",
            "q": "25 + 35 = ?",
            "choices": ["60", "55", "65", "70"],
            "a": "60"
        }
    ],

    "5": [

        {
            "subject": "Math",
            "q": "15 x 6 = ?",
            "choices": ["90", "80", "95", "100"],
            "a": "90"
        },

        {
            "subject": "Math",
            "q": "144 ÷ 12 = ?",
            "choices": ["12", "14", "10", "16"],
            "a": "12"
        },

        {
            "subject": "Reading",
            "q": "What does infer mean?",
            "choices": ["conclude", "repeat", "copy", "predict"],
            "a": "conclude"
        },

        {
            "subject": "Writing",
            "q": "A word that describes a noun is called?",
            "choices": ["adjective", "verb", "theme", "chapter"],
            "a": "adjective"
        },

        {
            "subject": "Reading",
            "q": "Point of view means?",
            "choices": ["perspective", "ending", "setting", "theme"],
            "a": "perspective"
        },

        {
            "subject": "Math",
            "q": "125 + 75 = ?",
            "choices": ["200", "175", "225", "250"],
            "a": "200"
        }
    ]
}

# =========================================================
# BOSSES
# =========================================================

BOSSES = [

    {
        "name": "Rookie Ray",
        "color": "red",
        "speed": 2200
    },

    {
        "name": "Crusher Kane",
        "color": "purple",
        "speed": 1800
    },

    {
        "name": "Venom Viper",
        "color": "green",
        "speed": 1400
    },

    {
        "name": "Titan King",
        "color": "darkred",
        "speed": 1000
    }
]

# =========================================================
# MAIN GAME
# =========================================================

class SOLPunchOut:

    def __init__(self, root):

        self.root = root
        self.root.title("SOL Punch Out")
        self.root.geometry("1500x900")
        self.root.configure(bg="black")

        # GAME DATA
        self.grade = "3"

        self.education_wins = 0
        self.boxing_wins = 0

        self.used_questions = []

        self.current_boss = 0

        self.blocking_up = False
        self.blocking_down = False

        self.counter_ready = False

        self.match_over = False

        # CONTROLS
        self.root.bind("<KeyPress-Up>", self.press_up)
        self.root.bind("<KeyRelease-Up>", self.release_up)

        self.root.bind("<KeyPress-Down>", self.press_down)
        self.root.bind("<KeyRelease-Down>", self.release_down)

        self.root.bind("<space>", self.counter_attack)

        self.root.bind("<Control-p>", self.pause_game)

        self.start_menu()

    # =====================================================
    # SOUND
    # =====================================================

    def play_victory_sound(self):

        if SOUND_ENABLED:

            winsound.Beep(700, 120)
            winsound.Beep(900, 120)
            winsound.Beep(1200, 220)

    # =====================================================
    # SAVE
    # =====================================================

    def pause_game(self, event=None):

        data = {

            "grade": self.grade,
            "education_wins": self.education_wins,
            "boxing_wins": self.boxing_wins,
            "used_questions": self.used_questions,
            "boss": self.current_boss
        }

        with open(SAVE_FILE, "w") as file:

            json.dump(data, file)

        messagebox.showinfo(
            "Game Saved",
            "Your game has been saved."
        )

    # =====================================================
    # LOAD
    # =====================================================

    def load_game(self):

        if not os.path.exists(SAVE_FILE):

            messagebox.showinfo(
                "No Save",
                "No saved game found."
            )

            return

        with open(SAVE_FILE, "r") as file:

            data = json.load(file)

        self.grade = data["grade"]
        self.education_wins = data["education_wins"]
        self.boxing_wins = data["boxing_wins"]
        self.used_questions = data["used_questions"]
        self.current_boss = data["boss"]

        self.education_instructions()

    # =====================================================
    # CLEAR SCREEN
    # =====================================================

    def clear_screen(self):

        for widget in self.root.winfo_children():

            widget.destroy()

    # =====================================================
    # START MENU
    # =====================================================

    def start_menu(self):

        self.clear_screen()

        tk.Label(
            self.root,
            text="SOL PUNCH OUT",
            font=("Arial", 60, "bold"),
            fg="gold",
            bg="black"
        ).pack(pady=40)

        tk.Label(
            self.root,
            text="Choose Grade Level",
            font=("Arial", 28),
            fg="white",
            bg="black"
        ).pack()

        self.grade_var = tk.StringVar(value="3")

        for g in ["3", "4", "5"]:

            tk.Radiobutton(
                self.root,
                text=f"{g}th Grade",
                variable=self.grade_var,
                value=g,
                font=("Arial", 24),
                fg="white",
                bg="black",
                selectcolor="darkblue"
            ).pack()

        tk.Button(
            self.root,
            text="NEW GAME",
            font=("Arial", 24, "bold"),
            bg="green",
            fg="white",
            width=20,
            command=self.new_game
        ).pack(pady=20)

        tk.Button(
            self.root,
            text="CONTINUE GAME",
            font=("Arial", 24, "bold"),
            bg="blue",
            fg="white",
            width=20,
            command=self.load_game
        ).pack(pady=20)

    # =====================================================
    # NEW GAME
    # =====================================================

    def new_game(self):

        self.grade = self.grade_var.get()

        self.education_wins = 0
        self.boxing_wins = 0
        self.used_questions = []

        self.current_boss = 0

        self.education_instructions()

    # =====================================================
    # EDUCATION INSTRUCTIONS
    # =====================================================

    def education_instructions(self):

        self.clear_screen()

        text = f"""
EDUCATION ROUND

Education Wins: {self.education_wins}/10
Boxing Wins: {self.boxing_wins}/10

• Answer all questions correctly
• Questions do not repeat
• Press CTRL + P to save

Press ENTER to begin
"""

        tk.Label(
            self.root,
            text=text,
            font=("Arial", 30),
            fg="white",
            bg="black",
            justify="left"
        ).pack(pady=120)

        self.root.bind("<Return>", self.start_questions)

    # =====================================================
    # START QUESTIONS
    # =====================================================

    def start_questions(self, event=None):

        self.root.unbind("<Return>")

        pool = []

        for q in QUESTIONS[self.grade]:

            if q["q"] not in self.used_questions:

                pool.append(q)

        if len(pool) < 5:

            self.used_questions = []
            pool = QUESTIONS[self.grade][:]

        random.shuffle(pool)

        self.questions = pool[:5]

        self.question_index = 0

        self.show_question()

    # =====================================================
    # SHOW QUESTION
    # =====================================================

    def show_question(self):

        if self.question_index >= len(self.questions):

            self.education_wins += 1

            self.boxing_instructions()

            return

        self.clear_screen()

        q = self.questions[self.question_index]

        self.used_questions.append(q["q"])

        tk.Label(
            self.root,
            text=q["subject"],
            font=("Arial", 32, "bold"),
            fg="gold",
            bg="black"
        ).pack(pady=20)

        tk.Label(
            self.root,
            text=q["q"],
            font=("Arial", 34),
            fg="white",
            bg="black",
            wraplength=1200
        ).pack(pady=40)

        self.answer_var = tk.StringVar()

        choices = q["choices"][:]

        random.shuffle(choices)

        for choice in choices:

            tk.Radiobutton(
                self.root,
                text=choice,
                variable=self.answer_var,
                value=choice,
                font=("Arial", 24),
                fg="white",
                bg="black",
                selectcolor="darkred"
            ).pack(pady=10)

        tk.Button(
            self.root,
            text="SUBMIT",
            font=("Arial", 24, "bold"),
            bg="green",
            fg="white",
            width=15,
            command=self.check_answer
        ).pack(pady=40)

    # =====================================================
    # CHECK ANSWER
    # =====================================================

    def check_answer(self):

        if self.answer_var.get() == "":
            return

        current = self.questions[self.question_index]

        if self.answer_var.get() == current["a"]:

            self.question_index += 1

            self.show_question()

        else:

            messagebox.showinfo(
                "Incorrect",
                "Try again."
            )

    # =====================================================
    # BOXING INSTRUCTIONS
    # =====================================================

    def boxing_instructions(self):

        self.clear_screen()

        boss = BOSSES[self.current_boss]

        text = f"""
NEXT OPPONENT:
{boss['name']}

CONTROLS

• HOLD UP = Block high punches
• HOLD DOWN = Block body punches
• PRESS SPACE = Counter punch

BLOCK FIRST.
THEN COUNTER.

Press ENTER to fight
"""

        tk.Label(
            self.root,
            text=text,
            font=("Arial", 28),
            fg="white",
            bg="black",
            justify="left"
        ).pack(pady=120)

        self.root.bind("<Return>", self.start_boxing)

    # =====================================================
    # START BOXING
    # =====================================================

    def start_boxing(self, event=None):

        self.root.unbind("<Return>")

        self.clear_screen()

        self.match_over = False

        self.player_health = 100
        self.enemy_health = 100

        boss = BOSSES[self.current_boss]

        self.enemy_speed = boss["speed"]

        self.canvas = tk.Canvas(
            self.root,
            width=1500,
            height=850,
            bg="gray10"
        )

        self.canvas.pack()

        # CROWD
        for i in range(120):

            x = random.randint(0, 1500)
            y = random.randint(0, 140)

            self.canvas.create_oval(
                x, y,
                x + 10, y + 10,
                fill=random.choice(
                    ["red", "blue", "green", "yellow"]
                )
            )

        # RING
        self.canvas.create_rectangle(
            180, 200,
            1320, 760,
            outline="white",
            width=8
        )

        # PLAYER
        self.player_head = self.canvas.create_oval(
            520, 250,
            620, 350,
            fill="peachpuff"
        )

        self.player_body = self.canvas.create_rectangle(
            540, 350,
            600, 580,
            fill="blue"
        )

        self.player_glove = self.canvas.create_oval(
            610, 390,
            690, 470,
            fill="red"
        )

        # ENEMY
        self.enemy_head = self.canvas.create_oval(
            820, 250,
            920, 350,
            fill="tan"
        )

        self.enemy_body = self.canvas.create_rectangle(
            840, 350,
            900, 580,
            fill=boss["color"]
        )

        self.enemy_glove = self.canvas.create_oval(
            760, 390,
            840, 470,
            fill="black"
        )

        # HEALTH BARS
        self.player_bar = self.canvas.create_rectangle(
            100, 80,
            400, 110,
            fill="lime"
        )

        self.enemy_bar = self.canvas.create_rectangle(
            1100, 80,
            1400, 110,
            fill="red"
        )

        self.status = self.canvas.create_text(
            750,
            140,
            text=f"FIGHTING {boss['name']}",
            font=("Arial", 30, "bold"),
            fill="gold"
        )

        self.root.after(2500, self.enemy_attack)

    # =====================================================
    # ENEMY ATTACK
    # =====================================================

    def enemy_attack(self):

        if self.match_over:
            return

        self.counter_ready = False

        self.attack_type = random.choice(
            ["high", "body"]
        )

        if self.attack_type == "high":

            self.canvas.itemconfig(
                self.status,
                text="HIGH PUNCH!"
            )

            self.canvas.coords(
                self.enemy_glove,
                720, 250,
                810, 340
            )

        else:

            self.canvas.itemconfig(
                self.status,
                text="BODY SHOT!"
            )

            self.canvas.coords(
                self.enemy_glove,
                720, 450,
                810, 540
            )

        # PLAYER HAS TIME TO REACT
        self.root.after(
            self.enemy_speed,
            self.evaluate_attack
        )

    # =====================================================
    # EVALUATE ATTACK
    # =====================================================

    def evaluate_attack(self):

        if self.match_over:
            return

        blocked = False

        # HIGH BLOCK
        if self.attack_type == "high" and self.blocking_up:

            blocked = True

        # BODY BLOCK
        elif self.attack_type == "body" and self.blocking_down:

            blocked = True

        # SUCCESSFUL BLOCK
        if blocked:

            self.canvas.itemconfig(
                self.status,
                text="BLOCKED! COUNTER NOW!"
            )

            self.counter_ready = True

            # GIVE TIME TO COUNTER
            self.root.after(
                2500,
                self.enemy_wait_after_block
            )

        else:

            self.player_health -= 20

            self.canvas.itemconfig(
                self.status,
                text="YOU GOT HIT!"
            )

            self.update_health()

    # =====================================================
    # WAIT AFTER BLOCK
    # =====================================================

    def enemy_wait_after_block(self):

        if self.match_over:
            return

        self.counter_ready = False

        self.update_health()

    # =====================================================
    # BLOCKING
    # =====================================================

    def press_up(self, event):

        self.blocking_up = True

        if hasattr(self, "canvas"):

            self.canvas.itemconfig(
                self.player_body,
                fill="lightblue"
            )

    def release_up(self, event):

        self.blocking_up = False

        if hasattr(self, "canvas"):

            self.canvas.itemconfig(
                self.player_body,
                fill="blue"
            )

    def press_down(self, event):

        self.blocking_down = True

        if hasattr(self, "canvas"):

            self.canvas.itemconfig(
                self.player_body,
                fill="cyan"
            )

    def release_down(self, event):

        self.blocking_down = False

        if hasattr(self, "canvas"):

            self.canvas.itemconfig(
                self.player_body,
                fill="blue"
            )

    # =====================================================
    # COUNTER
    # =====================================================

    def counter_attack(self, event):

        if not self.counter_ready:
            return

        self.enemy_health -= 25

        self.counter_ready = False

        # PUNCH ANIMATION
        self.canvas.coords(
            self.player_glove,
            760, 360,
            850, 450
        )

        self.canvas.itemconfig(
            self.status,
            text="COUNTER PUNCH LANDED!"
        )

        self.root.after(
            400,
            self.reset_glove
        )

        self.update_health()

    # =====================================================
    # RESET GLOVE
    # =====================================================

    def reset_glove(self):

        self.canvas.coords(
            self.player_glove,
            610, 390,
            690, 470
        )

    # =====================================================
    # UPDATE HEALTH
    # =====================================================

    def update_health(self):

        if self.match_over:
            return

        self.canvas.coords(
            self.player_bar,
            100, 80,
            100 + (self.player_health * 3),
            110
        )

        self.canvas.coords(
            self.enemy_bar,
            1400 - (self.enemy_health * 3),
            80,
            1400,
            110
        )

        # RESET ENEMY GLOVE
        self.canvas.coords(
            self.enemy_glove,
            760, 390,
            840, 470
        )

        # PLAYER LOSES
        if self.player_health <= 0:

            self.match_over = True

            self.player_knockout()

            return

        # ENEMY LOSES
        if self.enemy_health <= 0:

            self.match_over = True

            self.enemy_knockout()

            return

        # WAIT BEFORE NEXT ATTACK
        self.root.after(
            2000,
            self.enemy_attack
        )

    # =====================================================
    # PLAYER KO
    # =====================================================

    def player_knockout(self):

        self.canvas.move(
            self.player_head,
            0,
            200
        )

        self.canvas.move(
            self.player_body,
            120,
            200
        )

        self.canvas.move(
            self.player_glove,
            140,
            200
        )

        self.canvas.itemconfig(
            self.status,
            text="YOU WERE KNOCKED OUT!"
        )

        self.root.after(
            2500,
            self.restart_boxing
        )

    # =====================================================
    # ENEMY KO
    # =====================================================

    def enemy_knockout(self):

        self.play_victory_sound()

        self.canvas.move(
            self.enemy_head,
            0,
            200
        )

        self.canvas.move(
            self.enemy_body,
            -120,
            200
        )

        self.canvas.move(
            self.enemy_glove,
            -140,
            200
        )

        self.canvas.itemconfig(
            self.status,
            text="KNOCKOUT WIN!"
        )

        self.root.after(
            2500,
            self.victory
        )

    # =====================================================
    # RESTART BOXING
    # =====================================================

    def restart_boxing(self):

        messagebox.showinfo(
            "Defeat",
            "You lost the fight. Try again!"
        )

        self.start_boxing()

    # =====================================================
    # VICTORY
    # =====================================================

    def victory(self):

        self.boxing_wins += 1

        # HARDER BOSS EACH WIN
        if self.current_boss < len(BOSSES) - 1:

            self.current_boss += 1

        # FINAL GAME WIN
        if self.education_wins >= 10 and self.boxing_wins >= 10:

            self.final_scene()

            return

        messagebox.showinfo(
            "Victory",
            f"Education Wins: {self.education_wins}/10\n"
            f"Boxing Wins: {self.boxing_wins}/10"
        )

        # ONLY RETURN AFTER WINNING
        self.education_instructions()

    # =====================================================
    # FINAL SCENE
    # =====================================================

    def final_scene(self):

        self.clear_screen()

        tk.Label(
            self.root,
            text="🏆 WORLD CHAMPION 🏆",
            font=("Arial", 64, "bold"),
            fg="gold",
            bg="black"
        ).pack(pady=40)

        tk.Label(
            self.root,
            text="YOU MASTERED",
            font=("Arial", 42, "bold"),
            fg="red",
            bg="black"
        ).pack()

        tk.Label(
            self.root,
            text="EDUCATION AND BOXING",
            font=("Arial", 44, "bold"),
            fg="lime",
            bg="black"
        ).pack(pady=20)

        tk.Label(
            self.root,
            text="🔥 THE GREATEST OF ALL TIME 🔥",
            font=("Arial", 44, "bold"),
            fg="cyan",
            bg="black"
        ).pack(pady=50)

# =========================================================
# RUN GAME
# =========================================================

root = tk.Tk()

game = SOLPunchOut(root)

root.mainloop()