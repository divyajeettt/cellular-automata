import tkinter as tk
import tkinter.messagebox as msg


def callback(string):
    return string.isnumeric() or not string


def start():
    global N

    if not (N := number.get()):
        msg.showwarning("Empty Field", "Please enter required number of cells")
        return
    if (N := int(N)) in range(2):
        msg.showwarning("Invalid Value", "Number of cells cannot be 0 or 1")
        return

    root.destroy()


def main():
    global number, root

    root = tk.Tk()
    root.title("Welcome to the game")

    tk.Label(
        text="Enter the number of cells you\nwant in the side of the square",
        font=("consolas", 12, "bold")
    ).pack()

    number = tk.Entry(
        root, width=35, bd=3, font=("consolas", 12, "bold"),
        validate="key", validatecommand=(root.register(callback), "%P")
    )
    number.pack()
    number.bind("<Return>", lambda evt: start())

    tk.Button(
        root, text="Start", width=35, bd=3, font=("consolas", 12, "bold"),
        command=start
    ).pack()

    root.mainloop()


if __name__ == "__main__":
    main()