import pytest

from src import masks


@pytest.mark.parametrize("card_number, error_type", [
    (123, TypeError),
    ('123412341234', ValueError),
    ('123412341234word', ValueError)
])
def test_get_mask_card_number_errors(card_number, error_type):
    with pytest.raises(error_type):
        masks.get_mask_card_number(card_number)


def test_get_mask_card_number_correct(correct_card_number, correct_card_number_masked):
    assert masks.get_mask_card_number(correct_card_number) == correct_card_number_masked

@pytest.mark.parametrize("account_number, error_type", [
    (123, TypeError),
    ('123412341234', ValueError),
    ('123412341234word1234', ValueError)
])
def test_get_mask_account_errors(account_number, error_type):
    with pytest.raises(error_type):
        masks.get_mask_account(account_number)

def test_get_mask_account_correct(correct_account_number, correct_account_number_masked):
    assert masks.get_mask_account(correct_account_number) == correct_account_number_masked