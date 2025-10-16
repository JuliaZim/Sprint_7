import requests
from data import urls
import pytest
import allure
from data import data

class TestCreateOrder:
    @allure.description('Проверка апи создания заказа: /api/v1/orders')
    @allure.feature('Проверка созданя заказа')
    @allure.severity("High")
    @pytest.mark.parametrize('color',["BLACK", "GREY", ("BLACK", "GREY"), ()])
    def test_create_courier(self, color):
        # Устанавливаем заголовок в зависимости от тестируемых данных
        
        payload = data.get_order_data_with_color(self, color)
        if color == "BLACK":
            allure.dynamic.title('Создание заказа с черным самокатом')

        elif color == "GREY":
            allure.dynamic.title('Создание заказа с серым самокатом')
        else:
            allure.dynamic.title(f'Создание заказа с цветами {color}')
        response = requests.post(urls.create_order_url
            , json=payload
        )
    
        assert response.status_code == 201
        value = response.json()
        assert value['track'] != ''
