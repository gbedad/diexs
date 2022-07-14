from webapp import db
from webapp.models import Cryptocurrencies, User

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
parameters = {
    'start': '1',
    'limit': '20',
    'sort': 'cmc_rank'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '91f90390-6831-4e62-b62e-824b6d76ae02',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    all_currencies = data["data"]
    print(all_currencies)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


for currency in all_currencies:
    zulu = Cryptocurrencies(id=currency["id"], name=currency["name"], symbol=currency["symbol"], slug=currency["slug"],
                            first_historical_data=currency["first_historical_data"],
                            last_historical_data=currency["last_historical_data"], is_active=currency["is_active"] )
    db.session.add(zulu)
db.session.commit()
