from tkinter import *
import time

clock = None
test_text = "learn most boy serve animal plain thought better west " \
            "speed thought carry most any world dry this base note clear hard other took old study some " \
            "during amair short our girl picture noun big better while made fine children letter low " \
            "decide build left form my possible tail water knew too door eat goon object find fish hour " \
            "work their found blue during begin also noun sing pattern at common over whole pounds tree " \
            "at give must town hot food money be of boat door port build remember remember small music keep " \
            "word farm press above carry ready got language beauty each very special pattern name king who home is land"


def reset_timer():
    """Reset the timer"""
    type.config(state="normal")
    type.delete('1.0', END)
    timer.after_cancel(clock)
    timer.config(text=f"00:00")

def start_count():
    """Start the countdown when the user starts typing"""
    time.sleep(1.5)
    # Activate the typing box
    type.config(state="normal")
    type.focus()
    speed_timer(59)

def get_word():
    """
    Compare the words typed to the actual words to determine how many were typed correctly.
    Order is really important.
    """
    correct_words = 0
    typed_words = type.get("1.0",'end-1c')
    test_words = test_text.split()
    lst_typed_words = typed_words.split()
    for t_word in range(len(lst_typed_words)):
        if lst_typed_words[t_word] == test_words[t_word]:
            correct_words += 1
    # Disable the typing area so that the user doen't keep typing
    type.config(state="disabled")
    # Return the number of correctly typed words.
    score.config(text=f'Score: {correct_words}wpm')


def speed_timer(start_time):
    """
    Takes in the one minute timer.
    Updates the timer label (after which calls the same function for iteration) until it reaches zero.
    When timer reaches zero, call the get_word() to get the number of typed words per minute
    :param start_time:
    :return:
    """
    global clock
    timer.config(text=f"00:{start_time}")
    if start_time < 10:
        timer.config(text=f"00:0{start_time}")
    if start_time != 0:
        clock = timer.after(1000, speed_timer, start_time-1)
    elif start_time == 0:
        get_word()


window = Tk()
window.geometry('900x550')
window.config(bg='#34B3F1', pady=40, padx=40)
window.title("Type SpeedTest")
icon = PhotoImage(file='typing.png')
# logo = PhotoImage(file='type_big_2.png')
window.iconphoto(False, icon)
# canvas = Canvas(width=350, height=350, highlightthickness=0, background='#34B3F1')
# canvas.create_image(150, 150, image=logo)
# canvas.create_text(100, 300, text="00:00", font=("Courier", 50, 'bold'))
# canvas.grid(row=1, column=1)

# Timer
timer = Label(text="00:00", background="#34B3F1", foreground="#F15412", font=("Courier", 40, 'bold'), pady=15, padx=15)
timer.grid(row=1, column=1)

# Start Button
start = Button(text='Start ▶', width=15, height=2, background="#F15412", font=("Courier", 15, 'bold'), command=start_count)
start.grid(row=2, column=0)
start.focus()

# Reset Button
reset = Button(text='Reset 🔄', width=15, height=2, background="#F15412", font=("Courier", 15, 'bold'), command=reset_timer)
reset.grid(row=2, column=1)

# Display Score
score = Label(text="Score: 0",  background="#F15412", font=("Courier", 20, 'bold'), pady=15, padx=15)
score.grid(row=2, column=2)

# Text To Type
txt = Text(padx=10, pady=10, background="#EEEEEE", height=8, font=("Courier", 13, 'bold'))
txt.grid(row=3, column=0, columnspan=3)
txt.insert(END, test_text)
txt.config(state= "disabled")

# Typing Area Label
type_label = Label(text="Type the above text here", background='#34B3F1', font=("Courier", 20, 'bold'))
type_label.grid(row=5, column=1)

# Typing Area
type = Text(padx=5, pady=5, background="#EEEEEE", height=5, font=("Courier", 13, 'bold'))
type.grid(row=6, column=0, columnspan=3)
type.config(state= "disabled")


window.mainloop()
