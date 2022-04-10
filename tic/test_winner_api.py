from api import app


def test_api_is_wsgi_app():
    assert hasattr(app, 'wsgi_app')


def test_api_missing_parameter():
    assert app.test_client().get('/winner').status_code == 400


def test_api_response_is_json():
    response = app.test_client().get('/winner?board=_________')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert isinstance(response.json, dict)
    assert 'winner' in response.json
