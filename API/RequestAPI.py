import requests
from faker import Faker
import json

Base_url = "https://gorest.co.in/"
auth_token = "Bearer bc38b48c8525efc79696d726e9523cd006e5b4d721b94e5c36bfdad1c6f07f5c"


def generate_random_email():
    fake = Faker()
    return fake.email()


def generate_random_full_name():
    fake = Faker()
    return fake.name()


full_name = generate_random_full_name()
email_id = generate_random_email()


def post_request():
    url = Base_url + "/public/v2/users"
    print("Post Url", url)
    header = {"Authorization": auth_token}
    data = {
        "name": full_name,
        "email": email_id,
        "gender": "male",
        "status": "active"

    }
    response = requests.post(url, json=data, headers=header)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json POST response: ", json_str)
    user_id = json_data["id"]
    user_name = json_data["name"]
    assert "name" in json_data
    assert json_data["name"] == user_name
    print("....User is Craeted....")
    print("....=================....")
    return user_id


def get_request(user_id):
    url = Base_url + f"/public/v2/users/{user_id}"
    print("get url:", url)
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json GET response: ", json_data)
    print("....GET user is done....")
    print("....================....")


def get_all_request():
    url = Base_url + f"/public/v2/users/"
    print("get url:", url)
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json GET response: ", json_data)
    print("....GET user is done....")
    print("....================....")


def PUT_request(user_id):
    url = Base_url + f"/public/v2/users/{user_id}"
    print("Post url:", url)
    headers = {"Authorization": auth_token}
    data = {
        "name": full_name,
        "email": generate_random_email(),
        "gender": "male",
        "status": "inactive"
    }
    resposne = requests.put(url, json=data, headers=headers)
    assert resposne.status_code == 200
    json_data = resposne.json()
    json_str = json.dumps(json_data, indent=4)
    print("json PUT response: ", json_str)
    assert json_data["id"] == user_id
    assert json_data["status"] == "inactive"
    print("....User details is updated ....")
    print("....=======================....")


def Delete_request(user_id):
    url = Base_url + f"/public/v2/users/{user_id}"
    print("Delete Url:", url)
    headers = {"Authorization": auth_token}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print("....User is Deleted....")
    print("....===============....")


user_id = post_request()
get_all_request()
get_request(user_id)
PUT_request(user_id)
Delete_request(user_id)
