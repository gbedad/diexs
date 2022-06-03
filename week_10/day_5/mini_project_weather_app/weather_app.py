import requests
from datetime import datetime
from collections import defaultdict

import matplotlib.pyplot as plt


API_key = '18d5eb550a23e362e0c91abf5052a8ed'
from pyowm.owm import OWM
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
city_name = 'Paris'
country_code = 'FR'
url = 'https://api.openweathermap.org/data/2.5/forecast'


def get_humidity_by_day(city, country):
    response = requests.get(f'{url}?q={city},{country}&appid={API_key}')
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


my_list = get_humidity_by_day(city=city_name, country=country_code)

print(my_list)


def create_values_for_plot(data):
    names = []
    values = []
    for i in range(len(data)):
        names.append(data[i][1])
        values.append(data[i][0])

    return names, values


names, values = create_values_for_plot(my_list)
print(names)
print(values)


plt.bar(names, values)
plt.xlabel('Day')
plt.ylabel('Humidity %')
plt.suptitle(f'Humidity forecast in {city_name}')
for i in range(len(names)):
    plt.text(i, values[i]//2, str(int(values[i]))+'%', ha='center', color='white')
plt.show()





# out = defaultdict(list)
# for i in l:
#     out[i[1]] += [i[0]]
# out = [(sum(v)/len(v), k) for k, v in out.items()]
# print(out)


