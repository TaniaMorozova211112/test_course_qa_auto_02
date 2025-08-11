import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging

@pytest.fixture(scope='class')
def authenticated_session():
    session = requests.Session()
    # Зробити POST /auth для аутентифікації
    auth_url = "http://127.0.0.1:8080/auth"
    response = session.post(auth_url, auth=HTTPBasicAuth('test_user', 'test_pass'))
    response.raise_for_status()
    access_token = response.json().get('access_token')
    logging.info("Отримано токен та встановлено в сесію")
    # Додати токен в заголовки сесії
    session.headers.update({'Authorization': 'Bearer ' + access_token})
    yield session
    session.close()
    logging.info("Сесія закрита")

cars_db = {
    1: {"brand": "BMW", "year": 2018, "engine_volume": 2.0, "price": 50000},
    2: {"brand": "Audi", "year": 2020, "engine_volume": 1.8, "price": 45000},
    3: {"brand": "Mercedes", "year": 2019, "engine_volume": 2.5, "price": 55000},
    4: {"brand": "Toyota", "year": 2017, "engine_volume": 2.4, "price": 35000},
    5: {"brand": "Honda", "year": 2016, "engine_volume": 1.6, "price": 30000},
    6: {"brand": "Nissan", "year": 2021, "engine_volume": 1.5, "price": 40000},
    7: {"brand": "Ford", "year": 2015, "engine_volume": 2.2, "price": 32000},
    8: {"brand": "Chevrolet", "year": 2018, "engine_volume": 1.8, "price": 28000},
    9: {"brand": "Volkswagen", "year": 2019, "engine_volume": 2.0, "price": 33000},
    10: {"brand": "Hyundai", "year": 2020, "engine_volume": 1.6, "price": 29000},
    11: {"brand": "Kia", "year": 2019, "engine_volume": 2.0, "price": 31000},
    12: {"brand": "Subaru", "year": 2017, "engine_volume": 2.5, "price": 40000},
    13: {"brand": "Mazda", "year": 2018, "engine_volume": 2.0, "price": 32000},
    14: {"brand": "Lexus", "year": 2021, "engine_volume": 3.0, "price": 60000},
    15: {"brand": "Infiniti", "year": 2019, "engine_volume": 3.5, "price": 52000},
    16: {"brand": "Acura", "year": 2020, "engine_volume": 2.4, "price": 48000},
    17: {"brand": "Jeep", "year": 2018, "engine_volume": 3.6, "price": 45000},
    18: {"brand": "Land Rover", "year": 2020, "engine_volume": 2.0, "price": 55000},
    19: {"brand": "Volvo", "year": 2019, "engine_volume": 2.0, "price": 46000},
    20: {"brand": "Porsche", "year": 2021, "engine_volume": 3.0, "price": 70000},
    21: {"brand": "Tesla", "year": 2020, "engine_volume": 0.0, "price": 80000},
    22: {"brand": "Ferrari", "year": 2021, "engine_volume": 6.3, "price": 250000},
    23: {"brand": "Lamborghini", "year": 2020, "engine_volume": 6.5, "price": 300000},
    24: {"brand": "Bugatti", "year": 2019, "engine_volume": 8.0, "price": 350000},
    25: {"brand": "McLaren", "year": 2021, "engine_volume": 4.0, "price": 280000},
}

@pytest.mark.parametrize("sort_by, limit", [
    ("price", "3"),
    ("year", "5"),
    ("engine_volume", "2"),
    ("brand", "7"),
    (None, "4"),
    ("price", None),
    ("year", "1"),
])
def test_search_cars(authenticated_session, sort_by, limit):
    params = {}
    if sort_by:
        params['sort_by'] = sort_by
    if limit:
        params['limit'] = limit

    response = authenticated_session.get("http://127.0.0.1:8080/cars", params=params)
    assert response.status_code == 200

    data = response.json()

    # Отримуємо очікувані дані з cars_db
    expected_cars = sorted(
        cars_db.values(),
        key=lambda x: x.get(sort_by, x['brand']) if sort_by else x['brand']
    )
    if limit:
        expected_cars = expected_cars[:int(limit)]

    # Порівнюємо списки
    assert data == expected_cars