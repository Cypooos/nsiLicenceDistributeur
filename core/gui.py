import tkinter as tk

class GUI:


    def __init__(self,licenceManager,debug=False):
        self.lm = licenceManager
        # cree window
        self.window = tk.Tk()

        self.reload()

        # test:
        if debug:
            print(
            "\n".join([x+":"+str(y) for x,y in self.lm.getStats(add_after=12).items() ])
                )

        self.window.mainloop()
    
    def reload(self):
        label = tk.Label(self.window, text="Hello World")
        label.pack()
