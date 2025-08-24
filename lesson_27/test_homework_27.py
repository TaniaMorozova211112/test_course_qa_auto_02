import pytest
from novaposhta_tracking_page import NovaPoshtaTrackingPage


@pytest.mark.parametrize(
    "tracking_number, expected_status",
    [
        ("20400470952152", "Відправлення отримано. Грошовий переказ видано одержувачу."),
    ]
)
def test_tracking_status(driver, tracking_number, expected_status):
    page = NovaPoshtaTrackingPage(driver)
    page.open()
    page.enter_tracking_number(tracking_number)
    status = page.get_tracking_status()

    print(f"\nЗнайдений статус: {status}")  # для дебага
    assert status == expected_status, f"Очікувано: {expected_status}, отримано: {status}"
