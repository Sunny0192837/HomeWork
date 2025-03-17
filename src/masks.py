def get_mask_card_number(card_number: str) -> str:
    """Функция, конвертирующая номер карты в замаскированный номер карты"""

    if not isinstance(card_number, str):
        raise TypeError("В функцию передан некорректный тип данных")

    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен иметь длину в 16 символов и состоять только из цифр")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция, конвертирующая номер счета в замаскированный номер счета"""

    if not isinstance(account_number, str):
        raise TypeError("В функцию передан некорректный тип данных")

    if len(account_number) != 20 or not account_number.isdigit():
        raise ValueError("Номер счета должен иметь длину в 20 символов и состоять только из цифр")

    return f"**{account_number[-4:]}"
