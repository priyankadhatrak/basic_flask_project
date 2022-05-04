import pytest

@pytest.mark.great
def test_greater():
    assert 10 > 5

@pytest.mark.others
def test_less():
    assert 20 < 90