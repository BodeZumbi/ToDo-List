from tkinter import *
from tkinter import messagebox, Button


def new_task():
    task = myentry.get()
    if task != "":
        listTheBox.insert(END, task)
        myentry.delete(0, 'END')
    else:
        messagebox.showwarning("ERRO", "Por favor, insira uma task.")


def delete_task():
    listTheBox.delete(ANCHOR)


ws = Tk()
ws.geometry('500x450+500+200')
ws.title('A fazer')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

listTheBox = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle='none',
)

listTheBox.pack(side=LEFT, fill=BOTH)
task_list = [
    'placeholder1',
    'placeholder2',
    'placeholder3',
    'placeholder4',

]

for item in task_list:
    listTheBox.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

listTheBox.config(yscrollcommand=sb.set)
sb.config(command=listTheBox.yview)

myentry = Entry(
    ws,
    font=('times', 24)
)

myentry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add task',
    font='times 14',
    bg='#c5f776',
    padx=20,
    pady=10,
    command=new_task)

addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

deltask_btn: Button = Button(
    button_frame,
    text='Delete task',
    font='times14',
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=delete_task
)
deltask_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()
