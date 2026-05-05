# =========================================================
# SOL PUNCH OUT 7.1 — FULL GAME (SECTION 1 OF 3)
# GLOBAL NON‑REPEATING QUESTIONS + NAME + MENU + EDUCATION
# =========================================================

import tkinter as tk
from tkinter import messagebox, simpledialog
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
# MAIN GAME CLASS
# =========================================================

class SOLPunchOut:

    def __init__(self, root):

        self.root = root
        self.root.title("SOL Punch Out 7.1")
        self.root.geometry("1500x900")
        self.root.configure(bg="black")

        # Player info
        self.player_name = ""
        self.grade = "3"

        # Progress
        self.education_wins = 0      # rounds of 9 questions
        self.boxing_wins = 0         # boxing victories (10 points each)
        self.points = 0              # 10 per boxing win, 100 to win

        # GLOBAL non‑repeating questions (never reset until 100 points)
        self.used_questions = []

        # Boxing state flags (used in Section 2)
        self.enemy_attacking = False
        self.counter_window_open = False
        self.counter_ready = False
        self.match_over = False

        # Blocking flags
        self.blocking_up = False
        self.blocking_down = False

        # Current boss index
        self.current_boss = 0

        # Question state
        self.questions = []
        self.question_index = 0
        self.deferred_questions = []   # questions skipped to revisit
        self.current_attempts = 0

        # Keybinds
        self.root.bind("<KeyPress-Up>", self.press_up)
        self.root.bind("<KeyRelease-Up>", self.release_up)
        self.root.bind("<KeyPress-Down>", self.press_down)
        self.root.bind("<KeyRelease-Down>", self.release_down)

        self.root.bind("<Control-p>", self.pause_menu)

        self.start_menu()

    # =====================================================
    # SAVE GAME
    # =====================================================

    def save_game(self):

        data = {
            "grade": self.grade,
            "player_name": self.player_name,
            "education_wins": self.education_wins,
            "boxing_wins": self.boxing_wins,
            "points": self.points,
            "used_questions": self.used_questions,
            "current_boss": self.current_boss
        }

        with open(SAVE_FILE, "w") as file:
            json.dump(data, file)

        messagebox.showinfo("Saved", "Game Saved!")

    # =====================================================
    # PAUSE MENU (CTRL+P)
    # =====================================================

    def pause_menu(self, event=None):

        if messagebox.askyesno(
            "Pause",
            "Do you want to SAVE and quit?\n\nYes = Save & Quit\nNo = Continue Playing"
        ):
            self.save_game()
            self.root.destroy()

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
        self.player_name = data.get("player_name", "")
        self.education_wins = data["education_wins"]
        self.boxing_wins = data["boxing_wins"]
        self.points = data.get("points", self.boxing_wins * 10)
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
    # START MENU (improved graphics)
    # =====================================================

    def start_menu(self):

        self.clear_screen()

        # Background canvas with ring graphic
        canvas = tk.Canvas(self.root, width=1500, height=400, bg="black", highlightthickness=0)
        canvas.pack()

        # Gradient-style background
        canvas.create_rectangle(0, 0, 1500, 400, fill="black", outline="")
        canvas.create_oval(-200, -200, 700, 500, fill="#202040", outline="")
        canvas.create_oval(800, -200, 1700, 500, fill="#401020", outline="")

        # Simple ring ropes
        for y in (260, 290, 320):
            canvas.create_line(200, y, 1300, y, fill="white", width=4)

        canvas.create_rectangle(220, 240, 1280, 340, outline="gold", width=6)

        # Title
        canvas.create_text(
            750, 120,
            text="SOL PUNCH OUT",
            font=("Arial", 60, "bold"),
            fill="gold"
        )
        canvas.create_text(
            750, 190,
            text="SOL Test Training + Boxing Action",
            font=("Arial", 28, "bold"),
            fill="white"
        )

        # Menu controls below
        frame = tk.Frame(self.root, bg="black")
        frame.pack(pady=20)

        tk.Label(
            frame,
            text="Choose Grade Level",
            font=("Arial", 30),
            fg="white",
            bg="black"
        ).pack(pady=10)

        self.grade_var = tk.StringVar(value="3")

        for grade in ["3", "4", "5"]:
            tk.Radiobutton(
                frame,
                text=f"{grade}th Grade",
                variable=self.grade_var,
                value=grade,
                font=("Arial", 24),
                fg="white",
                bg="black",
                selectcolor="darkblue"
            ).pack()

        tk.Button(
            frame,
            text="NEW GAME",
            font=("Arial", 24, "bold"),
            bg="green",
            fg="white",
            width=20,
            command=self.new_game
        ).pack(pady=15)

        tk.Button(
            frame,
            text="CONTINUE GAME",
            font=("Arial", 24, "bold"),
            bg="blue",
            fg="white",
            width=20,
            command=self.load_game
        ).pack(pady=10)

    # =====================================================
    # NEW GAME
    # =====================================================

    def new_game(self):

        self.grade = self.grade_var.get()
        self.education_wins = 0
        self.boxing_wins = 0
        self.points = 0

        # GLOBAL non‑repeat list resets ONLY on new game
        self.used_questions = []
        self.current_boss = 0

        self.player_name = simpledialog.askstring(
            "Player Name",
            "Enter your boxer name:"
        ) or "Champion"

        self.education_instructions()

    # =====================================================
    # EDUCATION INSTRUCTIONS
    # =====================================================

    def education_instructions(self):

        self.clear_screen()

        instructions = f"""
EDUCATIONAL ROUND

Player: {self.player_name}
Grade: {self.grade}

Education Rounds Cleared: {self.education_wins}/10
Boxing Wins: {self.boxing_wins}/10
Points: {self.points}/100

• 9 Questions per round (3 Reading, 3 Writing, 3 Math)
• Questions NEVER repeat until you reach 100 points
• Press CTRL + P to pause and save
• Answer all 9 correctly to fight

Press ENTER to begin questions.
"""

        tk.Label(
            self.root,
            text=instructions,
            font=("Arial", 26),
            fg="white",
            bg="black",
            justify="left"
        ).pack(pady=120)

        self.root.bind("<Return>", self.start_questions)

    # =====================================================
    # START QUESTIONS (3 per subject, same grade)
    # =====================================================

    def start_questions(self, event=None):

        self.root.unbind("<Return>")

        grade_questions = [q for q in QUESTIONS[self.grade]
                           if (q["subject"] + q["q"]) not in self.used_questions]

        reading = [q for q in grade_questions if q["subject"] == "Reading"]
        writing = [q for q in grade_questions if q["subject"] == "Writing"]
        math = [q for q in grade_questions if q["subject"] == "Math"]

        if len(reading) < 3 or len(writing) < 3 or len(math) < 3:
            self.final_scene()
            return

        random.shuffle(reading)
        random.shuffle(writing)
        random.shuffle(math)

        self.questions = reading[:3] + writing[:3] + math[:3]
        random.shuffle(self.questions)

        self.question_index = 0
        self.deferred_questions = []
        self.current_attempts = 0

        self.show_question()

    # =====================================================
    # SHOW QUESTION
    # =====================================================

    def show_question(self):

        if self.question_index >= len(self.questions):

            if self.deferred_questions:
                self.questions = self.deferred_questions
                self.deferred_questions = []
                self.question_index = 0
            else:
                self.education_wins += 1
                self.boxing_instructions()
                return

        self.clear_screen()

        q = self.questions[self.question_index]
        self.current_attempts = 0

        self.current_question_id = q["subject"] + q["q"]
        self.used_questions.append(self.current_question_id)

        tk.Label(
            self.root,
            text=f"{q['subject']} Question",
            font=("Arial", 34, "bold"),
            fg="gold",
            bg="black"
        ).pack(pady=20)

        tk.Label(
            self.root,
            text=q["q"],
            font=("Arial", 30),
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
            ).pack(pady=8)

        tk.Label(
            self.root,
            text=f"Correct so far: {self.total_correct_so_far()}/90",
            font=("Arial", 22),
            fg="cyan",
            bg="black"
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="SUBMIT",
            font=("Arial", 24, "bold"),
            bg="green",
            fg="white",
            width=15,
            command=self.check_answer
        ).pack(pady=30)

    # =====================================================
    # TOTAL CORRECT SO FAR (for display)
    # =====================================================

    def total_correct_so_far(self):
        return self.question_index + (self.education_wins * 9)

    # =====================================================
    # HINT GENERATOR
    # =====================================================

    def get_hint(self, question):
        answer = str(question["a"])
        if len(answer) > 1:
            return f"Hint: The answer starts with '{answer[0]}'."
        else:
            return "Hint: Look closely at the choices."

    # =====================================================
    # CHECK ANSWER (2 attempts, skip option)
    # =====================================================

    def check_answer(self):

        if not self.questions:
            return

        current = self.questions[self.question_index]
        selected = self.answer_var.get()

        if selected == current["a"]:
            self.show_progress_meter()
            self.question_index += 1
            self.show_question()
        else:
            self.current_attempts += 1
            hint = self.get_hint(current)

            if self.current_attempts < 2:
                messagebox.showinfo("Incorrect", f"Try again.\n\n{hint}")
            else:
                if messagebox.askyesno(
                    "Skip Question?",
                    f"Incorrect again.\n\n{hint}\n\nMove on and come back later?"
                ):
                    self.deferred_questions.append(current)
                    self.question_index += 1
                    self.show_question()
                else:
                    messagebox.showinfo("Keep Trying", "Give it another shot!")

    # =====================================================
    # PROGRESS METER (3 seconds)
    # =====================================================

    def show_progress_meter(self):

        top = tk.Toplevel(self.root)
        top.overrideredirect(True)
        top.configure(bg="black")

        x = self.root.winfo_x() + 550
        y = self.root.winfo_y() + 320
        top.geometry(f"400x120+{x}+{y}")

        correct_count = self.total_correct_so_far() + 1

        tk.Label(
            top,
            text=f"Correct Answers: {correct_count} / 90",
            font=("Arial", 22, "bold"),
            fg="lime",
            bg="black"
        ).pack(expand=True, fill="both", padx=10, pady=10)

        top.after(3000, top.destroy)
    # =====================================================
    # BOXING INSTRUCTIONS
    # =====================================================

    def boxing_instructions(self):

        self.clear_screen()

        boss = BOSSES[self.current_boss]

        text = f"""
NEXT OPPONENT: {boss['name']}

CONTROLS

• HOLD UP = Block Head Punch
• HOLD DOWN = Block Body Punch
• PRESS ENTER = Counter Punch (1 second window)

BLOCK FIRST
THEN COUNTER

Land 3 counter punches to win the round.

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

        self.match_over = False
        self.enemy_attacking = False
        self.counter_window_open = False
        self.counter_ready = False

        self.player_health = 3
        self.enemy_health = 3

        boss = BOSSES[self.current_boss]
        self.enemy_speed = boss["speed"]

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
        for y in (220, 250, 280):
            self.canvas.create_line(170, y, 1330, y, fill="lightgray", width=3)

        # PLAYER BODY (better graphics)
        self.player_head = self.canvas.create_oval(520, 250, 620, 350, fill="peachpuff", outline="black", width=3)
        self.player_body = self.canvas.create_rectangle(540, 350, 600, 580, fill="blue", outline="black", width=3)
        self.player_belt = self.canvas.create_rectangle(540, 430, 600, 445, fill="gold", outline="black")

        self.player_glove = self.canvas.create_oval(
            610, 390, 690, 470, fill="red", outline="black", width=2
        )

        # ENEMY BODY (better graphics)
        self.enemy_head = self.canvas.create_oval(820, 250, 920, 350, fill="tan", outline="black", width=3)
        self.enemy_body = self.canvas.create_rectangle(840, 350, 900, 580, fill=boss["color"], outline="black", width=3)
        self.enemy_belt = self.canvas.create_rectangle(840, 430, 900, 445, fill="silver", outline="black")

        self.enemy_glove = self.canvas.create_oval(
            760, 390, 840, 470, fill="black", outline="white", width=2
        )

        # HEALTH BARS
        self.player_bar = self.canvas.create_rectangle(
            100, 80, 100 + (self.player_health * 100), 110, fill="lime"
        )
        self.enemy_bar = self.canvas.create_rectangle(
            1400 - (self.enemy_health * 100), 80, 1400, 110, fill="red"
        )

        self.status = self.canvas.create_text(
            750, 130,
            text=f"FIGHTING {boss['name']}",
            font=("Arial", 30, "bold"),
            fill="gold"
        )

        self.root.bind("<Return>", self.counter_attack)

        self.root.after(2500, self.enemy_attack)

    # =====================================================
    # ENEMY ATTACK
    # =====================================================

    def enemy_attack(self):

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
    # EVALUATE ATTACK (with hit/block visuals)
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
            self.flash_block()
            self.counter_ready = True
            self.counter_window_open = True
            self.root.after(1000, self.close_counter_window)
        else:
            self.player_health -= 1
            self.canvas.itemconfig(self.status, text="YOU GOT HIT!")
            self.flash_player_hit()
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
    # COUNTER ATTACK (ENTER KEY)
    # =====================================================

    def counter_attack(self, event):

        if not self.counter_ready or not self.counter_window_open or self.match_over:
            return

        self.counter_ready = False
        self.counter_window_open = False

        self.enemy_health -= 1

        # Counter punch animation + enemy hit flash
        self.canvas.coords(self.player_glove, 760, 360, 860, 450)
        self.canvas.itemconfig(self.status, text="COUNTER PUNCH!")
        self.flash_enemy_hit()

        self.root.after(300, self.reset_glove)
        self.update_health()

    # =====================================================
    # VISUAL HELPERS (hit/block)
    # =====================================================

    def flash_block(self):
        # Briefly change player glove color to show block
        self.canvas.itemconfig(self.player_glove, fill="yellow")
        self.root.after(200, lambda: self.canvas.itemconfig(self.player_glove, fill="red"))

    def flash_player_hit(self):
        # Briefly flash player body red
        self.canvas.itemconfig(self.player_body, fill="darkred")
        self.root.after(200, lambda: self.canvas.itemconfig(self.player_body, fill="blue"))

    def flash_enemy_hit(self):
        # Briefly flash enemy body white
        self.canvas.itemconfig(self.enemy_body, fill="white")
        self.root.after(200, lambda: self.canvas.itemconfig(self.enemy_body, fill=BOSSES[self.current_boss]["color"]))

    # =====================================================
    # RESET GLOVE
    # =====================================================

    def reset_glove(self):
        self.canvas.coords(self.player_glove, 610, 390, 690, 470)

    # =====================================================
    # UPDATE HEALTH
    # =====================================================

    def update_health(self):

        self.canvas.coords(self.player_bar, 100, 80, 100 + (self.player_health * 100), 110)
        self.canvas.coords(self.enemy_bar, 1400 - (self.enemy_health * 100), 80, 1400, 110)

        if self.player_health <= 0:
            self.match_over = True
            self.player_knockout()
            return

        if self.enemy_health <= 0:
            self.match_over = True
            self.enemy_knockout()
            return

        if not self.counter_window_open and not self.match_over:
            self.root.after(2000, self.enemy_attack)

    # =====================================================
    # PLAYER KO (fall animation)
    # =====================================================

    def player_knockout(self):

        self.enemy_attacking = False
        self.counter_window_open = False
        self.counter_ready = False

        self.canvas.itemconfig(self.status, text="YOU WERE KNOCKED OUT!")
        self.animate_player_fall(step=0)

    def animate_player_fall(self, step):

        if step < 20:
            for item in (self.player_head, self.player_body, self.player_belt, self.player_glove):
                self.canvas.move(item, -5, 10)
            self.root.after(60, lambda: self.animate_player_fall(step+1))
        else:
            self.root.after(1500, self.restart_boxing)

    # =====================================================
    # ENEMY KO (fall animation + points)
    # =====================================================

    def enemy_knockout(self):

        self.enemy_attacking = False
        self.counter_window_open = False
        self.counter_ready = False

        self.canvas.itemconfig(self.status, text="KNOCKOUT WIN!")
        self.points += 10
        self.boxing_wins += 1

        if self.current_boss < len(BOSSES) - 1:
            self.current_boss += 1

        self.animate_enemy_fall(step=0)

    def animate_enemy_fall(self, step):

        if step < 20:
            for item in (self.enemy_head, self.enemy_body, self.enemy_belt, self.enemy_glove):
                self.canvas.move(item, 5, 10)
            self.root.after(60, lambda: self.animate_enemy_fall(step+1))
        else:
            self.root.after(1500, self.victory)

    # =====================================================
    # RESTART BOXING (after losing)
    # =====================================================

    def restart_boxing(self):

        messagebox.showinfo("Defeat", "You were knocked out. Try again!")
        self.start_boxing()
    # =====================================================
    # VICTORY (after winning a boxing match)
    # =====================================================

    def victory(self):

        messagebox.showinfo(
            "Round Complete",
            f"You won the boxing match!\n\n"
            f"+10 Points Earned\n"
            f"Total Points: {self.points}/100\n"
            f"Education Rounds: {self.education_wins}/10\n"
            f"Boxing Wins: {self.boxing_wins}/10"
        )

        if self.points >= 100:
            self.final_scene()
            return

        self.education_instructions()

    # =====================================================
    # FINAL SCENE — GAME BEATEN
    # =====================================================

    def final_scene(self):

        self.clear_screen()

        # Only now do questions reset (no repeats before 100 points)
        self.used_questions = []

        tk.Label(
            self.root,
            text="🏆 WORLD CHAMPION 🏆",
            font=("Arial", 60, "bold"),
            fg="gold",
            bg="black"
        ).pack(pady=60)

        tk.Label(
            self.root,
            text=f"Congratulations, {self.player_name}!",
            font=("Arial", 40, "bold"),
            fg="white",
            bg="black"
        ).pack(pady=20)

        tk.Label(
            self.root,
            text="You mastered all 90 SOL questions\nand defeated all 10 opponents!",
            font=("Arial", 32),
            fg="cyan",
            bg="black"
        ).pack(pady=20)

        tk.Label(
            self.root,
            text="🏅 You earned the SOL Champion Medal! 🏅",
            font=("Arial", 34, "bold"),
            fg="lime",
            bg="black"
        ).pack(pady=40)

        dance_label = tk.Label(
            self.root,
            text="💃🕺 CELEBRATION DANCE! 🕺💃",
            font=("Arial", 36, "bold"),
            fg="yellow",
            bg="black"
        )
        dance_label.pack(pady=40)

        def flash():
            current = dance_label.cget("fg")
            dance_label.config(fg="yellow" if current == "red" else "red")
            self.root.after(300, flash)

        flash()

        self.root.after(10000, self.end_game)

    # =====================================================
    # END GAME → Return to Start Menu
    # =====================================================

    def end_game(self):

        messagebox.showinfo(
            "Game Complete",
            "Thank you for playing SOL Punch Out!\nReturning to main menu."
        )

        self.start_menu()

# =========================================================
# RUN GAME (MAIN LOOP)
# =========================================================

root = tk.Tk()
game = SOLPunchOut(root)
root.mainloop()
