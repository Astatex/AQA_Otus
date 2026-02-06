import pytest
import requests


def test_get_all_list():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    assert response.status_code == 200
    data_json = response.json()
    assert data_json["status"] == "success"


@pytest.mark.parametrize("breed", ["bulldog", "husky", "poodle", "retriever"])
def test_random_image_by_breed(breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
    assert response.status_code == 200
    data_json = response.json()
    assert data_json["status"] == "success"


def test_multiple_random_images():
    response = requests.get("https://dog.ceo/api/breeds/image/random/3")
    assert response.status_code == 200
    data_json = response.json()
    assert data_json["status"] == "success"
    assert isinstance(data_json["message"], list)
    assert len(data_json["message"]) == 3


def test_image_url_is_accessible():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    image_url = response.json()["message"]
    img_resp = requests.head(image_url)
    assert img_resp.status_code == 200


@pytest.mark.parametrize("method", ["POST", "PUT", "PATCH", "DELETE"])
def test_only_get(method):
    response = requests.request(method, "https://dog.ceo/api/breeds/")
    assert response.status_code == 404 or 405
