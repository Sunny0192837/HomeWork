import pytest

from src import processing


def test_filter_by_state_correct(dicts_list):
    result = processing.filter_by_state(dicts_list, "EXECUTED")
    expected = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ]
    assert result == expected

    result = processing.filter_by_state(dicts_list, "CANCELED")
    expected = [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
    assert result == expected


def test_filter_by_state_empty_list():
    with pytest.raises(ValueError):
        processing.filter_by_state([])


def test_filter_by_state_invalid_type():
    with pytest.raises(TypeError):
        processing.filter_by_state({"state": "EXECUTED"})


def test_filter_by_state_no_key(dicts_list):
    result = processing.filter_by_state(dicts_list, "EXECUTED")
    expected = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ]
    assert result == expected


def test_sort_by_date_correct(dicts_list):
    result = processing.sort_by_date(dicts_list)
    expected = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'date': '2018-06-30T02:08:58.425572'}
    ]
    assert result == expected


def test_sort_by_date_ascending(dicts_list):
    result = processing.sort_by_date(dicts_list, reverse=False)
    expected = [
        {'id': 939719570, 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ]
    assert result == expected


def test_sort_by_date_empty_list():
    with pytest.raises(ValueError):
        processing.sort_by_date([])


def test_sort_by_date_invalid_type():
    with pytest.raises(TypeError):
        processing.sort_by_date(123)