def test_addoption(base_url, status_code):
    assert status_code == 200


# pytest test_custom_url_status.py --url=https://ya.ru/ --status_code=200
# pytest test_custom_url_status.py --url=https://ya.ru/sfhfh  --status_code=404
