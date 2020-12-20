import tkinter as tk
import requests
import datetime as dt

HEIGHT = 500
WIDTH = 500

def format_response(weather):
    
    try:
       name = weather['name']
       desc = weather['weather'][0]['description']
       temp = weather['main']['temp']
       feel_like = weather['main']['feels_like']
       feels_likeC = int((feel_like-32)*5)/9
       tempC = int((temp-32)*5)/9
       date = dt.datetime.now()
       d1 = date.strftime('%A %d-%m-%Y ')

       final_str =  '\nCity: %s \nDate (TH): %s \nConditions: %s \nTemperature (°F): %s\nTemperature (°C): %i \nFeels like  (°C): %i ' % (name, d1, desc, temp, tempC, feels_likeC)
    except:
        final_str = '\nThere was a problem retrieving \nthat information '

    return final_str

  


def get_weather(city):
    weather_key = '0ed7e95aff3e7f50b057ea9c34aeac41'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather) 



root = tk.Tk()
root.title("Current Weather Data")
root.option_add("*Font", "consolas 15")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()



background_image = tk.PhotoImage(file='C://Users//User//Desktop//New folder (3)//Python//fall.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='light blue', bd=5)
frame.place(relx=0.5, rely=0.08, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, width='33')
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", bg='light gray', fg='black', activeforeground='red', width='20',font=('consolas', 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='light green', bd=5)
lower_frame.place(relx=0.5, rely=0.22, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, anchor='nw', justify='left', bd=10)
label.place(relwidth=1, relheight=1)

name_frame = tk.Frame(root, bg='light green', bd=5)
name_frame.place(relx=0.12, rely=0.86, relwidth=0.76, relheight=0.07)

name_label = tk.Label(name_frame, text="Made By: Tanabodee Yambangyang")
name_label.place(relwidth=1, relheight=1)




root.mainloop()