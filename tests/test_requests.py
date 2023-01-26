import os
import allure
import requests
from allure_commons.types import Severity
from pytest_voluptuous import S
from requests import Response
from reqres_tests.utils import attach
from reqres_tests.schemas.requests_schema import create_user_schema, get_user_schema, login_successful_schema, \
    login_unsuccessful_schema, register_unsuccessful_user_schema, update_user_schema, register_successful_user_shema
from reqres_tests.reqres import get_list_of_users, get_user, update_user, post_create_users, post_register_user, \
    post_login_user, post_login_unsuccessful_user, post_unsuccessful_register_user
from dotenv import load_dotenv


load_dotenv()
base_url = os.getenv('base_url')
user_id = os.getenv('user_id')
name = os.getenv('name')
job = os.getenv('job')
login = os.getenv('login')
password = os.getenv('password')
email = os.getenv('email')
invalid_email = os.getenv('invalid_email')
invalid_password = os.getenv('invalid_password')


@allure.tag('critical')
@allure.severity(Severity.BLOCKER)
@allure.feature('API-тесты reqres.in')
@allure.story('Данные пользователей')
@allure.title('Отображение списка пользователей')
def test_list_of_users():
    with allure.step('GET запрос, отображает список пользователей на странице'):
        response = get_list_of_users(page={"page": 2})
    assert response.status_code == 200
    assert response.json()['page'] == 2
    assert len(response.json()['data']) != 0
    attach.add_curl(response)
    attach.add_response(response)


@allure.tag('critical')
@allure.severity(Severity.BLOCKER)
@allure.feature('API-тесты reqres.in')
@allure.story('Авторизация пользователя')
@allure.title('Успешное создание пользователя')
def test_create_user():
    with allure.step('POST запрос, создает пользователя'):
        response = post_create_users(name, job)
    assert response.status_code == 201
    assert response.json()['name'] == name
    assert response.json()['job'] == job
    assert isinstance(response.json()['id'], str)
    assert response.json() == S(create_user_schema)
    attach.add_body_request(response)
    attach.add_curl(response)
    attach.add_response(response)


@allure.tag('critical')
@allure.severity(Severity.BLOCKER)
@allure.feature('API-тесты reqres.in')
@allure.story('Авторизация пользователя')
@allure.title('Успешное изменение данных пользователя')
def test_update_user():
    with allure.step('PUT запрос, обновляет данные пользователя'):
        response = update_user(user_id, name, job)
    assert response.status_code == 200
    assert response.json()['name'] == name
    assert response.json()['job'] == job
    assert response.json() == S(update_user_schema)
    attach.add_body_request(response)
    attach.add_curl(response)
    attach.add_response(response)


@allure.tag('critical')
@allure.severity(Severity.BLOCKER)
@allure.feature('API-тесты reqres.in')
@allure.story('Данные пользователей')
@allure.title('Получение данных пользователя по id')
def test_user_data():
    with allure.step('GET запрос, отображает данные пользователя '):
        response = get_user(user_id)
    assert response.status_code == 200
    assert response.json() == S(get_user_schema)
    attach.add_curl(response)
    attach.add_response(response)


@allure.tag('critical')
@allure.severity(Severity.BLOCKER)
@allure.feature('API-тесты reqres.in')
@allure.story('Регистрация')
@allure.title('Регистрация пользователя')
def test_successful_user_registration():
    with allure.step('POST запрос, успешная регистрация пользователя'):
        response = post_register_user(email, password)
    assert response.status_code == 200
    assert response.json() == S(register_successful_user_shema)
    attach.add_body_request(response)
    attach.add_curl(response)
    attach.add_response(response)


@allure.tag('critical')
@allure.severity(Severity.BLOCKER)
@allure.feature('API-тесты reqres.in')
@allure.story('Авторизация пользователя')
@allure.title('Успешная авторизация пользователя')
def test_login_successful():
    with allure.step('POST запрос, успешная авторизация пользователя'):
        response = post_login_user(email, password)
    assert response.status_code == 200
    assert response.json() == S(login_successful_schema)
    attach.add_curl(response)
    attach.add_response(response)


@allure.tag('critical')
@allure.severity(Severity.BLOCKER)
@allure.feature('API-тесты reqres.in')
@allure.story('Авторизация пользователя')
@allure.title('Неуспешная авторизация пользователя')
def test_login_unsuccessful():
    with allure.step('POST запрос, неуспешная авторизация пользователя'):
        response = post_login_unsuccessful_user(email)
    assert response.status_code == 400
    assert response.json() == S(login_unsuccessful_schema)
    attach.add_body_request(response)
    attach.add_curl(response)
    attach.add_response(response)


@allure.tag('critical')
@allure.severity(Severity.BLOCKER)
@allure.feature('API-тесты reqres.in')
@allure.story('Авторизация пользователя')
@allure.title('Неуспешная регистрация пользователя')
def test_unsuccessful_user_registration():
    with allure.step('POST запрос, неуспешная регистрация пользователя'):
        response = post_unsuccessful_register_user(invalid_email, invalid_password)
    print(response)
    assert response.status_code == 400
    assert response.json() == S(register_unsuccessful_user_schema)
    attach.add_body_request(response)
    attach.add_curl(response)
    attach.add_response(response)