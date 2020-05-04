import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    context = app.app_context()
    context.push()

    yield app.test_client()

    context.pop()
