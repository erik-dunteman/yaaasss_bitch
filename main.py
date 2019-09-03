try:
    import tkinter as tk
    from tkinter import *
except:
    import Tkinter as tk
    from Tkinter import *
import random


def generate():
    pronouns = ['Well shit,', 
            'Yas. Yaass.\nYAAAASSSSSS!',
            'Becky,',
            'Becky', 
            'Queeeeeen', 
            'Queen,', 
            'Suga,', 
            'Mammi,', 
            'Hun,',
            'Here yee, here yee:',
             'BITCH,', 
             'Girl,', 
             'DAMN!',
             'Yum!',
             'Queeeeeen,', 
             'Damn girl,',
            'Just so you know:', 
            'This.\nThis right here.',
            'YAAAAASSSSS!!']

    nouns = ['your face looks', 
            'your hair looks', 
            'your smile looks',
             'your eyes look', 
             'dat ass looks', 
             'your hair looks',
             'that booty looks',
            'EVERYTHING\nabout you looks', 
            'your personality looks', 
            'your smile looks', 
            'dem teeth look']

    adjectives = ['cute!', 
            'sexy', 
            'on point',
            'on fleek', 
            'perfect, just like you', 
            'straight fire',
            'amazing',
            'hella good',
            'tasty', 
            'smoking hot', 
            'like a party', 
            'fine.',
            'great with\nyour shoes',
            'savory',
            'juicy', 
            'better than before', 
            'thicker than a bowl\nof oatmeal']


    i = random.randint(0, len(pronouns)-1)
    j = random.randint(0,len(nouns)-1)
    k = random.randint(0, len(adjectives)-1)


    return ("{}\n{}\n{}".format(pronouns[i], nouns[j], adjectives[k]))



class App (object):
    def __init__(self):
        self.root=tk.Tk()
        self.root.overrideredirect(True)
        self.root.configure(background='black')
        self.root.geometry("{}x{}+{}+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight(), 0))
        self.variable=StringVar()
        self.i=0

        self.frame = Frame(self.root)
        self.frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        self.your_label=Label(self.frame,
            textvariable=self.variable, 
            fg = 'white', bg = 'black',
            text="Helvetica", 
            font=("Helvetica", 50))
    def grid(self):
        self.your_label.pack()
    def update_label(self):
        self.i=self.i+1

        choice = generate()

        self.variable.set(choice)
        self.root.after(3000,self.update_label)
    def run(self):
        self.grid()
        self.root.after(3000,self.update_label)
        self.root.mainloop()

if __name__=='__main__':
    App().run()


