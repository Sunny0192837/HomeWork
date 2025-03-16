# Проект HomeWork
## Описание: 
Проект HomeWork - это учебный проект разработки виджета для личного кабинета клиента
## Документация:
Проект содержит модули:
+ masks
+ widget
+ processing
### Модуль masks содержит функции для маскировки номер карт/счетов:
```commandline
def get_mask_card_number(card_number: str) -> str:
    """Функция, конвертирующая номер карты в замаскированный номер карты"""

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция, конвертирующая номер счета в замаскированный номер счета"""

    return f"**{account_number[-4:]}"
```
### Модуль widget содержит функции для работы с датой и номерами:
```commandline
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


def get_date(date: str) -> str:
    """Функция, возвращающая дату в формате ДД.ММ.ГГГГ"""

    date_converted = datetime.fromisoformat(date)
    return date_converted.strftime("%d.%m.%Y")
```
### Модуль processing содержит функции для сортировки словарей
```commandline
from datetime import datetime


def filter_by_state(dicts: list, state: str = "EXECUTED") -> list:
    """Возвращает все словари с нужным значением ключа 'state'"""

    needed_list = []

    for item in dicts:
        if item.get("state") == state:
            needed_list.append(item)

    return needed_list


def sort_by_date(dicts: list, reverse: bool = True) -> list:
    """Возвращает список, отсортированный по дате"""

    sorted_list = sorted(
        dicts,
        key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=reverse,
    )

    return sorted_list
```
