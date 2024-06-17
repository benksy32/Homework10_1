from typing import Dict, List


def filter_by_state(data: List[Dict[str, str]], state: str = "EXECUTED") -> List[Dict[str, str]]:
    """Функция фильтрует список словарей по указанному состоянию."""
    return [d for d in data if d.get("state") == state]


def sort_by_date(data: List[Dict[str, str]], order: str = "True") -> List[Dict[str, str]]:
    """Функция сортирует список словарей по значению ключа "date"."""
    reverse_order = True if order == "True" else False
    return sorted(data, key=lambda x: x["date"], reverse=reverse_order)
