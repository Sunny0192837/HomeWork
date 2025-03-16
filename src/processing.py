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
