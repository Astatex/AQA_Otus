import pytest
import requests


@pytest.mark.parametrize(
    "breed",
    [
        "bulldog",
        "hound",
        "mastiff",
        "poodle",
        "retriever",
        "sheepdog",
        "spaniel",
        "terrier",
    ],
)
def test_get_all_list(breed):
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    assert response.status_code == 200

    data_json = response.json()
    list_breed = data_json["message"]
    assert data_json["status"] == "success"
    assert isinstance(list_breed, dict)
    assert breed in list_breed, f"Порода '{breed}' отсутствует в списке"

    subbreeds = list_breed[breed]
    assert isinstance(subbreeds, list)
    assert len(subbreeds) > 0, f"У породы '{breed}' нет под пород"


@pytest.mark.parametrize(
    "breed",
    [
        "bulldog",
        "hound",
        "mastiff",
        "poodle",
        "retriever",
        "sheepdog",
        "spaniel",
        "terrier",
    ],
)
def test_random_image_by_breed(breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
    assert response.status_code == 200

    data_json = response.json()
    assert data_json["status"] == "success"
    assert data_json["message"].endswith((".jpg", ".jpeg", ".png"))


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
    assert response.status_code in (404, 405)
