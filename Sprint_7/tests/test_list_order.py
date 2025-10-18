import requests
from data import urls
import allure
import pytest


class TestListOrders:
    @allure.description("Проверка апи получения списка заказов: GET /api/v1/orders")
    @allure.feature("Получения списка заказов")
    @pytest.mark.parametrize('headers',[
        ({"limit": "1", "page": "0"}),
        ({"courierId":"629840"}),
        ({"limit": "10", "nearestStation": '["1","2", "3", "4"]'})
        
    ])
    def test_return_order_list(self, headers):
        allure.dynamic.title(f'Получение списка заказа с параметрами {headers}')
        headers_param = headers
        response = requests.get(
            urls.return_order_list_url, params=headers_param
        )
        response_body = response.json()
        #Проверка, что тело ответа содержит заказы
        assert 'orders' in response_body
        
 
