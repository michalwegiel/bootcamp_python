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


@pytest.fixture
def set_api_mock(monkeypatch):
    api = Mock(return_value={'login': 'some_random_login', 'id': 'id1234id'})
    monkeypatch.setattr(views, 'get_github_info', api)
    return api


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


def test_sign_up(client, set_api_mock):
    response = sign_up(client)
    assert response.status_code == 200
    assert b"Account created!" in response.data


def test_logout(client, set_api_mock):
    sign_up(client)
    response = logout(client)
    assert response.status_code == 200
    assert b"Logged out!" in response.data


def test_login(client, set_api_mock):
    sign_up(client)
    logout(client)
    response = login(client, email='mich@mich.com', password='1234567')
    assert response.status_code == 200
    assert b"Logged in successfully!" in response.data


def test_api(client, set_api_mock) -> None:
    response = sign_up(client)
    assert response.status_code == 200
    assert b"<td>some_random_login</td>" in response.data
    assert b"<td>id1234id</td>" in response.data
    set_api_mock.assert_called()


def test_home_page_negative(client):
    response = client.get('/')
    assert response.status_code == 302
    assert b"You should be redirected automatically to target URL: <a href=\"/login?next=%2F\">/login?next=%2F</a>" in response.data


def test_sign_up_negative_email_already_exists(client, set_api_mock):
    signing_up = sign_up(client, email='michal123@gmail.com', first_name='Mich', github='github_user',
                         password1='1234567', password2='1234567')
    assert b"Account created!" in signing_up.data
    logging_out = logout(client)
    assert b"Logged out!" in logging_out.data
    response = sign_up(client, email='michal123@gmail.com', first_name='Adam', github='github_user_2',
                       password1='abcdefgh', password2='abcdefgh')
    assert 200 == response.status_code
    assert b"Email already exists." in response.data


def test_sign_up_negative_email_too_short(client):
    response = sign_up(client, email='m@', first_name='Mich', github='github_user', password1='1234567',
                       password2='1234567')
    assert 200 == response.status_code
    assert b"Not valid email." in response.data


def test_sign_up_negative_first_name_too_short(client):
    response = sign_up(client, email='michal@gmail.com', first_name='M', github='github_user', password1='1234567',
                       password2='1234567')
    assert 200 == response.status_code
    assert b"First name must be greater than 1 character." in response.data


def test_sign_up_negative_not_matching_passwords(client):
    attempt_1 = sign_up(
        client,
        email='michal@gmail.com',
        first_name='Michal',
        github='github_user',
        password1='1234567',
        password2='12345678',
    )
    assert 200 == attempt_1.status_code
    assert b"Passwords do not match." in attempt_1.data
    attempt_2 = sign_up(
        client,
        email='michal@gmail.com',
        first_name='Michal',
        github='github_user',
        password1='0234567',
        password2='1234567',
    )
    assert 200 == attempt_2.status_code
    assert b"Passwords do not match." in attempt_2.data


def test_sign_up_negative_password_too_short(client):
    response = sign_up(
        client,
        email='michal@gmail.com',
        first_name='Michal',
        github='github_user',
        password1='abcd',
        password2='abcd',
    )
    assert 200 == response.status_code
    assert b"Password must be at least 7 characters." in response.data


def test_logging_in_negative_email_does_not_exist(client, set_api_mock):
    signing_up = sign_up(client, email='michal123@gmail.com', first_name='Mich', github='github_user',
                         password1='1234567', password2='1234567')
    assert b"Account created!" in signing_up.data
    logging_out = logout(client)
    assert b"Logged out!" in logging_out.data
    response = login(client, email='adam@gmail.com', password='1234567')
    assert 200 == response.status_code
    assert b"Email does not exist." in response.data


def test_logging_in_negative_incorrect_password(client, set_api_mock):
    signing_up = sign_up(client, email='michal123@gmail.com', first_name='Mich', github='github_user',
                         password1='1234567', password2='1234567')
    assert b"Account created!" in signing_up.data
    logging_out = logout(client)
    assert b"Logged out!" in logging_out.data
    response = login(client, email='michal123@gmail.com', password='12345678')
    assert 200 == response.status_code
    assert b"Invalid password, try again!" in response.data


def test_logging_in_negative_empty_login_form(client, set_api_mock):
    signing_up = sign_up(client, email='michal123@gmail.com', first_name='Mich', github='github_user',
                         password1='1234567', password2='1234567')
    assert b"Account created!" in signing_up.data
    logging_out = logout(client)
    assert b"Logged out!" in logging_out.data
    response = login(client, email='', password='')
    assert 200 == response.status_code
    assert b"Email does not exist." in response.data
