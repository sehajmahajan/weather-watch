from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import database,login,home_if_login

class Register:
    themeColor = 'yellow'
    # userName = 'abhay'
    # passWord = 'singh'
    def __init__(self):
        self.root = Tk()
        self.root.geometry('800x800') # (width x height)
        self.root.title("Register Now")
        self.root.resizable(False,False)
        self.frame=Frame(self.root,bg='#333333')
        self.frame.place(x=0, y=0, height=800, width=800)

        # inserting image
        self.img1=Image.open('images\weather.png').resize((100,100)) #opening and resizing image
        self.image1=ImageTk.PhotoImage(self.img1)
        self.label=Label(self.frame, image=self.image1, bg='#333333')
        self.label.place(x=180, y=140, width=100,height=100)

        self.textLabel = Label(self.frame, text='Register Now', bg='#333333', fg= self.themeColor, font=('Arial',40), anchor="w")
        self.textLabel.place(x=290, y=160, height=70, width=500)
        
        # creating frame2
        self.frame2 = Frame(self.frame, bg='#333333', borderwidth = 2, relief = "groove")
        self.frame2.place(x=240, y=280, height= 450, width= 400)

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

        # text = email
        self.label3 = Label(self.frame, text='E-Mail',bg='#333333', fg= self.themeColor, font=('Arial',18,), anchor="w")
        self.label3.place(x=300, y=460, height=30, width=200)

        self.entry3 = Entry(self.frame, bg='#333333',fg ='white', borderwidth = 2, relief = "groove")
        self.entry3.place(x=300, y=490, height=30, width=300)

        # text = email
        self.label4 = Label(self.frame, text='Enter Your City',bg='#333333', fg= self.themeColor, font=('Arial',18,), anchor="w")
        self.label4.place(x=300, y=540, height=30, width=200)

        self.entry4 = Entry(self.frame, bg='#333333',fg ='white',borderwidth = 2, relief = "groove")
        self.entry4.place(x=300, y=570, height=30, width=300)

        # register button
        self.btn1=Button(self.frame,text = 'Register', bg= self.themeColor, fg='Black', font=('Arial',15), command = self.register)
        self.btn1.place(x=300, y=620, height= 40, width= 200)

        # login button
        self.btn2=Button(self.frame,text = "Already have an account?", bg='#333333', fg=self.themeColor, font=('Arial',12), borderwidth=0,command=self.login, relief="solid",anchor='w')
        self.btn2.place(x=300, y=660, height= 40, width= 220)

        
        self.root.mainloop()

    
    def register(self):
        if self.entry1.get() and self.entry2.get() and self.entry3.get() and self.entry4.get():
            res = database.addUser((self.entry1.get(), self.entry2.get(), self.entry4.get(),self.entry3.get()))
            if res:
                messagebox.showinfo('Success', 'User added successfully.')
                self.root.destroy()
                login.Login()
            else:
                messagebox.showwarning('Alert', 'Username already taken.')
        else:
            messagebox.showerror('Alert', 'Please enter the details')

    def login(self):
        self.root.destroy()
        login.Login()

        
   


        
if __name__ == '__main__':
    Register()