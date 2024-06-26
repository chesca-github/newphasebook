import pytest
from phasebook import create_app  # Adjust the import based on your app structure

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
    })

    with app.app_context():
        yield app

@pytest.fixture
def client(app):
    return app.test_client()
