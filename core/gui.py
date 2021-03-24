import tkinter as tk

class GUI:


    def __init__(self,licenceManager,debug=False):
        self.lm = licenceManager
        # cree window
        self.window = tk.Tk()

        self.reload()

        # test:
        if debug:
            print(self.lm.getStats())

        self.window.mainloop()
    
    def reload(self):
        label = tk.Label(self.window, text="Hello World")
        label.pack()
