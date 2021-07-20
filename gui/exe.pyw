from tkinter import *
from subprocess import Popen
import sys
import psutil

try:
    path = f'{sys._MEIPASS}\\'
except:
    path = __file__[:len(__file__)-len(__file__.split('\\')[len(__file__.split('\\'))-1])]
with Popen(f'{path}\\fil\\taraskevizatar.exe') as proc:
    window = Tk()
    window.title('Taraskevizatar')
    label = Label(window, text='Скрипт работает.\nИспользуйте кнопку Home, чтобы начать фиксировать ввод\n и End для того, чтобы перевести текст на латинку.', padx=5, pady=5)
    label.grid(column=0, row=0)
    def close():
        proc.terminate()
        window.destroy()
        for proc1 in psutil.process_iter():
            if proc1.name() == "taraskevizatar.exe":
                proc1.kill()
        exit()
    button = Button(window, text="Остановить", command=close)
    window.protocol("WM_DELETE_WINDOW", close)
    button.grid(column=0, row=1)
    window.mainloop()