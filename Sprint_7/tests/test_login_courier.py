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
            ({"login": "exist_login", "password": "123"}, 200, "", "Проверка логина с валидными данными"),
            (
                {"login": "", "password": "123"},
                400,
                response_text.bad_request_login_response_text, "Попытка логина с некорректными данными: Отсутствует логин"
            ),
            (
                {"login": "exist_login", "password": ""},
                400,
                response_text.bad_request_login_response_text, "Попытка логина с некорректными данными: Отсутствует пароль"
            ),
            (
                {"login": "exist_login", "password": "1234"},
                404,
                response_text.user_not_found_response_text, "Попытка логина с некорректными данными: Неправильный пароль"
            ),
            (
                {"login": "exist_log", "password": "123"},
                404,
                response_text.user_not_found_response_text, "Попытка логина с некорректными данными: Неправильный логин"
            ),
        ],
    )
    def test_create_courier(self, login_data):
        payload, exp_status_code, exp_text, title_case = login_data
        # Устанавливаем заголовок теста
        allure.dynamic.title(title_case)

        response = requests.post(urls.login_courier_url, data=payload)
        assert response.status_code == exp_status_code
        if response.status_code == 200:
            value = response.json()
            value["id"] != ""
        else:
            assert response.text == exp_text
