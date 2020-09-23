import tkinter as tk
from tkinter import ttk
import time


class Clock():
    def __init__(self):
        self.root = tk.Tk()
        self.style = ttk.Style()
        self.style.configure("BW.TLabel", font=(
            'Helvetica', 48),  foreground="red", background="white")
        self.label = ttk.Label(text="", style='BW.TLabel')
        self.label.pack()
        self._pomodoro_time_limit = 10
        self._pomodoro_starttime = time.time()
        self.start_button = ttk.Button(text='Start', command=self.start_timer)
        self.start_button.pack()
        self.progressbar = ttk.Progressbar()
        self.progressbar.pack()
        self.root.mainloop()

    def update_clock(self):
        now = int(time.time() - self._pomodoro_starttime)
        # Остановка таймера при достижении лимита времени
        if now > self._pomodoro_time_limit:
            self.root.after_cancel(self._timer_job)
            return
        
        self.label.configure(text='Прошло\n' + str(now) + ' секунд')
        # Запуск таймера
        self._timer_job = self.root.after(1000, self.update_clock)
        self.progressbar.step(self._progressbar_increment)
        

    def start_timer(self):
        self._pomodoro_starttime = time.time()
        self._progressbar_increment = 100 / self._pomodoro_time_limit 
        self.progressbar['value'] = -self._progressbar_increment
        self.update_clock()


app = Clock()
