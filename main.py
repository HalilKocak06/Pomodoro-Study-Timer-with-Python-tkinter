import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="LONG BREAK TIME", bg=PINK, fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="BREAK TIME", bg=PINK, fg=GREEN)
        count_down(short_break_sec)
    else:
        title_label.config(text="STUDY TIME", bg=PINK, fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✅"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=PINK)

# TIMER Yazısı
title_label = tk.Label(text="TIMER", bg=PINK, fg=GREEN, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato = tk.PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Start butonu
start_button = tk.Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

# Reset butonu
reset_button = tk.Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

# Checkmark
check_marks = tk.Label(fg=GREEN, bg=PINK)
check_marks.grid(column=1, row=3)

window.mainloop()
