import requests
from helpers import base_scripts
from data import response_text
from data import urls
import pytest
import allure

class TestCreateCourier:
    @allure.description('Проверка апи создания курьера: api/v1/courier')
    @allure.feature('Создания курьера')
    @pytest.mark.parametrize('courier_data',[
        (base_scripts.generate_new_courier_payload(), 201, response_text.success_response_text, 'Создание нового курьера с валидными данными'),
        (base_scripts.register_new_courier_and_return_payload(), 409, response_text.two_same_courier_response_text, 'Попытка создания курьера с уже существующим логином'),
        ({"login": "", "password": "123", "firstName": "Имя536271735"}, 400, response_text.bad_request_response_text, 'Создание курьера, отсутствуют обязательные поля: отсутсвует логин'),
        ({"login": "ew32432", "password": "", "firstName": "Имя536271735"}, 400, response_text.bad_request_response_text, 'Создание курьера, отсутствуют обязательные поля: отсутсвует пароль')

    ])
    def test_create_courier(self, courier_data):
        payload, exp_status_code, exp_text, title_case = courier_data
        # Устанавливаем заголовок теста
        allure.dynamic.title(title_case)        
        response = requests.post(urls.create_courier_url
            , data=payload
        )
        assert response.status_code == exp_status_code
        assert response.text == exp_text