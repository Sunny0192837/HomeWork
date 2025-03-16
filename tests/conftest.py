import pytest


@pytest.fixture
def correct_card_number():
    return '1234123412341234'

@pytest.fixture
def correct_card_number_masked():
    return "1234 12** **** 1234"

@pytest.fixture
def correct_account_number():
    return '12341234190348549087'

@pytest.fixture
def correct_account_number_masked():
    return "**9087"

@pytest.fixture
def dicts_list():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
     {'id': 939719570, 'date': '2018-06-30T02:08:58.425572'},
     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]




