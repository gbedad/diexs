from webapp import db
from webapp.models import Cryptocurrencies, User

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import schedule
import time


def set_crypto_in_db():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
    parameters = {
        'start': '1',
        'limit': '25',
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
        c = Cryptocurrencies.query.filter_by(id=currency["id"]).first()
        if c is None:
            zulu = Cryptocurrencies(id=currency["id"], name=currency["name"], symbol=currency["symbol"], slug=currency["slug"],
                                    first_historical_data=currency["first_historical_data"],
                                    last_historical_data=currency["last_historical_data"], is_active=currency["is_active"] )

            db.session.add(zulu)
        else:
            c.name = currency["name"]
            c.symbol = currency["symbol"]
            c.slug = currency["slug"]
            c.first_historical_data = currency["first_historical_data"]
            c.last_historical_data = currency["last_historical_data"]
    db.session.commit()


def add_logo():
    cryptos_in_db = Cryptocurrencies.query.all()
    url_metadata_v2 = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info'
    crypto_ids_list = []
    for crypto in cryptos_in_db:
        print(crypto.id)
        crypto_ids_list.append(str(crypto.id))
    s = ",".join(crypto_ids_list)
    print(s)
    parameter = {
        'id': s,
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '91f90390-6831-4e62-b62e-824b6d76ae02',
    }

    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url_metadata_v2, params=parameter)
        data = json.loads(response.text)["data"]
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    for value in data.values():
        c = Cryptocurrencies.query.filter_by(id=value['id']).first()
        print(c)
        c.logo = value['logo']

    db.session.commit()


schedule.every().day.at("00:00").do(set_crypto_in_db)
schedule.every().day.at("00:30").do(add_logo)

while True:
    schedule.run_pending()
    time.sleep(2)


