# test_cars_api.py
import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

# ---------- logging ----------
logger = logging.getLogger("test_cars_api")
logger.setLevel(logging.INFO)
fmt = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

fh = logging.FileHandler("test_search.log", mode="w", encoding="utf-8")
fh.setFormatter(fmt)
logger.addHandler(fh)

ch = logging.StreamHandler()
ch.setFormatter(fmt)
logger.addHandler(ch)
# -----------------------------

BASE_URL = "http://127.0.0.1:8080"


@pytest.fixture(scope="class")
def auth_session():
    """
    Логін один раз на клас тестів — повертає готову requests.Session із заголовком Authorization.
    """
    session = requests.Session()
    auth_url = f"{BASE_URL}/auth"

    resp = session.post(auth_url, auth=HTTPBasicAuth("test_user", "test_pass"))
    resp.raise_for_status()

    token = resp.json().get("access_token")
    assert token, "Не отримано access_token"

    session.headers.update({"Authorization": f"Bearer {token}"})
    logger.info("Отримано токен та встановлено в сесію")
    yield session

    session.close()
    logger.info("Сесія закрита")


@pytest.mark.parametrize(
    "sort_by, limit",
    [
        ("price", 3),
        ("year", 5),
        ("engine_volume", 2),
        ("brand", 7),
        (None, 4),
        ("price", None),
        ("year", 1),
    ],
)
def test_search_cars(auth_session, sort_by, limit, request):
    """
    Параметризований тест: робимо GET /cars?sort_by=...&limit=...
    Логуємо в консоль і файл test_search.log.
    """
    params = {}
    if sort_by is not None:
        params["sort_by"] = sort_by
    if limit is not None:
        params["limit"] = str(limit)

    logger.info("Тест %s — params=%s", request.node.name, params)

    try:
        r = auth_session.get(f"{BASE_URL}/cars", params=params, timeout=5)
    except requests.RequestException as e:
        logger.exception("HTTP error: %s", e)
        pytest.fail(f"HTTP request failed: {e}")

    logger.info("Status: %s", r.status_code)
    assert r.status_code == 200, f"Unexpected status: {r.status_code} / {r.text}"

    data = r.json()
    logger.info("Отримано %d записів", len(data))
    logger.debug("Response body: %s", data)

    assert isinstance(data, list), "Response should be a list"

    if limit is not None:
        assert len(data) <= int(limit), f"Returned more records than limit={limit}"

    # Перевірка сортування (як на сервері — якщо sort_by відсутній, сортування за 'brand')
    if len(data) > 1:
        if sort_by:
            keys = [item.get(sort_by, 0) for item in data]
        else:
            keys = [item.get("brand", "") for item in data]

        assert keys == sorted(keys), f"Data not sorted by {sort_by or 'brand'}"