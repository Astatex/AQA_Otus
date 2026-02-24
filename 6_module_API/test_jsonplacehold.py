import pytest
import requests

from faker import Faker
import random

fake = Faker()


def test_get():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = response.json()
    assert response.status_code == 200
    assert [item["id"] for item in data] == list(range(1, 101))


@pytest.mark.parametrize(
    "title, body, user_id",
    [
        (fake.sentence(), fake.text(max_nb_chars=2001), random.randint(1, 100)),
        (fake.sentence(), fake.text(max_nb_chars=201), random.randint(1, 100)),
        (fake.sentence(), fake.text(max_nb_chars=21), random.randint(1, 100)),
    ],
)
def test_post(title, body, user_id):
    body_json = {"title": title, "body": body, "userId": user_id}
    headers = {"Content-type": "application/json"}

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts", json=body_json, headers=headers
    )

    assert response.status_code == 201  # для
    json_data = response.json()
    print(json_data)
    assert json_data["title"] == title
    assert json_data["body"] == body
    assert json_data["userId"] == user_id


@pytest.mark.parametrize(
    "id, title, body, user_id",
    [
        (
            random.randint(10, 89),
            fake.sentence(),
            fake.text(max_nb_chars=201),
            random.randint(1, 100),
        ),
        (
            random.randint(10, 89),
            fake.sentence(),
            fake.text(max_nb_chars=150),
            random.randint(1, 100),
        ),
        (
            random.randint(10, 89),
            fake.sentence(),
            fake.text(max_nb_chars=10),
            random.randint(1, 100),
        ),
    ],
)
def test_put(id, title, body, user_id):
    body_json = {"id": id, "title": title, "body": body, "userId": user_id}
    headers = {"Content-type": "application/json"}

    response = requests.put(
        f"https://jsonplaceholder.typicode.com/posts/{id}",
        json=body_json,
        headers=headers,
    )

    assert response.status_code == 200
    json_data = response.json()
    print(json_data)
    assert json_data["id"] == id
    assert json_data["title"] == title
    assert json_data["body"] == body
    assert json_data["userId"] == user_id


def test_patch():
    id = 45
    body_json = {"title": "Zero"}
    headers = {"Content-type": "application/json"}
    response = requests.patch(
        f"https://jsonplaceholder.typicode.com/posts/{id}",
        json=body_json,
        headers=headers,
    )
    assert response.status_code == 200
    json_data = response.json()
    print(json_data)
    assert json_data["id"] == id
    assert json_data["title"] == "Zero"


def test_delete():
    id = 45
    response = requests.patch(f"https://jsonplaceholder.typicode.com/posts/{id}")
    assert response.status_code == 200
