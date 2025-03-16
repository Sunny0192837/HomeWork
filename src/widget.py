from datetime import datetime

from src import masks


def mask_account_card(given_number: str) -> str:
    """Функция, возвращающая замаскированный номер карты/счета"""
    if not given_number:
        raise ValueError("Номер не может быть пустым")

    if not isinstance(given_number, str):
        raise TypeError("Передан некорректный тип данных")

    num = given_number.split(" ")

    if num[0] == "Visa" or num[0] == "MasterCard":
        masked_number = masks.get_mask_card_number(num[-1])
        num[-1] = masked_number

        return f"{' '.join(num)}"
    elif num[0] == "Счет":
        masked_number = masks.get_mask_account(num[-1])
        num[-1] = masked_number

        return f"{' '.join(num)}"


def get_date(date: str) -> str:
    """Функция, возвращающая дату в формате ДД.ММ.ГГГГ"""
    if not date:
        raise ValueError("Строка даты не может быть пустой")

    if not isinstance(date, str):
        raise TypeError("Некорректный тип данных")

    try:
        date_converted = datetime.fromisoformat(date)
        return date_converted.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Введенное значение некорректно")
