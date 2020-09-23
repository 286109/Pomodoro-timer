import tkinter as tk
from tkinter import ttk, NSEW, NS
import time


class Clock():
    def __init__(self):
        self.root = tk.Tk()
        self.style = ttk.Style()
        self.style.configure("BW.TLabel", font=(
            'Helvetica', 18),  foreground="black")
        self.label = ttk.Label(text="", style='BW.TLabel')
        # self.label = ttk.Label(text="")

        self.label.grid(row=0, column=0, columnspan=3, sticky=NS)
        self._pomodoro_time_limit = 20 * 60
        self._pomodoro_starttime = time.time()
        self.start_button = ttk.Button(text='Start', command=self.start_timer)
        self.start_button.grid(row=1, column=0)
        self.progressbar = ttk.Progressbar()
        self.progressbar.grid(row=2, column=0, columnspan=3)

        self.time_input_label = ttk.Label(text="User Name")
        self.time_input_label.grid(row=1, column=1)
        self.time_input_entry = ttk.Entry()
        self.time_input_entry.grid(row=1, column=2)

    def update_clock(self):
        now = int(time.time() - self._pomodoro_starttime)
        # Остановка таймера при достижении лимита времени
        if now > self._pomodoro_time_limit:
            self.root.after_cancel(self._timer_job)
            return

        self.label.configure(text=self.get_formatted_time(now),)
        # Запуск таймера
        self._timer_job=self.root.after(1000, self.update_clock)
        self.progressbar.step(self._progressbar_increment)

    def start_timer(self):
        self._pomodoro_starttime=time.time()
        self._progressbar_increment=100 / self._pomodoro_time_limit
        self.progressbar['value']=-self._progressbar_increment
        self.update_clock()
    
    def get_formatted_time(self, time_to_format: int):
        return f'{time_to_format // 60}:{time_to_format % 60}'

if __name__ == "__main__":
    app=Clock()
    app.root.mainloop()
