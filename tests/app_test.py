import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    return client

def test_retorno_200(client):
    res = client.get('/')
    assert res.status_code == 200

def test_conteudo_pagina(client):
    res = client.get('/')
    assert b"Hello world from Flask CI example." in res.data
