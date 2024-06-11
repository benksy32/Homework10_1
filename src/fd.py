def filter_by_state(data, state='EXECUTED'):
    return [d for d in data if d.get('state') == state]

def sort_by_date(data, order='descending'):
    reverse_order = True if order == 'descending' else False
    return sorted(data, key=lambda x: x['date'], reverse=reverse_order)
