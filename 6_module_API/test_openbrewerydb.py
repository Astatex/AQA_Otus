import pytest
import requests

import uuid


@pytest.mark.parametrize("per_page", [0, 200, 201])
def test_get(per_page):
    response = requests.get(
        f"https://api.openbrewerydb.org/v1/breweries?per_page={per_page}"
    )
    data = response.json()
    assert response.status_code == 200
    assert len(data) == per_page, f"Ожидалось {per_page} записей, получено {len(data)}"


def test_combined_filters():
    response = requests.get(
        "https://api.openbrewerydb.org/v1/breweries?by_state=New%20York&by_type=brewpub&per_page=5"
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 5
    for field in data:
        assert field["state_province"] == "New York"
        assert field["brewery_type"] == "brewpub"


def test_get_single_brewery():
    # ID из списка
    list_resp = requests.get("https://api.openbrewerydb.org/v1/breweries?per_page=1")
    brewery_id = list_resp.json()[0]["id"]
    print("--->", brewery_id)

    response = requests.get(f"https://api.openbrewerydb.org/v1/breweries/{brewery_id}")
    assert response.status_code == 200
    assert response.json()["id"] == brewery_id


def test_nonexistent_brewery():
    fake_id = str(uuid.uuid4())
    response = requests.get(f"https://api.openbrewerydb.org/v1/breweries/{fake_id}")
    assert response.status_code == 404


@pytest.mark.parametrize("method", ["POST", "PUT", "PATCH", "DELETE"])
def test_only_get(method):
    response = requests.request(method, "https://api.openbrewerydb.org/v1/breweries")
    assert response.status_code == 404 or 405
