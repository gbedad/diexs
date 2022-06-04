import requests
from pyowm.owm import OWM
from datetime import datetime
from collections import defaultdict

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


API_key = '18d5eb550a23e362e0c91abf5052a8ed'

owm = OWM('18d5eb550a23e362e0c91abf5052a8ed')
mgr = owm.weather_manager()
forecaster = mgr.forecast_at_place('Paris,FR', '3h')
three_h_forecast = mgr.forecast_at_place('Tel Aviv,IL', '3h').forecast
print(forecaster.when_starts('iso'))
print(forecaster.when_ends('iso'))
for weather in three_h_forecast:
    print(weather.detailed_status)

reg = owm.city_id_registry()
print(reg.ids_for('Tel Aviv', 'IL', matching='exact')[0])

my_city_id = 2643743 #London
weather = mgr.weather_at_id(my_city_id).weather
print(weather)

three_h_forecaster = mgr.forecast_at_place('Berlin,DE', '3h')
print(three_h_forecaster.most_humid())
station_id = 39276
# station_id = 75114007

# Get tick historic data for a meteostation
# historian = mgr.station_tick_history(station_id, limit=4)  # only 4 data items

# Get hourly historic data for the same station, no limits


# Get hourly historic data for the same station, no limits
# historian = mgr.station_day_history(station_id)

# sunrise_unix = weather.sunrise_time()  # default unit: 'unix'
# sunrise_iso = weather.sunrise_time(timeformat='iso')
# sunrise_date = weather.sunrise_time(timeformat='date')
# sunrset_unix = weather.sunset_time()  # default unit: 'unix'
# sunrset_iso = weather.sunset_time(timeformat='iso')
# sunrset_date = weather.sunset_time(timeformat='date')


# city_name = 'Tel Aviv'
# country_code = 'IL'


root = tk.Tk()

city_name1 = tk.StringVar()
country_code1 = tk.StringVar()
city_name1.set('Paris')
country_code1.set('FR')


def login_clicked():
    city_name1.set(city_entry.get())
    country_code1.set(country_entry.get())


url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name1.get()},{country_code1.get()}&appid={API_key}'


# city
city_label = ttk.Label(root, text="City:")
city_label.pack(fill='x', expand=False)

city_entry = ttk.Entry(root, textvariable=city_name1)
city_entry.pack(fill='x', expand=False)
city_entry.focus()

# country
country_label = ttk.Label(root, text="Country Code:")
country_label.pack(fill='x', expand=False)

country_entry = ttk.Entry(root, textvariable=country_code1)
country_entry.pack(fill='x', expand=False)

# confirm city button
confirm_button = tk.Button(root, text="Enter", command= lambda: login_clicked())
confirm_button.pack(fill='x', expand=False, pady=10)


# def get_humidity_by_day(city, country):
#     response = requests.get(f'{url}?q={city},{country}&appid={API_key}')
#     print(response.json()["list"])
#     resp = response.json()["list"]
#     list_tuples = []
#     assert isinstance(resp, object)
#     for hum in resp:
#         list_tuples.append((hum['dt_txt'][5:10].replace('-', '/'), hum["main"]["humidity"]))
#     humidity_by_date = defaultdict(list)
#     for i in list_tuples:
#         humidity_by_date[i[0]] += [i[1]]
#     humidity_by_date = [(sum(v) / len(v), k) for k, v in humidity_by_date.items()]
#     return humidity_by_date
#
#
# datas = get_humidity_by_day(city=city_name1, country=country_code1)


# Sign in frame
# signin = ttk.Frame(root)
# signin.pack(padx=1, pady=1, fill='x', expand=True)



# def get_city():
#    city_name=entry.get()
#    Label(root, text=city_name, font= ('Century 15 bold')).pack()
#    country_code=entry.get()
#    Label(root, text=country_code, font= ('Century 15 bold')).pack(pady=5)
# #Create an Entry Widget
# entry= ttk.Entry(root,font=('Century 12'),width=40)
# entry.pack()
# button= tk.Button(root, text="Enter", command= get_city)
# button.pack()



def get_humidity_by_day():
    response = requests.get(url)
    print(response.json()["list"])
    resp = response.json()["list"]
    list_tuples = []
    assert isinstance(resp, object)
    for hum in resp:
        list_tuples.append((hum['dt_txt'][5:10].replace('-', '/'), hum["main"]["humidity"]))
    humidity_by_date = defaultdict(list)
    for i in list_tuples:
        humidity_by_date[i[0]] += [i[1]]
    humidity_by_date = [(sum(v) / len(v), k) for k, v in humidity_by_date.items()]
    return humidity_by_date


def create_values_for_plot(data):
    data_names = []
    data_values = []
    for i in range(len(data)):
        data_names.append(data[i][1])
        data_values.append(data[i][0])

    return data_names, data_values


datas = get_humidity_by_day()
names, values = create_values_for_plot(datas)
print(names)
print(values)


def plot_values():
    fig = Figure(figsize=(5, 5),
                 dpi=100)
    plot = fig.add_subplot(111)

    plot.bar(names, values)
    # plot.xlabel('Day')
    # plt.ylabel('Humidity %')
    plot.set_title(f'Humidity forecast in {city_name1.get()}')
    plot.set_ylabel('Humidity (%)')
    plot.set_xlabel('Day')
    # plt.suptitle(f'Humidity forecast in {city_name}')
    for i in range(len(names)):
        plot.text(i, values[i]//2, str(int(values[i]))+'%', ha='center', color='white')
    # plt.show()

    canvas = FigureCanvasTkAgg(fig,
                               master=root)
    canvas.draw()

    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas,
                                   root)
    toolbar.update()

    canvas.get_tk_widget().pack()

root.title('WEATHER APP')

root.geometry("800x800")

plot_button = tk.Button(master=root,
                     command=plot_values,
                     height=2,
                     width=10,
                     text="Plot")

plot_button.pack()


root.mainloop()





# out = defaultdict(list)
# for i in l:
#     out[i[1]] += [i[0]]
# out = [(sum(v)/len(v), k) for k, v in out.items()]
# print(out)


