import pytest
import requests


url = 'http://localhost:5021' # The root url of the flask app

def test_index_page():
    r = requests.get(url+'/')
    assert r.status_code == 200


def test_login():
    r = requests.get(url + '/')
    data = r.json()
    assert data['username'] == 'admin'
    assert data['password'] == 'admin'
