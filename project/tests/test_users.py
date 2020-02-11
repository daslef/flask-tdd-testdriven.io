import json

def test_add_user(test_app, test_database):
    client = test_app.test_client()
    resp = client.post('/users', data=json.dumps({'username':'lex', 'email':'daslef93@gmail.com'}), content_type='application/json')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert 'daslef93@gmail.com was added!' in data['message']


def test_add_user_invalid_json(test_app, test_database):
    client = test_app.test_client()
    resp = client.post('/users', data=json.dumps({}), content_type='application/json')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert 'Input payload validation failed' in data['message']


def test_add_user_invalid_json_keys(test_app, test_database):
    client = test_app.test_client()
    resp = client.post('/users', data=json.dumps({'email':'daslef93@gmail.com'}), content_type='application/json')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert 'Input payload validation failed' in data['message']


def test_add_user_dublicate_email(test_app, test_database):
    client = test_app.test_client()
    resp = client.post('/users', data=json.dumps({'username':'lex', 'email':'daslef93@gmail.com'}), content_type='application/json')
    resp = client.post('/users', data=json.dumps({'username':'lex', 'email':'daslef93@gmail.com'}), content_type='application/json')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert 'Sorry. That email already exists.' in data['message']


def test_single_user(test_app, test_database):
    from project import db
    from project.api.models import User
    client = test_app.test_client()
    resp = client.get('/users/99')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 404
    assert 'User 99 does not exist' in data['message']


def test_single_user_incorrect_id(test_app, test_database):
    from project import db
    from project.api.models import User
    user = User(username='dummy', email='dummy@dubby.hey')