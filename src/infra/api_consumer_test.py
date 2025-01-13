from .api_consumer import ApiConsumer
from errors.http_request_error import HttpRequesError

# teste em get_starship


def test_get_starships(requests_mock):
    requests_mock.get('https://www.swapi.tech/api/starships/', status_code=200, json={
        'some': 'thing', 'results': [{}]
    })
    api_consumer = ApiConsumer()
    page = 1
    get_starships_response = api_consumer.get_starships(page=page)
    assert get_starships_response.request.method == 'GET'
    assert get_starships_response.request.url == 'https://www.swapi.tech/api/starships/'
    assert get_starships_response.request.params == {"page": page}

    assert get_starships_response.status_code == 200
    assert isinstance(get_starships_response.response["results"], list)


def test_get_starships_error(requests_mock):
    requests_mock.get('https://www.swapi.tech/api/starships/', status_code=404, json={
        'detail': 'something'
    })
    api_consumer = ApiConsumer()
    page = 100

    try:
        api_consumer.get_starships(page=page)
        assert True is False
    except HttpRequesError as error:
        assert error.message is not None
        assert error.status_code is not None
