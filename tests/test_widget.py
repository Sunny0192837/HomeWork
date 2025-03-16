import pytest

from src import widget


def test_mask_account_card_visa():
    result = widget.mask_account_card("Visa 1234567890123456")
    expected = "Visa 1234 56** **** 3456"
    assert result == expected


def test_mask_account_card_mastercard():
    result = widget.mask_account_card("MasterCard 9876543210987654")
    expected = "MasterCard 9876 54** **** 7654"
    assert result == expected


def test_mask_account_card_account():
    result = widget.mask_account_card("Счет 12345678901234567890")
    expected = "Счет **7890"
    assert result == expected


def test_mask_account_card_invalid_type():
    with pytest.raises(TypeError):
        widget.mask_account_card(1234567890123456)


def test_mask_account_card_empty_value():
    with pytest.raises(ValueError):
        widget.mask_account_card('')


def test_get_date_correct():
    result = widget.get_date("2019-07-03T18:35:29.512364")
    expected = "03.07.2019"
    assert result == expected


def test_get_date_invalid_format():
    with pytest.raises(ValueError):
        widget.get_date("2019/07/03")


def test_get_date_empty_string():
    with pytest.raises(ValueError):
        widget.get_date("")

def test_get_date_invalid_type():
    with pytest.raises(TypeError):
        widget.get_date(123)