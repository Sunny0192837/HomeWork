def get_mask_card_number(card_number: str) -> str:
    """Функция, конвертирующая номер карты в замаскированный номер карты"""

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция, конвертирующая номер счета в замаскированный номер счета"""

    return f"**{account_number[-4:]}"
