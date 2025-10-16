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
        ({"limit": "10", "nearestStation": '["1","2"]'})
        
    ])
    def test_return_order_list(self, headers):
        allure.dynamic.title(f'Получение списка заказа с параметрами {headers}')
        headers_param = headers
        response = requests.get(
            urls.return_order_list_url, params=headers_param
        )
        response_body = response.json()
        assert 'orders' in response_body
        if len(response_body['orders']) > 0:
            assert  response_body['orders'][0]['id'] != None
            assert  response_body['orders'][0]['track'] != None
            assert  response_body['orders'][0]['status'] != None
            assert  response_body['orders'][0]['address'] != None
            assert  response_body['orders'][0]['phone'] != None
        
 
