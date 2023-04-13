import requests
import allure


server = 'https://regions-test.2gis.com/1.0/regions'


@allure.title('Проверка статус кода запроса без параметров и типа содержимого ответа')
def test_all_regions_status_code_200_and_format_json():
    url = server
    response = requests.get(url, data=None, verify=False)
    assert response.status_code == 200
    assert response.headers['Content-type'] == 'application/json; charset=utf-8'
    print('response_status_code', response.status_code)
    print(response.json())


@allure.title('Запрос с корректным параметром q')
def test_all_regions_good_q_param():
    qs = ['Москва', 'москва', 'рск']
    for q in qs:
        url = f'{server}?q={q}'
        response = requests.get(url, data=None, verify=False)
        assert response.status_code == 200
        print('q', q, 'response_status_code', response.status_code)
        print(response.json())


@allure.title('Проверка, что, если передан параметр q, остальные параметры игнорируются')
def test_all_regions_ignore_other_params_except_q():
    q = 'Москва'
    country_code = 'kz'
    page = 2
    page_size = 5
    url = f'{server}?q={q}&country_code={country_code}&page={page}&page_size={page_size}'
    response = requests.get(url, data=None, verify=False)
    assert response.status_code == 200
    print('response_status_code', response.status_code)
    print(response.json())


@allure.title('Запрос с корректным параметром country_code')
def test_all_regions_good_country_code_param():
    country_codes = ['ru', 'kg', 'kz', 'cz']
    for country_code in country_codes:
        url = f'{server}?country_code={country_code}'
        response = requests.get(url, data=None, verify=False)
        assert response.status_code == 200
        print('country_code', country_code, 'response_status_code', response.status_code)
        print(response.json())


@allure.title('Запрос с корректным параметром page')
def test_all_regions_good_page_param():
    page = 1
    url = f'{server}?page={page}'
    response = requests.get(url, data=None, verify=False)
    assert response.status_code == 200
    print('page', page, 'response_status_code', response.status_code)
    print(response.json())


@allure.title('Проверка пагинации')
def test_all_regions_pagination():
    page_sizes = [5, 10, 15]
    for page_size in page_sizes:
        status_code = 200
        page = 1
        while status_code == 200:
            url = f'{server}?page={page}&page_size={page_size}'
            response = requests.get(url, data=None, verify=False)
            print('page_size', page_size, 'page', page, 'response_status_code', response.status_code)
            assert response.status_code in (200, 404)
            status_code = response.status_code
            if status_code == 200:
                page = page + 1
                print('page_size', page_size)


@allure.title('Запрос с корректным параметром page_size')
def test_all_regions_good_page_size_param():
    page_sizes = [5, 10, 15]
    for page_size in page_sizes:
        url = f'{server}?page_size={page_size}'
        response = requests.get(url, data=None, verify=False)
        assert response.status_code == 200
        print('page_size', page_size, 'response_status_code', response.status_code)
        print(response.json())
