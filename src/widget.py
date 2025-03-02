from src import masks


def mask_account_card(given_number: str) -> str:
    """Функция, возвращающая замаскированный номер карты/счета"""

    num = given_number.split(" ")

    if num[0] == "Visa" or num[0] == "MasterCard":
        masked_number = masks.get_mask_card_number(num[-1])
        num[-1] = masked_number

        return f"{' '.join(num)}"
    elif num[0] == "Счет":
        masked_number = masks.get_mask_account(num[-1])
        num[-1] = masked_number

        return f"{' '.join(num)}"
    else:
        return "Вы ввели некорректное значение"
