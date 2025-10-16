import requests
from data import response_text
from data import urls
import pytest
import allure


class TestLoginCourier:
    @allure.description("Проверка апи логина курьера: /api/v1/courier/login")
    @allure.feature("Логин курьера")
    @pytest.mark.parametrize(
        "login_data",
        [
            ({"login": "exist_login", "password": "123"}, 200, ""),
            (
                {"login": "", "password": "123"},
                400,
                response_text.bad_request_login_response_text,
            ),
            (
                {"login": "exist_login", "password": ""},
                400,
                response_text.bad_request_login_response_text,
            ),
            (
                {"login": "exist_login", "password": "1234"},
                404,
                response_text.user_not_found_response_text,
            ),
            (
                {"login": "exist_log", "password": "123"},
                404,
                response_text.user_not_found_response_text,
            ),
        ],
    )
    def test_create_courier(self, login_data):
        payload, exp_status_code, exp_text = login_data
        print(payload)
        # Устанавливаем заголовок в зависимости от тестируемых данных
        if exp_status_code == 200:
            allure.dynamic.title("Проверка логина с валидными данными")
            allure.dynamic.severity("Bloked")
        elif exp_status_code == 404:
            allure.dynamic.title("Попытка логина с некорректными данными")
            allure.dynamic.severity("High")
        else:
            allure.dynamic.title(
                f"Логин курьера, отсутствуют обязательные поля: статус {exp_status_code}"
            )
            allure.dynamic.severity("Medium")
        response = requests.post(urls.login_courier_url, data=payload)
        assert response.status_code == exp_status_code
        if response.status_code == 200:
            value = response.json()
            value["id"] != ""
        else:
            assert response.text == exp_text
