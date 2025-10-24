import requests
from data import urls
import pytest
import allure
from data import data

class TestCreateOrder:
    @allure.description('Проверка апи создания заказа: /api/v1/orders')
    @allure.feature('Проверка созданя заказа')
    @allure.severity("High")
    @pytest.mark.parametrize('order_data',[("BLACK", 'Создание заказа с черным самокатом'),
                                            ("GREY", 'Создание заказа с серым самокатом'),
                                            (("BLACK", "GREY"), 'Создание заказа с черным или серым самокатом'),
                                            ((), 'Создание заказа: Не выбран ни один цвет')])
    def test_create_courier(self, order_data):
        # Устанавливаем заголовок в зависимости от тестируемых данных
        color, title_case = order_data
        payload = data.get_order_data_with_color(self, color)
        allure.dynamic.title(title_case)
        response = requests.post(urls.create_order_url
            , json=payload
        )
    
        assert response.status_code == 201
        value = response.json()
        assert value['track'] != ''
