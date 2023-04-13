import requests
import allure


server = 'https://regions-test.2gis.com/1.0/regions'


@allure.title('Запрос с некорректным параметром q')
def test_all_regions_bad_q_param():
    qs = ['ва', 'Moscow', '@', 123]
    for q in qs:
        url = f'{server}?q={q}'
        response = requests.get(url, data=None, verify=False)
        assert response.status_code == 400
        print('q', q, 'response_status_code', response.status_code)
        print(response.json())


@allure.title('В параметре q задан город, которого нет в базе')
def test_all_regions_nonexistent_region():
    q = 'Краснодар'
    url = f'{server}?q={q}'
    response = requests.get(url, data=None, verify=False)
    assert response.status_code == 404
    print('response_status_code', response.status_code)
    print(response.json())


@allure.title('Запрос с некорректным параметром country_code')
def test_all_regions_bad_country_code_param():
    country_codes = ['usa', 123, '@', 'рус']
    for country_code in country_codes:
        url = f'{server}?country_code={country_code}'
        response = requests.get(url, data=None, verify=False)
        assert response.status_code == 400
        print('country_code', country_code, 'response_status_code', response.status_code)
        print(response.json())


@allure.title('Запрос с некорректным параметром page')
def test_all_regions_bad_page_param():
    pages = [0, 1.5, 'один']
    for page in pages:
        url = f'{server}?page={page}'
        response = requests.get(url, data=None, verify=False)
        assert response.status_code == 400
        print('page', page, 'response_status_code', response.status_code)
        print(response.json())


@allure.title('Запрос с некорректным параметром page_size')
def test_all_regions_good_page_size_param():
    page_sizes = [-1, 1.5, 4, 7, 13, 16]
    for page_size in page_sizes:
        url = f'{server}?page_size={page_size}'
        response = requests.get(url, data=None, verify=False)
        assert response.status_code == 400
        print('page_size', page_size, 'response_status_code', response.status_code)
        print(response.json())
