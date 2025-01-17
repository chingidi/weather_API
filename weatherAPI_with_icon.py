import tkinter as tk
import requests
from PIL import Image, ImageTk


app = tk.Tk()
app.title("Weather_API")

C = tk.Canvas(app, height=500, width=600)
background_image= tk.PhotoImage(file='./landscape.png')
background_label = tk.Label(app, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()


frame = tk.Frame(app,  bg='#42c2f4', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

textbox = tk.Entry(frame, font=40)
textbox.place(relwidth=0.65, relheight=1)

submit = tk.Button(frame, text='Get Weather', font=40, command=lambda: get_weather())
submit.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(app, bg='#42c2f4', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

results = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)

results.config(font=40, bg='white')
results.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(results, bg='white', bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

def open_image(icon):

    size = int(lower_frame.winfo_height()*0.20)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img

def get_weather():

    city=textbox.get()      
    weather_key = 'edffd1bf975a74d5d10e58c5ac8be2d3'
    
    
    url = 'https://api.openweathermap.org/data/2.5/weather'

    params = {'APPID': 'edffd1bf975a74d5d10e58c5ac8be2d3', 'q': city}

    response = requests.get(url, params=params)
    print(response.json())
    weather_json = response.json()
    results['text'] = format_response(response.json())
    icon_name = weather_json['weather'][0]['icon']
    open_image(icon_name)


def format_response(weather_json):

    try:
        city = weather_json['name']
        conditions = weather_json['weather'][0]['description']
        temp = weather_json['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (city, conditions, temp)
        
    except:
        final_str = 'City Not Found'
    return final_str








#closing the window
app.mainloop()
