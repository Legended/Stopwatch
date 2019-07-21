import tkinter as tk
from tkinter import ttk
from datetime import timedelta
from contextlib import suppress


class Stopwatch:

    var = 0
    stopwatch = None

    def __init__(self, master):
        """Widgets"""

        # Stopwatch display.
        self.timer = ttk.Label(master, text='0:00:00.000', font=('System', 40), relief='sunken')
        self.timer.grid(row=0, column=0, columnspan=3)

        # Start button for initiating the stopwatch.
        self.start_button = ttk.Button(master, text='Start',
                                       command=lambda: (self.start_button.grid_forget(),
                                                        self.stop_button.grid(row=1, column=0),
                                                        self.start(self.var)))
        self.start_button.grid(row=1, column=0)

        # Stop button for pausing the stopwatch.
        self.stop_button = ttk.Button(master, text='Stop',
                                      command=lambda: (self.stop_button.grid_forget(),
                                                       self.start_button.grid(row=1, column=0),
                                                       root.after_cancel(self.stopwatch)))

        # Reset button for resetting the stopwatch.
        self.reset_button = ttk.Button(master, text='Reset',
                                       command=lambda: (self.stop_button.grid_forget(),
                                                        self.start_button.grid(row=1, column=0),
                                                        self.reset()))
        self.reset_button.grid(row=1, column=1)

        # Exit button for closing the program.
        self.exit_button = ttk.Button(master, text='Exit', command=root.quit)
        self.exit_button.grid(row=1, column=2)

    def start(self, num):
        """Initiates the stopwatch."""
        self.var = num
        t = str(timedelta(milliseconds=num))
        self.timer.config(text=(t[0:11] if '.' in t else f'{t}.000'))
        self.stopwatch = root.after(1, self.start, num + 1)

    def reset(self):
        """Resets the stopwatch and sets variables to default values."""
        with suppress(ValueError):
            root.after_cancel(self.stopwatch)
            self.var = 0
            self.stopwatch = None
            self.timer.config(text='0:00:00.000')


def main():
    global root

    root = tk.Tk()
    root.config(padx=10, pady=10)
    root.title('Stopwatch')
    root.resizable(False, False)
    Stopwatch(root)

    # Set window to open in the center of the screen.
    root.update()
    x = (root.winfo_screenwidth() / 2) - (root.winfo_width() / 2)
    y = (root.winfo_screenheight() / 2) - (root.winfo_height() / 2)
    root.geometry('+%d+%d' % (x, y))

    root.mainloop()
    

if __name__ == '__main__':
    main()
