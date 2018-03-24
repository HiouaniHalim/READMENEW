from Tkinter import *
import ttk
import PROJECT__1


def NEW():
    """"""
    VALUE = float(ENTRY_A.get())

    # VALUE = float(ENTRY_A.get())
    if type(VALUE) == float:
        APP = PROJECT__1.TRANSFORM(KILOGRAM=VALUE)
        LISTBOX.insert(0, APP.__mul__())


def Gram():

    GRAM = float(ENTRY_B.get())

    if type(GRAM) == float:
        APP = PROJECT__1.TRANSFORM(KILOGRAM=GRAM)
        LISTBOX.insert(0, APP.__pow__())


def DELET():
    LISTBOX.delete(0, END)


ROOT = Tk()
ROOT.geometry('400x400+500+100')
ROOT.title('__TRANSFORM__')
ROOT.resizable(0, 0)

BUTTON_1 = ttk.Button(ROOT, text='RESET', width=7, command=DELET)
BUTTON_1.place(y=280)
BUTTON_2 = ttk.Button(ROOT, text='EXIT', width=7, command=ROOT.destroy)
BUTTON_2.place(x=330, y=365)

# BECAUSE FRAME A
FRAME_A = Frame(ROOT, height=150, width=400)
FRAME_A.pack()

LISTBOX = Listbox(FRAME_A, width=50, height=5, bg='grey')
LISTBOX.pack(pady=20)

# BECAUSE FRAME B
FRAME_B = Frame(ROOT, height=100, width=400)
FRAME_B.pack()

LABEL_A = ttk.Label(FRAME_B, text='KG :')
LABEL_A.place(x=30, y=60)

ENTRY_A = ttk.Entry(FRAME_B, width=10)
ENTRY_A.bind('<Return>', NEW)
ENTRY_A.place(x=65, y=59)

LABEL_B = ttk.Label(FRAME_B, text='G :')
ENTRY_A.bind('<Return>', Gram)
LABEL_B.place(x=250, y=60)

ENTRY_B = ttk.Entry(FRAME_B, width=10)
ENTRY_B.place(x=280, y=59)

# BECAUSE FRAME C
FRAME_C = Frame(ROOT, height=50, width=400)
FRAME_C.pack()

BUTTON_A = ttk.Button(FRAME_C, text='VALUE', command=NEW, width=7)
BUTTON_A.place(x=70)
BUTTON_B = ttk.Button(FRAME_C, text='VALUE', command=Gram, width=7)
BUTTON_B.place(x=285)
ROOT.mainloop()