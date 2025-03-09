def filter_by_state(dicts: list, state: str = "EXECUTED") -> list:
    """Возвращает все словари с нужным значением ключа 'state'"""

    needed_list = []

    for item in dicts:
        if item.get("state") == state:
            needed_list.append(item)

    return needed_list
