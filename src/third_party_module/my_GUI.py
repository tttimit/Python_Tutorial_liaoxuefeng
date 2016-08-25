from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # self.helloLabel = Label(self, text='Hello, world!')
        # self.helloLabel.pack()
        # self.quiteButton = Button(self, text='Quit', command=self.quit)
        # self.quiteButton.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)


app = Application()

app.master.title('Hello World!')

app.mainloop()

# 如果GUI比较复杂，还是建议使用系统原生支持的语言来写
