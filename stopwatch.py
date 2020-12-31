import tkinter as tk
from tkinter import ttk
from datetime import timedelta
from contextlib import suppress


class Stopwatch(tk.Frame):
    var = 0
    stopwatch = None

    def __init__(self, master: tk.Tk, *args, **kwargs):
        """Widgets"""
        self.master = master
        super().__init__(self.master, *args, **kwargs)

        # Stopwatch display.
        self.timer = ttk.Label(self.master, text='0:00:00.000', font=('System', 40), relief='sunken')
        self.timer.grid(row=0, column=0, columnspan=3)

        # Start button for initiating the stopwatch.
        self.start_button = ttk.Button(self.master, text='Start',
                                       command=lambda: (self.start_button.grid_forget(),
                                                        self.stop_button.grid(row=1, column=0),
                                                        self.start(self.var)))
        self.start_button.grid(row=1, column=0)

        # Stop button for pausing the stopwatch.
        self.stop_button = ttk.Button(self.master, text='Stop',
                                      command=lambda: (self.stop_button.grid_forget(),
                                                       self.start_button.grid(row=1, column=0),
                                                       self.master.after_cancel(self.stopwatch)))

        # Reset button for resetting the stopwatch.
        self.reset_button = ttk.Button(self.master, text='Reset',
                                       command=lambda: (self.stop_button.grid_forget(),
                                                        self.start_button.grid(row=1, column=0),
                                                        self.reset()))
        self.reset_button.grid(row=1, column=1)

        # Exit button for closing the program.
        self.exit_button = ttk.Button(self.master, text='Exit', command=self.master.quit)
        self.exit_button.grid(row=1, column=2)

    def start(self, ms: int):
        """Initiates the stopwatch."""
        self.var = ms
        t = str(timedelta(milliseconds=ms))
        self.timer.config(text=(t[0:11] if '.' in t else f'{t}.000'))
        self.stopwatch = self.master.after(1, self.start, ms + 1)

    def reset(self):
        """Resets the stopwatch and sets variables to default values."""
        with suppress(ValueError):
            self.master.after_cancel(self.stopwatch)
            self.var = 0
            self.stopwatch = None
            self.timer.config(text='0:00:00.000')


def main():
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
