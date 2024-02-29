from tkinter import *
from tkinter import messagebox
import requests
import datetime
from PIL import Image, ImageTk
import login


class Home:
    API_KEY = "ce42a8b45d885f469ac82d490100d6a2"
    API_URL = "http://api.openweathermap.org/data/2.5/weather"
    FORECAST_API_URL = "http://api.openweathermap.org/data/2.5/forecast"

    
    

    def __init__(self):
        self.root = Tk()
        self.root.geometry('800x800')  # (width x height)
        self.root.title("Weather Watch")
        self.root.resizable(False, False)

        self.frame1 = Frame(self.root, bg='#333333')
        self.frame1.place(x=0, y=0, height=800, width=800)

        self.frame2 = Frame(self.root, bg='#292929')
        self.frame2.place(x=0, y=0, height=200, width=800)

        self.frame3 = Frame(self.root, bg='#2e2e2e')
        self.frame3.place(x=480, y=260, height=240, width=290)

        self.logo1 = Image.open("images\weather.png").resize((120, 120))
        self.logoImage = ImageTk.PhotoImage(self.logo1)
        self.label = Label(self.root, image=self.logoImage, bg='#292929')
        self.label.place(x=60, y=40, width=120, height=120)

        self.textLabel = Label(self.frame2, text='Weather Watch', bg='#292929', fg='yellow', font=('Arial', 60),
                               anchor="w")
        self.textLabel.place(x=200, y=60, height=75, width=570)

        self.city_label = Label(self.root, text='Enter city here: ', bg='#2e2e2e', fg='yellow', font=('Arial', 17))
        self.city_label.place(x=510, y=315, height=30, width=230)

        self.city_entry = Entry(self.root, fg='white', bg='#2e2e2e', font=(10), borderwidth=2, relief="groove")
        self.city_entry.place(x=510, y=350, height=30, width=230)

        self.weather_label_text = Label(self.frame1, text="Weather", bg='#333333', fg='yellow', font=('Arial', 20),
                                        anchor='w')
        self.weather_label_text.place(x=90, y=280, height=40, width=130)

        self.weather_label = Label(self.frame1, text="", font=('Arial', 18), bg='#333333', fg='white', anchor='w')
        self.weather_label.place(x=280, y=280, height=40, width=180)

        self.temperature_label_text = Label(self.frame1, text="Temperature", bg='#333333', fg='yellow',
                                            font=('Arial', 20), anchor='w')
        self.temperature_label_text.place(x=90, y=350, height=40, width=180)

        self.temperature_label = Label(self.frame1, text="", font=('Arial', 18), bg='#333333', fg='white', anchor='w')
        self.temperature_label.place(x=280, y=350, height=40, width=150)

        self.humidity_label_text = Label(self.frame1, text="Humidity", bg='#333333', fg='yellow', font=('Arial', 20),
                                         anchor='w')
        self.humidity_label_text.place(x=90, y=420, height=40, width=150)

        self.humidity_label = Label(self.frame1, text="", font=('Arial', 18), bg='#333333', fg='white', anchor='w')
        self.humidity_label.place(x=280, y=420, height=40, width=150)

        self.get_weather_button = Button(self.root, text="Get Weather", bg='yellow', fg='Black', font=('Arial', 15),
                                         command=self.get_weather)
        self.get_weather_button.place(x=510, y=400, height=30, width=230)

        self.login_button = Button(self.root, text="Login (access all features)", bg='#2e2e2e', fg='yellow',borderwidth = 0, font=('Arial', 15),
                                         command=self.direct_login)
        self.login_button.place(x=500, y=450, height=30, width=250)
       

       # popup for login
        def show_login_popup():
            response = messagebox.askyesno("Login", "Do you want to log in?")
            if response:
                # Add your login logic here (e.g., open a login window)
                self.root.destroy()
                login.Login()
            else:
                # Add any action you want to perform if the user chooses not to log in
                print("User chose not to log in.") 

        # After 10 seconds, show the login popup
        self.root.after(10000, show_login_popup)

        self.root.mainloop()



        # function for login
    def direct_login(self):
        self.root.destroy()
        login.Login()
   

    def get_weather(self):
        city = self.city_entry.get()
        if not city:
            self.weather_label.config(text="Please enter a city.")
            return

        weather_params = {
            "q": city,
            "appid": self.API_KEY,
            "units": "metric"
        }

        forecast_params = {
            "q": city,
            "appid": self.API_KEY,
            "units": "metric",
            "cnt": 32,  # Get data for the next 4 daysdemo
        }

        try:
            response = requests.get(self.API_URL, params=weather_params)
            weather_data = response.json()

            forecast_response = requests.get(self.FORECAST_API_URL, params=forecast_params)
            forecast_data = forecast_response.json()
            # print(forecast_data) #getting date
            if str(forecast_data['list'][0]['dt_txt'])[:10]=='2023-07-27':
                print('this is date 27')

            if weather_data["cod"] == 200 and forecast_data.get("list"):
                weather_info = weather_data['weather'][0]['description']
                temperature_info = f"{weather_data['main']['temp']} °C"
                humidity_info = f"{weather_data['main']['humidity']} %"

                self.weather_label.config(text=weather_info)
                self.temperature_label.config(text=temperature_info)
                self.humidity_label.config(text=humidity_info)


                

                
              
            else:
                self.weather_label.config(text=f"Error: Unable to fetch weather data for {city}.")
        except requests.exceptions.RequestException:
            self.weather_label.config(text="Error: Connection Error")

if __name__ == '__main__':
    Home()
