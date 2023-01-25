import os

import requests
from requests import Response
from dotenv import load_dotenv

load_dotenv()
base_url = os.getenv('base_url')


def get_list_of_users(page):
    response: Response = requests.get(f'{base_url}/api/users', params=page)
    return response


def get_user(user_id):
    response: Response = requests.get(f'{base_url}/api/users/{user_id}')
    return response


def post_create_users(name, job):
    json = {'name': name,
            'job': job
            }
    response = requests.post(f'{base_url}/api/users', json=json)
    return response


def update_user(user_id, name, job):
    json = {
        'name': name,
        'job': job
    }
    response = requests.put(f'{base_url}/api/users/{user_id}', json=json)
    return response


def delete_user(id_user):
    response = requests.delete(f'{base_url}/api/users/{id_user}')
    return response


def post_register_user(email, password):
    json = {
        'email': email,
        'password': password
    }
    response = requests.post(f'{base_url}/api/register', json=json)
    return response


def post_unsuccessful_register_user(email, password):
    json = {
        'email': email,
        'password': password
    }
    response = requests.post(f'{base_url}/api/register', json=json)
    return response


def post_login_user(email, password):
    json = {
        'email': email,
        'password': password
    }
    response = requests.post(f'{base_url}/api/login', json=json)
    return response


def post_login_unsuccessful_user(email):
    json = {
        'email': email,
    }
    response = requests.post(f'{base_url}/api/login', json=json)
    return response
