# =========================================================
# SOL PUNCH OUT - EDUCATION + ARCADE BOXING EDITION
# FULL GAME VERSION
# =========================================================
# FEATURES
# ---------------------------------------------------------
# ✔ Education questions FIRST
# ✔ Multiple choice works correctly
# ✔ Different randomized questions
# ✔ Boxing after questions
# ✔ 10 total wins to beat game
# ✔ Visible enemy punches
# ✔ Slower readable attacks
# ✔ Extra counter time
# ✔ Realistic boxer graphics
# ✔ Different bosses
# ✔ Difficulty settings
# ✔ Health bars
# ✔ Crowd arena
# ✔ Spacebar counter punches
# ✔ Epic final ending
# =========================================================

import tkinter as tk
from tkinter import messagebox
import random

# =========================================================
# QUESTIONS
# =========================================================

QUESTIONS = [

    {
        "subject": "Math",
        "q": "5 + 5 = ?",
        "choices": ["10", "7", "15", "20"],
        "a": "10"
    },

    {
        "subject": "Math",
        "q": "9 x 9 = ?",
        "choices": ["81", "72", "99", "65"],
        "a": "81"
    },

    {
        "subject": "Reading",
        "q": "What is the main idea called?",
        "choices": ["theme", "chapter", "ending", "table"],
        "a": "theme"
    },

    {
        "subject": "Writing",
        "q": "What is an action word?",
        "choices": ["verb", "noun", "adjective", "comma"],
        "a": "verb"
    },

    {
        "subject": "Math",
        "q": "20 / 4 = ?",
        "choices": ["5", "4", "6", "8"],
        "a": "5"
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
        "choices": [".", "!", "?", ","],
        "a": "."
    }

]

# =========================================================
# BOSSES
# =========================================================

BOSSES = [

    {
        "name": "Iron Mike",
        "color": "red",
        "gloves": "black",
        "speed": 2300
    },

    {
        "name": "Crusher Kane",
        "color": "purple",
        "gloves": "gold",
        "speed": 2000
    },

    {
        "name": "Venom Viper",
        "color": "green",
        "gloves": "lime",
        "speed": 1700
    },

    {
        "name": "TITAN KING",
        "color": "darkred",
        "gloves": "white",
        "speed": 1500
    }

]

# =========================================================
# MAIN GAME
# =========================================================

class SOLPunchOut:

    def __init__(self, root):

        self.root = root
        self.root.title("SOL Punch Out Arcade")
        self.root.geometry("1400x900")
        self.root.configure(bg="black")

        # GAME VARIABLES
        self.total_wins = 0
        self.current_boss = 0

        self.player_health = 100
        self.enemy_health = 100

        self.question_index = 0
        self.correct_answers = 0

        self.expected_dodge = None
        self.dodge_success = False

        self.counter_ready = False

        # CONTROLS
        self.root.bind("<Up>", self.up_pressed)
        self.root.bind("<Down>", self.down_pressed)

        # SPACEBAR COUNTER
        self.root.bind("<space>", self.counter_attack)

        self.start_menu()

    # =====================================================
    # MENU
    # =====================================================

    def start_menu(self):

        self.clear_screen()

        tk.Label(
            self.root,
            text="SOL PUNCH OUT",
            font=("Arial", 50, "bold"),
            fg="gold",
            bg="black"
        ).pack(pady=50)

        tk.Label(
            self.root,
            text="Choose Difficulty",
            font=("Arial", 24),
            fg="white",
            bg="black"
        ).pack()

        self.diff_var = tk.StringVar(value="Normal")

        for diff in ["Easy", "Normal", "Hard", "Champion"]:

            tk.Radiobutton(
                self.root,
                text=diff,
                variable=self.diff_var,
                value=diff,
                font=("Arial", 22),
                fg="white",
                bg="black",
                selectcolor="darkred"
            ).pack()

        tk.Button(
            self.root,
            text="START GAME",
            font=("Arial", 24, "bold"),
            bg="red",
            fg="white",
            width=18,
            command=self.start_game
        ).pack(pady=40)

    # =====================================================
    # START GAME
    # =====================================================

    def start_game(self):

        self.difficulty = self.diff_var.get()

        self.total_wins = 0
        self.current_boss = 0

        self.prepare_questions()
        self.show_question()

    # =====================================================
    # QUESTIONS
    # =====================================================

    def prepare_questions(self):

        self.questions = QUESTIONS[:]

        random.shuffle(self.questions)

        self.question_index = 0

    # =====================================================
    # SHOW QUESTION
    # =====================================================

    def show_question(self):

        # QUESTIONS COMPLETE
        if self.question_index >= 5:

            self.start_boxing()
            return

        self.clear_screen()

        question = self.questions[self.question_index]

        tk.Label(
            self.root,
            text=f"Question {self.question_index + 1}/5",
            font=("Arial", 30, "bold"),
            fg="gold",
            bg="black"
        ).pack(pady=20)

        tk.Label(
            self.root,
            text=question["subject"],
            font=("Arial", 26),
            fg="cyan",
            bg="black"
        ).pack()

        tk.Label(
            self.root,
            text=question["q"],
            font=("Arial", 34),
            fg="white",
            bg="black",
            wraplength=1100
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
                selectcolor="darkblue",
                activebackground="black",
                activeforeground="yellow"
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

        selected = self.answer_var.get()

        if selected == "":

            messagebox.showwarning(
                "No Answer",
                "Please select an answer."
            )

            return

        question = self.questions[self.question_index]

        if selected == question["a"]:

            self.correct_answers += 1

            messagebox.showinfo(
                "Correct!",
                "Great job!"
            )

        else:

            messagebox.showinfo(
                "Incorrect",
                f"Correct answer: {question['a']}"
            )

        self.question_index += 1

        self.show_question()

    # =====================================================
    # CLEAR SCREEN
    # =====================================================

    def clear_screen(self):

        for widget in self.root.winfo_children():
            widget.destroy()

    # =====================================================
    # START BOXING
    # =====================================================

    def start_boxing(self):

        self.clear_screen()

        self.player_health = 100
        self.enemy_health = 100

        boss = BOSSES[self.current_boss]

        # DIFFICULTY
        if self.difficulty == "Easy":
            self.enemy_speed = boss["speed"] + 800

        elif self.difficulty == "Normal":
            self.enemy_speed = boss["speed"]

        elif self.difficulty == "Hard":
            self.enemy_speed = boss["speed"] - 300

        else:
            self.enemy_speed = boss["speed"] - 500

        # TITLE
        tk.Label(
            self.root,
            text=f"YOU VS {boss['name']}",
            font=("Arial", 36, "bold"),
            fg="gold",
            bg="black"
        ).pack()

        self.status = tk.Label(
            self.root,
            text="WATCH THE PUNCHES!",
            font=("Arial", 24, "bold"),
            fg="lime",
            bg="black"
        )

        self.status.pack()

        # CANVAS
        self.canvas = tk.Canvas(
            self.root,
            width=1300,
            height=700,
            bg="gray10",
            highlightthickness=0
        )

        self.canvas.pack(pady=10)

        # CROWD
        crowd_colors = [
            "red",
            "blue",
            "yellow",
            "green",
            "purple",
            "orange"
        ]

        for i in range(80):

            x = random.randint(0, 1300)
            y = random.randint(0, 120)

            self.canvas.create_oval(
                x,
                y,
                x + 20,
                y + 20,
                fill=random.choice(crowd_colors)
            )

        # RING
        self.canvas.create_rectangle(
            100,
            150,
            1200,
            620,
            outline="white",
            width=8
        )

        # ROPES
        for y in [230, 330, 430]:

            self.canvas.create_line(
                100,
                y,
                1200,
                y,
                fill="white",
                width=5
            )

        # =================================================
        # PLAYER BOXER
        # =================================================

        self.player_head = self.canvas.create_oval(
            250,
            180,
            340,
            270,
            fill="peachpuff"
        )

        self.player_body = self.canvas.create_rectangle(
            250,
            270,
            340,
            430,
            fill="dodgerblue"
        )

        self.canvas.create_rectangle(
            250,
            390,
            340,
            450,
            fill="blue"
        )

        self.player_glove_left = self.canvas.create_oval(
            180,
            300,
            250,
            360,
            fill="red"
        )

        self.player_glove_right = self.canvas.create_oval(
            340,
            300,
            410,
            360,
            fill="red"
        )

        # =================================================
        # ENEMY BOXER
        # =================================================

        self.enemy_head = self.canvas.create_oval(
            930,
            180,
            1020,
            270,
            fill="tan"
        )

        self.enemy_body = self.canvas.create_rectangle(
            930,
            270,
            1020,
            430,
            fill=boss["color"]
        )

        self.enemy_glove_left = self.canvas.create_oval(
            860,
            300,
            930,
            360,
            fill=boss["gloves"]
        )

        self.enemy_glove_right = self.canvas.create_oval(
            1020,
            300,
            1090,
            360,
            fill=boss["gloves"]
        )

        # HEALTH BARS
        self.player_health_bar = self.canvas.create_rectangle(
            100,
            70,
            400,
            100,
            fill="lime"
        )

        self.enemy_health_bar = self.canvas.create_rectangle(
            900,
            70,
            1200,
            100,
            fill="red"
        )

        self.canvas.create_text(
            250,
            45,
            text="PLAYER",
            fill="white",
            font=("Arial", 18, "bold")
        )

        self.canvas.create_text(
            1050,
            45,
            text=boss["name"],
            fill="white",
            font=("Arial", 18, "bold")
        )

        # START FIGHT
        self.root.after(2500, self.enemy_attack)

    # =====================================================
    # ENEMY ATTACK
    # =====================================================

    def enemy_attack(self):

        self.counter_ready = False

        attack = random.choice(["face", "body"])

        self.expected_dodge = attack
        self.dodge_success = False

        self.status.config(
            text=f"{BOSSES[self.current_boss]['name']} throws a {attack.upper()} punch!"
        )

        # ===============================================
        # SHOW PUNCH COMING FIRST
        # ===============================================

        if attack == "face":

            # windup
            self.canvas.move(self.enemy_glove_left, 60, -30)

            self.root.after(
                500,
                lambda: self.throw_face_punch()
            )

        else:

            # windup
            self.canvas.move(self.enemy_glove_right, 60, 30)

            self.root.after(
                500,
                lambda: self.throw_body_punch()
            )

    # =====================================================
    # FACE PUNCH
    # =====================================================

    def throw_face_punch(self):

        self.canvas.move(self.enemy_glove_left, -250, -80)
        self.canvas.move(self.enemy_body, -50, 0)

        self.root.after(
            self.enemy_speed,
            self.evaluate_attack
        )

    # =====================================================
    # BODY PUNCH
    # =====================================================

    def throw_body_punch(self):

        self.canvas.move(self.enemy_glove_right, -250, 80)
        self.canvas.move(self.enemy_body, -50, 0)

        self.root.after(
            self.enemy_speed,
            self.evaluate_attack
        )

    # =====================================================
    # EVALUATE ATTACK
    # =====================================================

    def evaluate_attack(self):

        # reset enemy
        self.canvas.coords(
            self.enemy_glove_left,
            860,
            300,
            930,
            360
        )

        self.canvas.coords(
            self.enemy_glove_right,
            1020,
            300,
            1090,
            360
        )

        self.canvas.coords(
            self.enemy_body,
            930,
            270,
            1020,
            430
        )

        if not self.dodge_success:

            self.player_health -= 15

            self.status.config(
                text="YOU GOT HIT!"
            )

        else:

            self.counter_ready = True

            self.status.config(
                text="DODGED! PRESS SPACEBAR TO COUNTER!"
            )

            # EXTRA COUNTER TIME
            self.root.after(
                1800,
                self.end_counter_window
            )

        self.update_health()

    # =====================================================
    # END COUNTER WINDOW
    # =====================================================

    def end_counter_window(self):

        self.counter_ready = False

    # =====================================================
    # DODGE CONTROLS
    # =====================================================

    def up_pressed(self, event):

        if self.expected_dodge == "face":

            self.dodge_success = True

            self.canvas.move(
                self.player_head,
                0,
                -60
            )

            self.root.after(
                300,
                self.reset_player
            )

    def down_pressed(self, event):

        if self.expected_dodge == "body":

            self.dodge_success = True

            self.canvas.move(
                self.player_body,
                0,
                60
            )

            self.root.after(
                300,
                self.reset_player
            )

    # =====================================================
    # RESET PLAYER
    # =====================================================

    def reset_player(self):

        self.canvas.coords(
            self.player_head,
            250,
            180,
            340,
            270
        )

        self.canvas.coords(
            self.player_body,
            250,
            270,
            340,
            430
        )

    # =====================================================
    # COUNTER ATTACK
    # =====================================================

    def counter_attack(self, event):

        if self.counter_ready:

            self.enemy_health -= 20

            self.status.config(
                text="COUNTER PUNCH LANDED!"
            )

            # visible punch
            self.canvas.move(
                self.player_glove_right,
                250,
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
            self.player_glove_right,
            340,
            300,
            410,
            360
        )

    # =====================================================
    # UPDATE HEALTH
    # =====================================================

    def update_health(self):

        # PLAYER BAR
        self.canvas.coords(
            self.player_health_bar,
            100,
            70,
            100 + (self.player_health * 3),
            100
        )

        # ENEMY BAR
        self.canvas.coords(
            self.enemy_health_bar,
            1200 - (self.enemy_health * 3),
            70,
            1200,
            100
        )

        # PLAYER WINS MATCH
        if self.enemy_health <= 0:

            self.total_wins += 1

            if self.total_wins >= 10:

                self.epic_ending()
                return

            messagebox.showinfo(
                "Victory",
                f"You won match #{self.total_wins}!"
            )

            self.current_boss += 1

            if self.current_boss >= len(BOSSES):
                self.current_boss = 0

            self.prepare_questions()
            self.show_question()

            return

        # PLAYER LOSES
        if self.player_health <= 0:

            messagebox.showinfo(
                "Knockout",
                "You were knocked out!"
            )

            self.start_boxing()
            return

        self.root.after(
            1800,
            self.enemy_attack
        )

    # =====================================================
    # EPIC ENDING
    # =====================================================

    def epic_ending(self):

        self.clear_screen()

        tk.Label(
            self.root,
            text="🏆 WORLD CHAMPION 🏆",
            font=("Arial", 54, "bold"),
            fg="gold",
            bg="black"
        ).pack(pady=40)

        tk.Label(
            self.root,
            text="YOU DEFEATED TITAN KING!",
            font=("Arial", 36, "bold"),
            fg="red",
            bg="black"
        ).pack(pady=20)

        tk.Label(
            self.root,
            text="🔥 GREATEST BOXER OF ALL TIME 🔥",
            font=("Arial", 34, "bold"),
            fg="lime",
            bg="black"
        ).pack(pady=40)

        tk.Button(
            self.root,
            text="PLAY AGAIN",
            font=("Arial", 24, "bold"),
            bg="red",
            fg="white",
            command=self.start_menu
        ).pack(pady=50)

# =========================================================
# RUN GAME
# =========================================================

root = tk.Tk()

game = SOLPunchOut(root)

root.mainloop()