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
#pack() method:It organizes the widgets in blocks before placing in the parent widget

frame = tk.Frame(app,  bg='#42c2f4', bd=5)

#place() method:It organizes the widgets by placing them on specific positions directed by the programmer.
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

textbox = tk.Entry(frame, font=40)
textbox.place(relwidth=0.65, relheight=1)

submit = tk.Button(frame, text='Get Weather', font=40, command=lambda: get_weather())
submit.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(app, bg='#42c2f4', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
#bg_color = 'white'

'''Label: It refers to the display box where you can put any text or
image which can be updated any time as per the code'''
results = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)

#configer the results Label
# configuration of the widgets which can organize the widgets in the parent windows.
results.config(font=40, bg='white')
results.place(relwidth=1, relheight=1)

#Canvas: It is used to draw pictures and other complex layout like graphics, text and widgets
weather_icon = tk.Canvas(results, bg='white', bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

#creating a function for getting the img file TKinter
def open_image(icon):

    size = int(lower_frame.winfo_height()*0.20)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img


#creating a method for getting weather of entered city
def get_weather():

    city=textbox.get()      
    weather_key = 'edffd1bf975a74d5d10e58c5ac8be2d3'
    
    #this is the URL for openweathermap API
    
    url = 'https://api.openweathermap.org/data/2.5/weather'

    params = {'APPID': 'edffd1bf975a74d5d10e58c5ac8be2d3', 'q': city}

    '''getting the detailes , using the requests method (using get method (it output = 200,201) )
    GET is nothing but method ,is used to retrieve information from the given server.
'''
    response = requests.get(url, params=params)
    print(response.json())
    weather_json = response.json()
    results['text'] = format_response(response.json())
    icon_name = weather_json['weather'][0]['icon']
    open_image(icon_name)


def format_response(weather_json):

    #there is using try(The try block lets you test a block of code for errors.)
    try:
        city = weather_json['name']
        conditions = weather_json['weather'][0]['description']
        temp = weather_json['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (city, conditions, temp)
    
    #The except block lets you handle the error.
    except:
        final_str = 'City Not Found'
    return final_str








#closing the window
app.mainloop()
