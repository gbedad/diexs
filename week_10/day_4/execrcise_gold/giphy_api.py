import requests

API_KEY = 'hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My'
gif_type = 'hilarious'
rating = 'g'
width = 300

url = f"https://api.giphy.com/v1/gifs/search?q={gif_type}&rating={rating}&api_key={API_KEY}"

response = requests.get(url)

print(response.json())

print(len(response.json()["data"]))


# Exercise 3 Giphy API

def ask_giphy_type():
    user_input = input("Enter a term or phrase for gifs: ")
    new_url = f"https://api.giphy.com/v1/gifs/search?q={user_input}&rating={rating}&api_key={API_KEY}"
    resp = requests.get(new_url)
    if resp.json()["meta"]["status"] == 200:
        return resp.json()["data"]
    else:
        return "No gifs for this term"


my_data = ask_giphy_type()
print(my_data)