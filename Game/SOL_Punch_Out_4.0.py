# =========================================================
# SOL PUNCH OUT 6.0 — FULL GAME (SECTION 1 OF 3)
# GLOBAL NON‑REPEATING QUESTIONS + MENU + EDUCATION
# =========================================================

import tkinter as tk
from tkinter import messagebox
import random
import json
import os

SAVE_FILE = "sol_punch_out_save.json"

# =========================================================
# GLOBAL QUESTION STORAGE
# =========================================================

QUESTIONS = {"3": [], "4": [], "5": []}

# =========================================================
# 3RD GRADE QUESTIONS
# =========================================================

reading_3 = [
    ("Who is the main character in a story?", "protagonist",
     ["protagonist", "villain", "author", "reader"]),
    ("Where does a story happen?", "setting",
     ["setting", "theme", "plot", "ending"]),
    ("What is the lesson of a story called?", "theme",
     ["theme", "chapter", "setting", "cover"]),
    ("What do you call the people in a story?", "characters",
     ["characters", "settings", "chapters", "titles"]),
    ("What is the beginning of a story called?", "introduction",
     ["introduction", "ending", "theme", "setting"])
]

writing_3 = [
    ("What punctuation ends a question?", "?",
     ["?", ".", "!", ","]),
    ("What punctuation ends a sentence?", ".",
     [".", "?", "!", ","]),
    ("What is an uppercase letter called?", "capital",
     ["capital", "space", "period", "comma"]),
    ("What do you put between words?", "space",
     ["space", "comma", "question mark", "colon"]),
    ("What punctuation shows excitement?", "!",
     ["!", ".", "?", ","])
]

# Generate 3rd grade questions
for i in range(120):
    a = random.randint(1, 20)
    b = random.randint(1, 20)

    QUESTIONS["3"].append({
        "subject": "Math",
        "q": f"{a} + {b} = ?",
        "choices": [str(a+b), str(a+b+1), str(a+b-1), str(a+b+2)],
        "a": str(a+b)
    })

    q = random.choice(reading_3)
    QUESTIONS["3"].append({
        "subject": "Reading",
        "q": q[0] + f" #{i}",
        "choices": q[2],
        "a": q[1]
    })

    q = random.choice(writing_3)
    QUESTIONS["3"].append({
        "subject": "Writing",
        "q": q[0] + f" #{i}",
        "choices": q[2],
        "a": q[1]
    })

# =========================================================
# 4TH GRADE QUESTIONS
# =========================================================

reading_4 = [
    ("Words that sound alike are called?", "rhyming",
     ["rhyming", "verbs", "themes", "plots"]),
    ("What is the opposite of hot?", "cold",
     ["cold", "warm", "fire", "steam"]),
    ("What is a word with the same meaning called?", "synonym",
     ["synonym", "verb", "noun", "theme"]),
    ("What is the problem in a story called?", "conflict",
     ["conflict", "setting", "theme", "chapter"]),
    ("What is the ending of a story called?", "conclusion",
     ["conclusion", "introduction", "theme", "setting"])
]

writing_4 = [
    ("What is an action word?", "verb",
     ["verb", "noun", "adjective", "theme"]),
    ("What names a person place or thing?", "noun",
     ["noun", "verb", "comma", "sentence"]),
    ("What describes a noun?", "adjective",
     ["adjective", "verb", "theme", "plot"]),
    ("What punctuation separates items in a list?", "comma",
     ["comma", "period", "question mark", "colon"]),
    ("What begins every sentence?", "capital",
     ["capital", "comma", "verb", "space"])
]

# Generate 4th grade questions
for i in range(120):
    a = random.randint(10, 50)
    b = random.randint(2, 12)

    QUESTIONS["4"].append({
        "subject": "Math",
        "q": f"{a} × {b} = ?",
        "choices": [str(a*b), str(a*b+2), str(a*b-2), str(a*b+5)],
        "a": str(a*b)
    })

    q = random.choice(reading_4)
    QUESTIONS["4"].append({
        "subject": "Reading",
        "q": q[0] + f" #{i}",
        "choices": q[2],
        "a": q[1]
    })

    q = random.choice(writing_4)
    QUESTIONS["4"].append({
        "subject": "Writing",
        "q": q[0] + f" #{i}",
        "choices": q[2],
        "a": q[1]
    })

# =========================================================
# 5TH GRADE QUESTIONS
# =========================================================

reading_5 = [
    ("What does infer mean?", "conclude",
     ["conclude", "repeat", "copy", "guess"]),
    ("Point of view means?", "perspective",
     ["perspective", "ending", "theme", "plot"]),
    ("What is the main idea called?", "topic",
     ["topic", "chapter", "setting", "ending"]),
    ("What helps support the main idea?", "details",
     ["details", "theme", "plot", "cover"]),
    ("What is a comparison using like or as?", "simile",
     ["simile", "metaphor", "noun", "verb"])
]

writing_5 = [
    ("What describes a noun?", "adjective",
     ["adjective", "verb", "chapter", "theme"]),
    ("What is a group of sentences about one idea?", "paragraph",
     ["paragraph", "comma", "theme", "plot"]),
    ("What is the first sentence in a paragraph called?", "topic sentence",
     ["topic sentence", "comma", "verb", "theme"]),
    ("What punctuation joins two sentences?", "semicolon",
     ["semicolon", "comma", "question mark", "space"]),
    ("What is writing meant to persuade called?", "persuasive",
     ["persuasive", "fiction", "poetry", "drama"])
]

# Generate 5th grade questions
for i in range(120):
    b = random.randint(2, 12)
    answer = random.randint(2, 12)
    a = b * answer

    QUESTIONS["5"].append({
        "subject": "Math",
        "q": f"{a} ÷ {b} = ?",
        "choices": [str(answer), str(answer+1), str(answer-1), str(answer+2)],
        "a": str(answer)
    })

    q = random.choice(reading_5)
    QUESTIONS["5"].append({
        "subject": "Reading",
        "q": q[0] + f" #{i}",
        "choices": q[2],
        "a": q[1]
    })

    q = random.choice(writing_5)
    QUESTIONS["5"].append({
        "subject": "Writing",
        "q": q[0] + f" #{i}",
        "choices": q[2],
        "a": q[1]
    })

# =========================================================
# BOSSES
# =========================================================

BOSSES = [
    {"name": "Rookie Ray", "speed": 2300, "color": "red"},
    {"name": "Crusher Kane", "speed": 1900, "color": "purple"},
    {"name": "Venom Viper", "speed": 1500, "color": "green"},
    {"name": "Titan King", "speed": 1200, "color": "darkred"}
]

# =========================================================
# MAIN GAME CLASS (SECTION 1 CONTENT)
# =========================================================

class SOLPunchOut:

    def __init__(self, root):

        self.root = root
        self.root.title("SOL Punch Out 6.0")
        self.root.geometry("1500x900")
        self.root.configure(bg="black")

        # Game progress
        self.grade = "3"
        self.education_wins = 0
        self.boxing_wins = 0

        # GLOBAL non‑repeating question list
        self.used_questions = []

        # Boxing state flags (Section 2 will use these)
        self.enemy_attacking = False
        self.counter_window_open = False
        self.counter_ready = False
        self.match_over = False

        # Blocking flags
        self.blocking_up = False
        self.blocking_down = False

        # Keybinds
        self.root.bind("<KeyPress-Up>", self.press_up)
        self.root.bind("<KeyRelease-Up>", self.release_up)
        self.root.bind("<KeyPress-Down>", self.press_down)
        self.root.bind("<KeyRelease-Down>", self.release_down)
        self.root.bind("<space>", self.counter_attack)
        self.root.bind("<Control-p>", self.save_game)

        self.start_menu()

    # =====================================================
    # SAVE GAME
    # =====================================================

    def save_game(self, event=None):

        data = {
            "grade": self.grade,
            "education_wins": self.education_wins,
            "boxing_wins": self.boxing_wins,
            "used_questions": self.used_questions,
            "current_boss": self.current_boss
        }

        with open(SAVE_FILE, "w") as file:
            json.dump(data, file)

        messagebox.showinfo("Saved", "Game Saved!")

    # =====================================================
    # LOAD GAME
    # =====================================================

    def load_game(self):

        if not os.path.exists(SAVE_FILE):
            messagebox.showinfo("No Save", "No save file found.")
            return

        with open(SAVE_FILE, "r") as file:
            data = json.load(file)

        self.grade = data["grade"]
        self.education_wins = data["education_wins"]
        self.boxing_wins = data["boxing_wins"]
        self.used_questions = data["used_questions"]
        self.current_boss = data["current_boss"]

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
        ).pack(pady=50)

        tk.Label(
            self.root,
            text="Choose Grade Level",
            font=("Arial", 30),
            fg="white",
            bg="black"
        ).pack(pady=20)

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

        # GLOBAL non‑repeat list resets ONLY on new game
        self.used_questions = []

        self.current_boss = 0

        self.education_instructions()

    # =====================================================
    # EDUCATION INSTRUCTIONS
    # =====================================================

    def education_instructions(self):

        self.clear_screen()

        instructions = f"""
EDUCATIONAL ROUND

Education Wins: {self.education_wins}/10
Boxing Wins: {self.boxing_wins}/10

• Questions NEVER repeat globally
• Press CTRL + P to save
• Complete questions to fight

Press ENTER to begin.
"""

        tk.Label(
            self.root,
            text=instructions,
            font=("Arial", 28),
            fg="white",
            bg="black",
            justify="left"
        ).pack(pady=150)

        self.root.bind("<Return>", self.start_questions)

    # =====================================================
    # START QUESTIONS
    # =====================================================

    def start_questions(self, event=None):

        self.root.unbind("<Return>")

        # Build list of ALL unused questions across ALL grades
        available = []

        for grade in QUESTIONS:
            for q in QUESTIONS[grade]:
                qid = q["subject"] + q["q"]
                if qid not in self.used_questions:
                    available.append(q)

        # If fewer than 5 remain, game is beaten
        if len(available) < 5:
            self.final_scene()
            return

        random.shuffle(available)
        self.questions = available[:5]
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
        qid = q["subject"] + q["q"]

        # GLOBAL non‑repeat tracking
        self.used_questions.append(qid)

        tk.Label(
            self.root,
            text=q["subject"],
            font=("Arial", 34, "bold"),
            fg="gold",
            bg="black"
        ).pack(pady=20)

        tk.Label(
            self.root,
            text=q["q"],
            font=("Arial", 32),
            fg="white",
            bg="black",
            wraplength=1200
        ).pack(pady=50)

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

        current = self.questions[self.question_index]

        if self.answer_var.get() == current["a"]:
            self.question_index += 1
            self.show_question()
        else:
            messagebox.showinfo("Incorrect", "Try again.")
    # =====================================================
    # BOXING INSTRUCTIONS
    # =====================================================

    def boxing_instructions(self):

        self.clear_screen()

        boss = BOSSES[self.current_boss]

        text = f"""
NEXT OPPONENT

{boss['name']}

CONTROLS

• HOLD UP = Block Head Punch
• HOLD DOWN = Block Body Punch
• PRESS SPACE = Counter Punch

BLOCK FIRST
THEN COUNTER

Press ENTER to fight.
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

        # Reset match state
        self.match_over = False
        self.enemy_attacking = False
        self.counter_window_open = False
        self.counter_ready = False

        self.player_health = 100
        self.enemy_health = 100

        boss = BOSSES[self.current_boss]
        self.enemy_speed = boss["speed"]

        # Canvas
        self.canvas = tk.Canvas(
            self.root,
            width=1500,
            height=850,
            bg="gray10"
        )
        self.canvas.pack()

        # RING
        self.canvas.create_rectangle(
            150, 180, 1350, 760,
            outline="white", width=8
        )

        # PLAYER BODY
        self.canvas.create_oval(520, 250, 620, 350, fill="peachpuff")
        self.canvas.create_rectangle(540, 350, 600, 580, fill="blue")

        # PLAYER GLOVE
        self.player_glove = self.canvas.create_oval(
            610, 390, 690, 470, fill="red"
        )

        # ENEMY BODY
        self.canvas.create_oval(820, 250, 920, 350, fill="tan")
        self.canvas.create_rectangle(840, 350, 900, 580, fill=boss["color"])

        # ENEMY GLOVE
        self.enemy_glove = self.canvas.create_oval(
            760, 390, 840, 470, fill="black"
        )

        # HEALTH BARS
        self.player_bar = self.canvas.create_rectangle(
            100, 80, 400, 110, fill="lime"
        )
        self.enemy_bar = self.canvas.create_rectangle(
            1100, 80, 1400, 110, fill="red"
        )

        # STATUS TEXT
        self.status = self.canvas.create_text(
            750, 130,
            text=f"FIGHTING {boss['name']}",
            font=("Arial", 30, "bold"),
            fill="gold"
        )

        # Start enemy attack loop
        self.root.after(2500, self.enemy_attack)

    # =====================================================
    # ENEMY ATTACK
    # =====================================================

    def enemy_attack(self):

        # Prevent overlapping attacks or attacks during counter window
        if self.match_over or self.enemy_attacking or self.counter_window_open:
            return

        self.enemy_attacking = True
        self.counter_ready = False

        self.attack_type = random.choice(["high", "body"])

        if self.attack_type == "high":
            self.canvas.itemconfig(self.status, text="HIGH PUNCH!")
            self.canvas.coords(self.enemy_glove, 720, 260, 810, 340)
        else:
            self.canvas.itemconfig(self.status, text="BODY SHOT!")
            self.canvas.coords(self.enemy_glove, 720, 470, 810, 540)

        self.root.after(self.enemy_speed, self.evaluate_attack)

    # =====================================================
    # EVALUATE ATTACK
    # =====================================================

    def evaluate_attack(self):

        if self.match_over:
            return

        blocked = (
            (self.attack_type == "high" and self.blocking_up) or
            (self.attack_type == "body" and self.blocking_down)
        )

        if blocked:
            self.canvas.itemconfig(self.status, text="BLOCKED! COUNTER NOW!")

            self.counter_ready = True
            self.counter_window_open = True

            # Enemy frozen during counter window
            self.root.after(2000, self.close_counter_window)

        else:
            self.player_health -= 20
            self.canvas.itemconfig(self.status, text="YOU GOT HIT!")
            self.update_health()

        self.enemy_attacking = False

    # =====================================================
    # CLOSE COUNTER WINDOW
    # =====================================================

    def close_counter_window(self):

        if self.match_over:
            return

        self.counter_ready = False
        self.counter_window_open = False

        self.update_health()

    # =====================================================
    # BLOCKING
    # =====================================================

    def press_up(self, event):
        self.blocking_up = True

    def release_up(self, event):
        self.blocking_up = False

    def press_down(self, event):
        self.blocking_down = True

    def release_down(self, event):
        self.blocking_down = False

    # =====================================================
    # COUNTER ATTACK
    # =====================================================

    def counter_attack(self, event):

        if not self.counter_ready or not self.counter_window_open or self.match_over:
            return

        self.counter_ready = False
        self.counter_window_open = False

        self.enemy_health -= 25

        # Counter punch animation
        self.canvas.coords(self.player_glove, 760, 360, 860, 450)
        self.canvas.itemconfig(self.status, text="COUNTER PUNCH LANDED!")

        self.root.after(400, self.reset_glove)
        self.update_health()

    # =====================================================
    # RESET GLOVE
    # =====================================================

    def reset_glove(self):
        self.canvas.coords(self.player_glove, 610, 390, 690, 470)

    # =====================================================
    # UPDATE HEALTH
    # =====================================================

    def update_health(self):

        # Update bars
        self.canvas.coords(self.player_bar, 100, 80, 100 + (self.player_health * 3), 110)
        self.canvas.coords(self.enemy_bar, 1400 - (self.enemy_health * 3), 80, 1400, 110)

        # DO NOT reset enemy glove here — keeps animation visible

        # Check KO
        if self.player_health <= 0:
            self.match_over = True
            self.player_knockout()
            return

        if self.enemy_health <= 0:
            self.match_over = True
            self.enemy_knockout()
            return

        # Only attack again if no counter window
        if not self.counter_window_open and not self.match_over:
            self.root.after(2000, self.enemy_attack)

    # =====================================================
    # PLAYER KO
    # =====================================================

    def player_knockout(self):

        self.enemy_attacking = False
        self.counter_window_open = False
        self.counter_ready = False

        self.canvas.itemconfig(self.status, text="YOU WERE KNOCKED OUT!")

        self.root.after(2500, self.restart_boxing)

    # =====================================================
    # ENEMY KO
    # =====================================================

    def enemy_knockout(self):

        self.enemy_attacking = False
        self.counter_window_open = False
        self.counter_ready = False

        self.canvas.itemconfig(self.status, text="KNOCKOUT WIN!")

        self.root.after(2500, self.victory)

    # =====================================================
    # RESTART BOXING
    # =====================================================

    def restart_boxing(self):

        messagebox.showinfo("Defeat", "You lost the fight.")
        self.start_boxing()
    # =====================================================
    # VICTORY (after winning a boxing match)
    # =====================================================

    def victory(self):

        self.boxing_wins += 1

        # Move to next boss if available
        if self.current_boss < len(BOSSES) - 1:
            self.current_boss += 1

        # If BOTH goals reached → final scene
        if self.education_wins >= 10 and self.boxing_wins >= 10:
            self.final_scene()
            return

        messagebox.showinfo(
            "Victory",
            f"Education Wins: {self.education_wins}/10\n"
            f"Boxing Wins: {self.boxing_wins}/10"
        )

        self.education_instructions()

    # =====================================================
    # FINAL SCENE — GAME BEATEN
    # =====================================================

    def final_scene(self):

        self.clear_screen()

        # Reset global question list ONLY after full victory
        self.used_questions = []

        tk.Label(
            self.root,
            text="🏆 WORLD CHAMPION 🏆",
            font=("Arial", 60, "bold"),
            fg="gold",
            bg="black"
        ).pack(pady=80)

        tk.Label(
            self.root,
            text="YOU BEAT THE ENTIRE GAME!",
            font=("Arial", 40, "bold"),
            fg="lime",
            bg="black"
        ).pack(pady=30)

        tk.Label(
            self.root,
            text="THE GREATEST SOL FIGHTER EVER",
            font=("Arial", 34, "bold"),
            fg="cyan",
            bg="black"
        ).pack(pady=30)

        tk.Button(
            self.root,
            text="PLAY AGAIN",
            font=("Arial", 28, "bold"),
            bg="green",
            fg="white",
            width=20,
            command=self.start_menu
        ).pack(pady=60)

    # =====================================================
    # RESTART BOXING (after losing)
    # =====================================================

    def restart_boxing(self):

        messagebox.showinfo("Defeat", "You lost the fight.")
        self.start_boxing()

# =========================================================
# RUN GAME (MAIN LOOP)
# =========================================================

root = tk.Tk()
game = SOLPunchOut(root)
root.mainloop()
