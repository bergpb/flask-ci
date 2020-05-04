from tests import client


def test_index_return_200(client):
    res = client.get("/")
    assert res.status_code == 200


def test_page_content(client):
    res = client.get("/")
    assert b"Hello world from Flask CI example." in res.data
