"""
A Tkinter GUI desktop application that tests your typing speed.
Using Tkinter and what you have learnt about building GUI applications
with Python, build a desktop app that assesses your typing speed.
Give the user some sample text and detect how many words they can type per minute.
The average typing speed is 40 words per minute.
But with practice, you can speed up to 100 words per minute.
You can try out a web version here:
https://typing-speed-test.aoeu.eu/

If you have more time, you can build your typing speed test into a typing trainer,
with high scores and more text samples. You can design your program any way you want.
Questions for this assignment
Reflection Time: This is a place to journal your experience of completing this project.
This will help you figure out how to improve as a developer.
Write down how you approached the project. What was hard, what was easy.
How might you improve for the next project? What was your biggest learning from today?
 What would you do differently if you were to tackle this project again?
"""
from tkinter import *
from timeit import default_timer as timer
import random

#creating new windows and configurations
window = Tk()
window.geometry("450x200")

#labels
x = 0
def game():
    global x
    if x == 0:
        window.destroy()
        x=x+1
    def check_result():
        if entry.get() == words[word]:
            end= timer()
            print(end - start)
        else:
            print("wrong spelling")
    words = ["programming", "coding", "debugging", "testing", "compiling", "integration", "running"]
    word = random.randint(0, (len(words)-1))
    start = timer()
    windows = Tk()
    windows.geometry("450x200")
    val_x2 = Label(windows, text=words[word], font="times 20")
    val_x2.place(x=150, y=10)
    val_x3 = Label(windows, text="lets see how fast you ca write", font="times 20")
    val_x3.place(x=10, y=50)
    entry = Entry(windows)
    entry.place(x=280, y=100)
    val_b1 = Button(windows, text="Done", command=check_result, width=12, bg="grey")
    val_b1.place(x=150, y=100)
    val_b2 = Button(windows, text="Wanna try again", command=game, width=12, bg="grey")
    val_b2.place(x=150, y=100)
    windows.mainloop()

val_x = Label(window, text="lets start this game...", font="times 20")
val_x.place(x=10, y=50)
val_b = Button(window, text="Goo",command=game, width=12, bg="grey")
val_b.place(x=150, y=100)
window.mainloop()
