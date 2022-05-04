import tkinter as tk
import tkinter.ttk as ttk
from turtle import left

window = tk.Tk()

for y in range(5):
    window.columnconfigure(y, weight=1, minsize=75)
    window.rowconfigure(y, weight=1, minsize=50)
    for x in range(3):
        frame1 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
        frame1.grid(row=y, column=x, padx=5, pady=5)
        # if y == 0 and x == 0:
        if y == 0 and x == 1:
            label = tk.Label(master=frame1, text="Master Mind", fg="white", bg="black")
            label.pack()
        #if y == 0 and x == 2:
        if y == 1 and x == 0:
            label = tk.Label(master=frame1, text="Player one", fg="white", bg="black")
            label.pack()
        #if y == 1 and x == 1:
        if y == 1 and x == 2:
            label = tk.Label(master=frame1, text="Player two", fg="white", bg="black")
            label.pack()
        if y == 2 and x == 0:
            label = tk.Label(master=frame1, text="Result:", fg="white", bg="black")
            label.pack()
            for q in range(1):
                for i in range(5):
                    label = tk.Label(master=frame1, bg="white", height=2, width=5, relief=tk.RIDGE)
                    label.pack(side=tk.LEFT)
        #if y == 2 and x == 1:
        if y == 2 and x == 2:
            label = tk.Label(master=frame1, text="Result:", fg="white", bg="black")
            label.pack()
            for q in range(1):
                for i in range(5):
                    label = tk.Label(master=frame1, bg="white", height=2, width=5, relief=tk.RIDGE)
                    label.pack(side=tk.RIGHT)
        if y == 3 and x == 0:
            label = tk.Label(master=frame1, text="Sequence guess:", fg="white", bg="black")
            label.pack()
            for q in range(1):
                for i in range(5):
                    label = tk.Label(master=frame1, bg="white", height=2, width=5, relief=tk.RIDGE)
                    label.pack(side=tk.LEFT)
        #if y == 3 and x == 1:
        if y == 3 and x == 2:
            label = tk.Label(master=frame1, text="Sequence guess:", fg="white", bg="black")
            label.pack()
            for q in range(1):
                for i in range(5):
                    label = tk.Label(master=frame1, bg="white", height=2, width=5, relief=tk.RIDGE)
                    label.pack(side=tk.RIGHT)
        if y == 4 and x == 0:
            p1_button_red = tk.Button(master=frame1, relief=tk.RIDGE, text="Red", width=10, bg="red", fg="black")
            p1_button_yellow = tk.Button(master=frame1, relief=tk.RIDGE, text="Yellow", width=10, bg="yellow", fg="black")
            p1_button_blue = tk.Button(master=frame1, relief=tk.RIDGE, text="Blue", width=10, bg="blue", fg="black")
            p1_button_orange = tk.Button(master=frame1, relief=tk.RIDGE, text="Orange", width=10, bg="orange", fg="black")
            p1_button_green = tk.Button(master=frame1, relief=tk.RIDGE, text="Green", width=10, bg="lightgreen", fg="black")
            p1_button_purple = tk.Button(master=frame1, relief=tk.RIDGE, text="Purple", width=10, bg="purple", fg="black")

            p1_button_remove = tk.Button(master=frame1, relief=tk.RIDGE, text="Remove", width=10, bg="black", fg="white")
            p1_button_confirm = tk.Button(master=frame1, relief=tk.RIDGE, text="Confirm", width=10, bg="green", fg="black", padx=5, pady=5)
            p1_button_red.pack(side=tk.LEFT)
            p1_button_yellow.pack(side=tk.LEFT)
            p1_button_blue.pack(side=tk.LEFT)
            p1_button_orange.pack(side=tk.LEFT)
            p1_button_green.pack(side=tk.LEFT)
            p1_button_purple.pack(side=tk.LEFT)

            p1_button_remove.pack(side=tk.LEFT)
            p1_button_confirm.pack(side=tk.LEFT)
        #if y == 4 and x == 1:
        if y == 4 and x == 2:
            p2_button_red = tk.Button(master=frame1, relief=tk.RIDGE, text="Red", width=10, bg="red", fg="black")
            p2_button_yellow = tk.Button(master=frame1, relief=tk.RIDGE, text="Yellow", width=10, bg="yellow", fg="black")
            p2_button_blue = tk.Button(master=frame1, relief=tk.RIDGE, text="Blue", width=10, bg="blue", fg="black")
            p2_button_orange = tk.Button(master=frame1, relief=tk.RIDGE, text="Orange", width=10, bg="orange", fg="black")
            p2_button_green = tk.Button(master=frame1, relief=tk.RIDGE, text="Green", width=10, bg="lightgreen", fg="black")
            p2_button_purple = tk.Button(master=frame1, relief=tk.RIDGE, text="Purple", width=10, bg="purple", fg="black")

            p2_button_remove = tk.Button(master=frame1, relief=tk.RIDGE, text="Remove", width=10, bg="black", fg="white")
            p2_button_confirm = tk.Button(master=frame1, relief=tk.RIDGE, text="Confirm", width=10, bg="green", fg="black", padx=5, pady=5)

            p2_button_red.pack(side=tk.LEFT)
            p2_button_yellow.pack(side=tk.LEFT)
            p2_button_blue.pack(side=tk.LEFT)
            p2_button_orange.pack(side=tk.LEFT)
            p2_button_green.pack(side=tk.LEFT)
            p2_button_purple.pack(side=tk.LEFT)

            p2_button_remove.pack(side=tk.LEFT)
            p2_button_confirm.pack(side=tk.LEFT)


# entry.insert(0, "Guess the color here, starting from the left: ")
# entry_Two.insert(0, "Guess the color here, starting from the left: ")
# frame_a.grid()
# frame_b.grid()
#frame.grid(row=1, column=2, padx=5, pady=5)

# entry.delete(0, tk.END)
# entry.insert(0, "wow")

window.mainloop()
# window.destroy()