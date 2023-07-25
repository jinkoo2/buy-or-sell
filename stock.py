

def save_dict_as_json(data, filepath):
    import json
    with open(filepath, 'w') as json_file:
        json.dump(data, json_file)

def get_ticker_list_from_nasdaq_screener_file(csv_file):
    import pandas as pd
    data = pd.read_csv(csv_file)
    return [ str for str in data['Symbol'].astype(str) if '^' not in str and '/' not in str]
