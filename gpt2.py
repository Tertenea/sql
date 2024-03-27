import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import sqlite3

def on_frame_configure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_mousewheel(event, canvas):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

def create_frame(root):
    canvas = tk.Canvas(root)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    canvas.bind_all("<MouseWheel>", lambda event, canvas=canvas: on_mousewheel(event, canvas))

    frame.bind("<Configure>", lambda event, canvas=canvas: on_frame_configure(canvas))

    return frame

def main():
    root = tk.Tk()
    root.title("Hehehehehehehe")

    style = Style(theme='darkly')
    style.configure('TButton', font=('Helvetica', 11))

    frame = create_frame(root)

    db = sqlite3.connect('epood_pkiviorg.db')
    qry = db.execute('SELECT * FROM pkiviorg')
    data = qry.fetchall()
    i = 0
    fields = ['ID', 'first_name', 'last_name', 'email', 'car_make', 'car_model', 'car_year', 'car_price']
    for field in fields:
        ttk.Label(frame, text=field).grid(column=i, row=0)
        i += 1

    for row in data:
        i += 1
        for j in range(len(row)):
            ttk.Label(frame, text=row[j]).grid(column=j, row=i)


    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.BOTTOM)

    ttk.Button(button_frame, text="Button 1").pack(side=tk.LEFT)
    ttk.Button(button_frame, text="Button 2").pack(side=tk.LEFT)
    ttk.Button(button_frame, text="Button 3").pack(side=tk.LEFT)

    root.mainloop()

if __name__ == "__main__":
    main()
