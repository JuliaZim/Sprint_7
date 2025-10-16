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
        (base_scripts.generate_new_courier_payload(), 201, response_text.success_response_text),
        (base_scripts.register_new_courier_and_return_payload(), 409, response_text.two_same_courier_response_text),
        ({"login": "", "password": "123", "firstName": "Имя536271735"}, 400, response_text.bad_request_response_text),
        ({"login": "ew32432", "password": "", "firstName": "Имя536271735"}, 400, response_text.bad_request_response_text)

    ])
    def test_create_courier(self, courier_data):
        payload, exp_status_code, exp_text = courier_data
        # Устанавливаем заголовок в зависимости от тестируемых данных
        if exp_status_code == 201:
            allure.dynamic.title('Создание нового курьера с валидными данными')
            allure.dynamic.severity("Bloked")
        elif exp_status_code == 409:
            allure.dynamic.title('Попытка создания курьера с уже существующим логином')
            allure.dynamic.severity("High")
        else:
            allure.dynamic.title(f'Создание курьера, отсутствуют обязательные поля: статус {exp_status_code}')
            allure.dynamic.severity("Medium")
        
        response = requests.post(urls.create_courier_url
            , data=payload
        )
        assert response.status_code == exp_status_code
        assert response.text == exp_text