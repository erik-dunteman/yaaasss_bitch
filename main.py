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
             'your quarantine\nsuit looks',
            'EVERYTHING\nabout you looks', 
            'your personality\nlooks', 
            'your smile looks', 
            'dem teeth look',
            'your coronavirus\nlooks',
            'that virus looks',
            'your coronavirus\nlooks',
            'your coronavirus\nlooks',]

    adjectives = ['like it\nhas Covid-19', 
            'sexy',
            'diseased',
            'hopeless',
            'like you\nhave coronavirus',
            'pretty viral\ntbh',
            'like you should\ngo to a hospital', 
            'on point',
            'on fleek', 
            'perfect,\njust like you', 
            'straight fire',
            'amazing',
            'hella good',
            'tasty', 
            'smoking hot',
            'feverish.',
            'like you should\nget tested 4 covid' ,
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

    others = ['THE WORLD\nIS BURNING', 'THERE IS\nNO ESCAPE', "FUCK"]
    main = "{}\n{}\n{}".format(pronouns[i], nouns[j], adjectives[k])
    others.append(main)
    others.append(main)
    others.append(main)
    i = random.randint(0,len(others)-1)
    return (others[i])



class App (object):
    def __init__(self):
        self.root=tk.Tk()
        self.root.overrideredirect(True)
        # self.root.attributes('-fullscreen', True)
        # self.root.wm_attributes('-type', 'splash')
        self.root.configure(background='black')
        self.root.geometry("{}x{}+{}+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight(), 0))
        self.root.bind("<Any-KeyPress>", self.exit)

        self.variable=StringVar()
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
        choice = generate()
        self.variable.set(choice)
        self.root.after(120000,self.update_label)
    def run(self):
        self.grid()
        self.root.after(1,self.update_label)
        self.root.mainloop()
    def exit(self, event):
        self.root.destroy()

if __name__=='__main__':
    App().run()


