# =========================================================
# SOL PUNCH OUT - COMPLETE FINAL EDITION
# =========================================================
# FIXES + NEW FEATURES
# ---------------------------------------------------------
# ✔ Fixed multiple victory message bug
# ✔ Choose Grade Level (3rd, 4th, 5th)
# ✔ Education game FIRST
# ✔ Boxing game SECOND
# ✔ Better boxing graphics
# ✔ Opponents closer together
# ✔ Punches easier to see
# ✔ Clear dodge/block system
# ✔ Losing boxer falls down
# ✔ Different bosses
# ✔ Save system CTRL + P
# ✔ No repeated questions
# ✔ Enter to start screens
# ✔ Spacebar counter punch
# ✔ 10 wins to beat game
# =========================================================

import tkinter as tk
from tkinter import messagebox
import random
import json
import os

SAVE_FILE = "sol_punch_out_save.json"

# =========================================================
# QUESTIONS
# =========================================================

QUESTIONS = {

    "3": [

        {
            "subject": "Math",
            "q": "5 + 5 = ?",
            "choices": ["10", "15", "7", "20"],
            "a": "10"
        },

        {
            "subject": "Reading",
            "q": "Who is the main character?",
            "choices": ["protagonist", "villain", "author", "reader"],
            "a": "protagonist"
        },

        {
            "subject": "Writing",
            "q": "What punctuation ends a sentence?",
            "choices": [".", "!", ",", "?"],
            "a": "."
        },

        {
            "subject": "Math",
            "q": "3 x 3 = ?",
            "choices": ["9", "6", "12", "15"],
            "a": "9"
        },

        {
            "subject": "Reading",
            "q": "Where does a story happen?",
            "choices": ["setting", "ending", "theme", "plot"],
            "a": "setting"
        }

    ],

    "4": [

        {
            "subject": "Math",
            "q": "7 x 6 = ?",
            "choices": ["42", "36", "48", "50"],
            "a": "42"
        },

        {
            "subject": "Writing",
            "q": "What is an action word?",
            "choices": ["verb", "noun", "adjective", "period"],
            "a": "verb"
        },

        {
            "subject": "Reading",
            "q": "Words that sound alike are called?",
            "choices": ["rhyming", "verbs", "chapters", "plots"],
            "a": "rhyming"
        },

        {
            "subject": "Math",
            "q": "20 / 4 = ?",
            "choices": ["5", "6", "4", "7"],
            "a": "5"
        },

        {
            "subject": "Writing",
            "q": "What is a naming word?",
            "choices": ["noun", "verb", "comma", "theme"],
            "a": "noun"
        }

    ],

    "5": [

        {
            "subject": "Math",
            "q": "9 x 9 = ?",
            "choices": ["81", "90", "72", "99"],
            "a": "81"
        },

        {
            "subject": "Reading",
            "q": "What does infer mean?",
            "choices": ["conclude", "repeat", "draw", "compare"],
            "a": "conclude"
        },

        {
            "subject": "Writing",
            "q": "What describes a noun?",
            "choices": ["adjective", "verb", "period", "chapter"],
            "a": "adjective"
        },

        {
            "subject": "Math",
            "q": "100 / 5 = ?",
            "choices": ["20", "25", "10", "15"],
            "a": "20"
        },

        {
            "subject": "Reading",
            "q": "What is point of view?",
            "choices": ["perspective", "ending", "conflict", "rhyming"],
            "a": "perspective"
        }

    ]

}

# =========================================================
# BOSSES
# =========================================================

BOSSES = [

    {
        "name": "Iron Mike",
        "color": "red",
        "speed": 1700
    },

    {
        "name": "Crusher Kane",
        "color": "purple",
        "speed": 1500
    },

    {
        "name": "Venom Viper",
        "color": "green",
        "speed": 1300
    },

    {
        "name": "Titan King",
        "color": "darkred",
        "speed": 1100
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

        self.grade = "3"

        self.total_wins = 0
        self.current_boss = 0

        self.player_health = 100
        self.enemy_health = 100

        self.question_index = 0
        self.used_questions = []

        self.expected_dodge = None
        self.counter_ready = False
        self.match_over = False

        self.root.bind("<Up>", self.up_pressed)
        self.root.bind("<Down>", self.down_pressed)
        self.root.bind("<space>", self.counter_attack)

        self.root.bind("<Control-p>", self.pause_menu)

        self.start_menu()

    # =====================================================
    # SAVE
    # =====================================================

    def save_game(self):

        data = {

            "grade": self.grade,
            "wins": self.total_wins,
            "boss": self.current_boss,
            "used": self.used_questions
        }

        with open(SAVE_FILE, "w") as file:

            json.dump(data, file)

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
        self.total_wins = data["wins"]
        self.current_boss = data["boss"]
        self.used_questions = data["used"]

        self.education_instructions()

    # =====================================================
    # PAUSE
    # =====================================================

    def pause_menu(self, event=None):

        self.save_game()

        messagebox.showinfo(
            "Saved",
            "Game saved successfully!"
        )

    # =====================================================
    # START MENU
    # =====================================================

    def start_menu(self):

        self.clear_screen()

        tk.Label(
            self.root,
            text="SOL PUNCH OUT",
            font=("Arial", 54, "bold"),
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

        for grade in ["3", "4", "5"]:

            tk.Radiobutton(
                self.root,
                text=f"{grade}th Grade",
                variable=self.grade_var,
                value=grade,
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
            text="CONTINUE SAVED GAME",
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

        self.total_wins = 0
        self.current_boss = 0

        self.used_questions = []

        self.education_instructions()

    # =====================================================
    # EDUCATION INSTRUCTIONS
    # =====================================================

    def education_instructions(self):

        self.clear_screen()

        text = """

EDUCATION ROUND

• Answer all multiple choice questions
• Questions do NOT repeat
• Finish questions to unlock boxing

CONTROLS
• Mouse = Choose answers
• CTRL + P = Save Game

Press ENTER to continue.
"""

        tk.Label(
            self.root,
            text=text,
            font=("Arial", 28),
            fg="white",
            bg="black",
            justify="left"
        ).pack(pady=100)

        self.root.bind("<Return>", self.start_questions)

    # =====================================================
    # START QUESTIONS
    # =====================================================

    def start_questions(self, event=None):

        self.root.unbind("<Return>")

        all_questions = QUESTIONS[self.grade]

        remaining = []

        for q in all_questions:

            if q["q"] not in self.used_questions:

                remaining.append(q)

        random.shuffle(remaining)

        self.questions = remaining

        self.question_index = 0

        self.show_question()

    # =====================================================
    # SHOW QUESTION
    # =====================================================

    def show_question(self):

        if self.question_index >= len(self.questions):

            self.boxing_instructions()
            return

        self.clear_screen()

        question = self.questions[self.question_index]

        self.used_questions.append(question["q"])

        tk.Label(
            self.root,
            text=f"{question['subject']}",
            font=("Arial", 32, "bold"),
            fg="gold",
            bg="black"
        ).pack(pady=20)

        tk.Label(
            self.root,
            text=question["q"],
            font=("Arial", 36),
            fg="white",
            bg="black",
            wraplength=1200
        ).pack(pady=50)

        self.answer_var = tk.StringVar()

        choices = question["choices"][:]

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

        self.question_index += 1

        self.show_question()

    # =====================================================
    # BOXING INSTRUCTIONS
    # =====================================================

    def boxing_instructions(self):

        self.clear_screen()

        boss = BOSSES[self.current_boss]

        text = f"""

NEXT OPPONENT:
{boss['name']}

BOXING CONTROLS

• UP = Dodge face punch
• DOWN = Dodge body punch
• SPACEBAR = Counter punch

Watch the enemy glove carefully.

Press ENTER to fight.
"""

        tk.Label(
            self.root,
            text=text,
            font=("Arial", 28),
            fg="white",
            bg="black",
            justify="left"
        ).pack(pady=100)

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
            bg="gray10",
            highlightthickness=0
        )

        self.canvas.pack()

        # CROWD
        for i in range(200):

            x = random.randint(0, 1500)
            y = random.randint(0, 140)

            self.canvas.create_oval(
                x,
                y,
                x + 15,
                y + 15,
                fill=random.choice(
                    [
                        "red",
                        "blue",
                        "yellow",
                        "green",
                        "purple",
                        "orange"
                    ]
                )
            )

        # RING
        self.canvas.create_rectangle(
            150,
            180,
            1350,
            750,
            outline="white",
            width=10
        )

        # PLAYER
        self.player_head = self.canvas.create_oval(
            450,
            250,
            550,
            350,
            fill="peachpuff"
        )

        self.player_body = self.canvas.create_rectangle(
            460,
            350,
            540,
            550,
            fill="blue"
        )

        self.player_glove = self.canvas.create_oval(
            540,
            370,
            620,
            450,
            fill="red"
        )

        # ENEMY
        self.enemy_head = self.canvas.create_oval(
            850,
            250,
            950,
            350,
            fill="tan"
        )

        self.enemy_body = self.canvas.create_rectangle(
            860,
            350,
            940,
            550,
            fill=boss["color"]
        )

        self.enemy_glove = self.canvas.create_oval(
            780,
            370,
            860,
            450,
            fill="black"
        )

        # HEALTH
        self.player_bar = self.canvas.create_rectangle(
            100,
            80,
            400,
            110,
            fill="lime"
        )

        self.enemy_bar = self.canvas.create_rectangle(
            1100,
            80,
            1400,
            110,
            fill="red"
        )

        self.status_text = self.canvas.create_text(
            750,
            140,
            text=f"FIGHTING {boss['name']}",
            font=("Arial", 28, "bold"),
            fill="gold"
        )

        self.root.after(2500, self.enemy_attack)

    # =====================================================
    # ENEMY ATTACK
    # =====================================================

    def enemy_attack(self):

        if self.match_over:
            return

        self.expected_dodge = random.choice(
            ["face", "body"]
        )

        self.counter_ready = False

        # CLEAR VISIBLE WINDUP
        self.canvas.move(
            self.enemy_glove,
            -60,
            -30
        )

        if self.expected_dodge == "face":

            self.canvas.itemconfig(
                self.status_text,
                text="HIGH PUNCH INCOMING!"
            )

        else:

            self.canvas.itemconfig(
                self.status_text,
                text="BODY SHOT INCOMING!"
            )

        self.root.after(
            1000,
            self.throw_punch
        )

    # =====================================================
    # THROW PUNCH
    # =====================================================

    def throw_punch(self):

        if self.match_over:
            return

        # BIG PUNCH MOTION
        self.canvas.move(
            self.enemy_glove,
            -220,
            0
        )

        self.root.after(
            self.enemy_speed,
            self.evaluate_attack
        )

    # =====================================================
    # EVALUATE
    # =====================================================

    def evaluate_attack(self):

        if self.match_over:
            return

        self.canvas.coords(
            self.enemy_glove,
            780,
            370,
            860,
            450
        )

        dodged = False

        if self.expected_dodge == "face" and self.last_move == "up":

            dodged = True

        if self.expected_dodge == "body" and self.last_move == "down":

            dodged = True

        if dodged:

            self.counter_ready = True

            self.canvas.itemconfig(
                self.status_text,
                text="DODGED! PRESS SPACE!"
            )

            self.root.after(
                2000,
                self.end_counter
            )

        else:

            self.player_health -= 20

            self.canvas.itemconfig(
                self.status_text,
                text="YOU GOT HIT!"
            )

            self.update_health()

        self.last_move = None

    # =====================================================
    # END COUNTER
    # =====================================================

    def end_counter(self):

        self.counter_ready = False

        self.update_health()

    # =====================================================
    # DODGE CONTROLS
    # =====================================================

    def up_pressed(self, event):

        self.last_move = "up"

        self.canvas.move(
            self.player_head,
            0,
            -40
        )

        self.root.after(
            300,
            lambda: self.canvas.coords(
                self.player_head,
                450,
                250,
                550,
                350
            )
        )

    def down_pressed(self, event):

        self.last_move = "down"

        self.canvas.move(
            self.player_body,
            0,
            40
        )

        self.root.after(
            300,
            lambda: self.canvas.coords(
                self.player_body,
                460,
                350,
                540,
                550
            )
        )

    # =====================================================
    # COUNTER ATTACK
    # =====================================================

    def counter_attack(self, event):

        if not self.counter_ready:
            return

        self.enemy_health -= 25

        self.canvas.move(
            self.player_glove,
            220,
            0
        )

        self.root.after(
            250,
            self.reset_glove
        )

        self.counter_ready = False

        self.update_health()

    # =====================================================
    # RESET GLOVE
    # =====================================================

    def reset_glove(self):

        self.canvas.coords(
            self.player_glove,
            540,
            370,
            620,
            450
        )

    # =====================================================
    # UPDATE HEALTH
    # =====================================================

    def update_health(self):

        if self.match_over:
            return

        self.canvas.coords(
            self.player_bar,
            100,
            80,
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

        # PLAYER LOSES
        if self.player_health <= 0:

            self.match_over = True

            self.player_fall()

            return

        # ENEMY LOSES
        if self.enemy_health <= 0:

            self.match_over = True

            self.enemy_fall()

            return

        self.root.after(
            1800,
            self.enemy_attack
        )

    # =====================================================
    # PLAYER FALL
    # =====================================================

    def player_fall(self):

        self.canvas.move(
            self.player_head,
            0,
            200
        )

        self.canvas.move(
            self.player_body,
            80,
            200
        )

        self.canvas.move(
            self.player_glove,
            120,
            200
        )

        self.canvas.itemconfig(
            self.status_text,
            text="YOU WERE KNOCKED OUT!"
        )

        self.root.after(
            2500,
            self.show_defeat
        )

    # =====================================================
    # ENEMY FALL
    # =====================================================

    def enemy_fall(self):

        self.canvas.move(
            self.enemy_head,
            0,
            200
        )

        self.canvas.move(
            self.enemy_body,
            -80,
            200
        )

        self.canvas.move(
            self.enemy_glove,
            -120,
            200
        )

        self.canvas.itemconfig(
            self.status_text,
            text="KNOCKOUT WIN!"
        )

        self.root.after(
            2500,
            self.show_victory
        )

    # =====================================================
    # SHOW VICTORY
    # =====================================================

    def show_victory(self):

        self.total_wins += 1

        self.current_boss += 1

        if self.current_boss >= len(BOSSES):

            self.current_boss = 0

        if self.total_wins >= 10:

            self.epic_ending()
            return

        messagebox.showinfo(
            "Victory",
            f"You won fight #{self.total_wins}!"
        )

        self.education_instructions()

    # =====================================================
    # SHOW DEFEAT
    # =====================================================

    def show_defeat(self):

        messagebox.showinfo(
            "Defeat",
            "You lost the fight."
        )

        self.education_instructions()

    # =====================================================
    # EPIC ENDING
    # =====================================================

    def epic_ending(self):

        self.clear_screen()

        tk.Label(
            self.root,
            text="🏆 WORLD CHAMPION 🏆",
            font=("Arial", 64, "bold"),
            fg="gold",
            bg="black"
        ).pack(pady=50)

        tk.Label(
            self.root,
            text="YOU DEFEATED EVERY BOSS!",
            font=("Arial", 42, "bold"),
            fg="red",
            bg="black"
        ).pack(pady=20)

        tk.Label(
            self.root,
            text="🔥 THE GREATEST OF ALL TIME 🔥",
            font=("Arial", 40, "bold"),
            fg="lime",
            bg="black"
        ).pack(pady=40)

    # =====================================================
    # CLEAR SCREEN
    # =====================================================

    def clear_screen(self):

        for widget in self.root.winfo_children():

            widget.destroy()

# =========================================================
# RUN GAME
# =========================================================

root = tk.Tk()

game = SOLPunchOut(root)

root.mainloop()