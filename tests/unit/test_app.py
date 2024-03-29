import pytest
import requests

base_url = "http://127.0.0.1:5000"
headers_test = {'Content-Type': 'application/json'}


def test_get_student():
    response = requests.get(url=str(base_url + '/student/get/1'), headers=headers_test)
    assert 201 == response.status_code
    print(response.text)


def test_get_all_student():
    response = requests.get(url=str(base_url + '/student/getall'), headers=headers_test)
    assert 201 == response.status_code
    print(response.text)


def test_create_student():
    sample_payload = {
        "name": "Sunil",
        "rollno": 45
    }
    response = requests.post(url=str(base_url + '/student/create'), headers=headers_test, json=sample_payload)
    assert response.status_code == 201
    print(response.text)


def test_update_room():
    sample_payload = {
        "name": "Sahil",
    }
    response = requests.post(url=str(base_url + '/student/update/2'), headers=headers_test, json=sample_payload)
    assert response.status_code == 201


def test_delete_student():
    response = requests.delete(url=str(base_url + '/student/delete/2'), headers=headers_test)
    assert 201 == response.status_code
    print(response.text)
