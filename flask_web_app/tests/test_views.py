from website import create_app
import pytest
from unittest.mock import Mock
from website import views

@pytest.fixture
def client():
    flask_app = create_app(reset_database=True)
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as test_client:
        yield test_client


def login(client, email, password):
    return client.post('/login', data=dict(
        email=email,
        password=password
    ), follow_redirects=True)


def logout(client):
    return client.get('/logout', follow_redirects=True)


def sign_up(client, email='mich@mich.com', first_name='Michal', github='michalwegiel', password1='1234567',
            password2='1234567'):
    return client.post('/sign-up', data=dict(
        email=email,
        firstName=first_name,
        github=github,
        password1=password1,
        password2=password2,
    ), follow_redirects=True)


def test_login_page_get(client):
    response = client.get('/login')
    expected_html = b"""<form method="POST">
    <h3 align="center">Login</h3>
    <div class="form-group">
        <label for="email">Email Address</label>
        <input
                type="email"
                class="form-control"
                id="email"
                name="email"
                placeholder="Enter email"
        />
    </div>
    <div class="form-group">
        <label for="password">Enter Password</label>
        <input
                type="password"
                class="form-control"
                id="password"
                name="password"
                placeholder="Enter Password"
        />
    </div>
    <br />
    <button type="submit" class="btn btn-primary">Login</button>
</form>"""
    assert response.status_code == 200
    assert expected_html in response.data


def test_sign_up_page_get(client):
    response = client.get('/sign-up')
    expected_html = b"""<form method="POST">
    <h3 align="center">Sign Up</h3>
    <div class="form-group">
        <label for="email">Email Address</label>
        <input
                type="email"
                class="form-control"
                id="email"
                name="email"
                placeholder="Enter email"
        />
    </div>
    <div class="form-group">
        <label for="firstName">First Name</label>
        <input
                type="text"
                class="form-control"
                id="firstName"
                name="firstName"
                placeholder="Enter first name"
        />
    </div>
    <div class="form-group">
        <label for="github">Github User Name</label>
        <input
                type="text"
                class="form-control"
                id="github"
                name="github"
                placeholder="Enter github user name"
        />
    </div>
    <div class="form-group">
        <label for="password1">Enter Password</label>
        <input
                type="password"
                class="form-control"
                id="password1"
                name="password1"
                placeholder="Enter Password"
        />
    </div>
    <div class="form-group">
        <label for="password2">Password (Confirm)</label>
        <input
                type="password"
                class="form-control"
                id="password2"
                name="password2"
                placeholder="Confirm Password"
        />
    </div>
    <br />
    <button type="submit" class="btn btn-primary">Submit</button>
</form>"""
    assert response.status_code == 200
    assert expected_html in response.data


def test_sign_up(client):
    response = sign_up(client)
    assert response.status_code == 200
    assert b"Account created!" in response.data


def test_logout(client):
    sign_up(client)
    response = logout(client)
    assert response.status_code == 200
    assert b"Logged out!" in response.data


def test_login(client):
    sign_up(client)
    logout(client)
    response = login(client, email='mich@mich.com', password='1234567')
    assert response.status_code == 200
    assert b"Logged in successfully!" in response.data


def test_api(client, monkeypatch) -> None:
    api = Mock(return_value={'login': 'some_random_login', 'id': 'id1234id'})
    monkeypatch.setattr(views, 'get_github_info', api)
    response = sign_up(client)
    assert response.status_code == 200
    assert b"<td>some_random_login</td>" in response.data
    assert b"<td>id1234id</td>" in response.data
