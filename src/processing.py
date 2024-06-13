from typing import Dict, List


def filter_by_state(data: List[Dict[str, str]], state: str = "EXECUTED") -> List[Dict[str, str]]:
    return [d for d in data if d.get("state") == state]


def sort_by_date(data: List[Dict[str, str]], order: str = "descending") -> List[Dict[str, str]]:
    reverse_order = True if order == "descending" else False
    return sorted(data, key=lambda x: x["date"], reverse=reverse_order)
