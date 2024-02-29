from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import database, register, home_if_login

class Login:
    themeColor = 'yellow'
    # userName = 'abhay'
    # passWord = 'singh'
    def __init__(self):
        self.root = Tk()
        self.root.geometry('800x800') # (width x height)
        self.root.title("Weather Watch")
        self.root.resizable(False,False)
        self.frame=Frame(self.root,bg='#333333')
        self.frame.place(x=0, y=0, height=800, width=800)

        # inserting image
        self.img1=Image.open('images\weather.png').resize((100,100)) #opening and resizing image
        self.image1=ImageTk.PhotoImage(self.img1)
        self.label=Label(self.frame, image=self.image1, bg='#333333')
        self.label.place(x=180, y=140, width=100,height=100)

        self.textLabel = Label(self.frame, text='Weather Watch', bg='#333333', fg= self.themeColor, font=('Arial',40), anchor="w")
        self.textLabel.place(x=290, y=170, height=50, width=500)
        
        # creating frame2
        self.frame2 = Frame(self.frame, bg='#333333', borderwidth = 2, relief = "groove")
        self.frame2.place(x=240, y=280, height= 300, width= 400)

        # text = username
        self.label1 = Label(self.frame, text='Username',bg='#333333', fg= self.themeColor, font=('Arial',18), anchor="w")
        self.label1.place(x=300, y=300, height=30, width=200)

        self.entry1 = Entry(self.frame,bg='#333333',fg='white', borderwidth = 2, relief = "groove")
        self.entry1.place(x=300, y=330, height=30, width=300)

        # text = password
        self.label2 = Label(self.frame, text='Password',bg='#333333', fg= self.themeColor, font=('Arial',18,), anchor="w")
        self.label2.place(x=300, y=380, height=30, width=200)

        self.entry2 = Entry(self.frame, bg='#333333',fg ='white',show="*", borderwidth = 2, relief = "groove")
        self.entry2.place(x=300, y=410, height=30, width=300)

        # login button
        self.btn1=Button(self.frame,text = 'Login', bg= self.themeColor, fg='Black', font=('Arial',15), command = self.login)
        self.btn1.place(x=300, y=480, height= 40, width= 200)

        # Register button
        self.btn2=Button(self.frame,text = "Don't have any account?", bg='#333333', fg=self.themeColor, font=('Arial',12), borderwidth=0, relief="solid",anchor='w',command=self.register)
        self.btn2.place(x=300, y=520, height= 40, width= 220)

        
        self.root.mainloop()

    # method to get data from two entries
    def login(self):
        print('button is clicked')
        if self.entry1.get() and self.entry2.get():
            print('data is given')
            res = database.loginUser((self.entry1.get(), self.entry2.get()))
            if res:
                messagebox.showinfo('Success', 'Login is successful.')
                self.root.destroy()
                home_if_login.Home2(res)
            else:
                messagebox.showerror('Alert', 'Invalid username/password.')
        else:
            print('enter details')
            messagebox.showerror('Alert', 'Please your details.')

    def register(self):
        self.root.destroy()
        register.Register()

if __name__ == '__main__':
    Login()