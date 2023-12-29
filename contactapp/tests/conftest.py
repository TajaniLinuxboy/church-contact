import pytest
from app import app

@pytest.fixture()
def myapp():
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


