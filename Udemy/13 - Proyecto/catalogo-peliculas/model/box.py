from tkinter import messagebox 

def mensaje(mensaje):
    if mensaje[0] == 'i':
        messagebox.showinfo(mensaje[1], mensaje[2])
    elif mensaje[0] == 'e':
        messagebox.showerror(mensaje[1], mensaje[2])
    else:
        confirm = messagebox.askokcancel(mensaje[1], mensaje[2])
        return confirm