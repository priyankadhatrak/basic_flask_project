from re import template
from flask import render_template, Flask
import pytest
from users import app
from mock import Mock
from requests import codes


@pytest.fixture
def fixture_client():
    """Create an api test client fixture."""

    # import pdb; pdb.set_trace()

    return app.app.test_client()

@pytest.fixture
def setUp(self):

    print("This is API testing with 1.Get, 2.Post, 3.Delete methods")

    print("*"*70)



@pytest.fixture
def myrequest(mocker):
    return Mock((), url='https://test-url.com:8000', cookies=None, headers={})
