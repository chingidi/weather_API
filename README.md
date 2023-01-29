# weather_API
Weather_API using Tkinter,JSON,Requests method and PIL library
#importing a TKinter(The tkinter package (“Tk interface”) is the standard Python interface to the Tcl/Tk GUI toolkit.)

import tkinter as tk


'''importing a HTTP requests module(The requests module allows you to send HTTP requests using Python.
The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).)'''

import requests


'''importing a PIL library(Python Imaging Library (expansion of PIL) is the de facto image processing package for Python language.
It incorporates lightweight image processing tools that aids in editing, creating and saving images)'''

from PIL import Image, ImageTk

#creating a tk window (there app is window name)
#if once we create or open one window you must close the window by using (window_name.mainloop())

app = tk.Tk()
app.title("Weather_API")



#Canvas: It is used to draw pictures and other complex layout like graphics, text and widgets
#and align that
C = tk.Canvas(app, height=500, width=600)

#giving the bg image from TKinter PIL library
background_image= tk.PhotoImage(file='./landscape.png')

'''Label: It refers to the display box where you can put any text or
image which can be updated any time as per the code'''
background_label = tk.Label(app, image=background_image)

#place() method:It organizes the widgets by placing them on specific positions directed by the programmer.
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#pack() method:It organizes the widgets in blocks before placing in the parent widget

C.pack()

#creating a main frame in window and align the frame and giving the bg color and border
#Frame: It acts as a container to hold the widgets.
frame = tk.Frame(app,  bg='#42c2f4', bd=5)

#place() method:It organizes the widgets by placing them on specific positions directed by the programmer.
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
#frame_window = C.create_window(100, 40, window=frame)

#creating the entry wizard(It is used to input the single line text entry from the user)
#and font size the textbox
textbox = tk.Entry(frame, font=40)

#place() method:It organizes the widgets by placing them on specific positions directed by the programmer.
textbox.place(relwidth=0.65, relheight=1)

def focus0(event):
    submit.focus_set()
#creating the submit button and align (for calling function and print the details)

submit = tk.Button(frame, text='Get Weather', font=40, command=lambda: get_weather())
textbox.bind("<Return>",focus0)
#submit.config(font=)

#place() method:It organizes the widgets by placing them on specific positions directed by the programmer.
submit.place(relx=0.7, relheight=1, relwidth=0.3)

#creating the another frame for displaying fatched data
#and align the frame and giving bg color and border
lower_frame = tk.Frame(app, bg='#42c2f4', bd=10)

#place() method:It organizes the widgets by placing them on specific positions directed by the programmer.
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

#declare the bg color for using label
bg_color = 'white'

#creating a label
'''Label: It refers to the display box where you can put any text or
image which can be updated any time as per the code'''
results = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)

#configer the results Label
# configuration of the widgets which can organize the widgets in the parent windows.
results.config(font=40, bg=bg_color)

#place() method:It organizes the widgets by placing them on specific positions directed by the programmer.
results.place(relwidth=1, relheight=1)

#Canvas: It is used to draw pictures and other complex layout like graphics, text and widgets
#and styling and align the weather icon
#and display the result and bg color and thickness for icon space
weather_icon = tk.Canvas(results, bg=bg_color, bd=0, highlightthickness=0)

#place() method:It organizes the widgets by placing them on specific positions directed by the programmer.
#and align the icon
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

#creating a function for getting the img file TKinter
def open_image(icon):

    #creating a vriable for  displaying size
    size = int(lower_frame.winfo_height()*0.20)

    #creating a variable for getting a png from library and resize the 
    #the png files must be save in same folder
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    #weather_icon.delete("all")

    #declaring the space for img(whare it display)
    weather_icon.create_image(0,0, anchor='nw', image=img)

    #assign the variable for getting weather icon
    weather_icon.image = img


#creating a method for getting weather of entered city
def get_weather():

    city=textbox.get()      

    '''weather_key is nothing but the opensource api key it getting from the
     openweathermap.org ,it nothing but the opensource weather API
     once we login it will provide the key
    '''
    weather_key = 'edffd1bf975a74d5d10e58c5ac8be2d3'
    
    #this is the URL for openweathermap API
    
    url = 'https://api.openweathermap.org/data/2.5/weather'

    #creating a dic for for storing the entered city weather detailes
    params = {'APPID': 'edffd1bf975a74d5d10e58c5ac8be2d3', 'q': city, 'units':'imperial'}

    '''getting the detailes , using the requests method (using get method (it output = 200,201) )
    GET is nothing but method ,is used to retrieve information from the given server using a given URI
    URI (Uniform Resource Identifier) URI provides a technique for defining the identity of an item
    '''
    response = requests.get(url, params=params)

    #printing the got data for our prpse
    
    print(response.json())

    #creat and declare the variable for format_response function
    '''creating a function and JSON object or method
       (response.json() returns a JSON object of the result (if the result was written in JSON format, if not it raises an error).
       Python requests are generally used to fetch the content from a particular resource URI.)
       It is one of the most used methods in the requests module.'''
    weather_json = response.json()

    #this line for display results in lower fram
    #without this line don't display the results it means detailes
    results['text'] = format_response(response.json())
    
    #getting the icon code from json detailes 
    icon_name = weather_json['weather'][0]['icon']
 
    #and calling the img from file folder using the open_image function
    open_image(icon_name)


def format_response(weather_json):

    #there is using try(The try block lets you test a block of code for errors.)
    try:

        #getting the detailes from JSON method to weather_json(argument )
        #from get_weather function
        city = weather_json['name']
        conditions = weather_json['weather'][0]['description']
        temp = weather_json['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (city, conditions, temp)
    
    #The except block lets you handle the error.
    except:
        final_str = 'City Not Found'
    #final_str = 'hello'
    return final_str








#closing the window
app.mainloop()
