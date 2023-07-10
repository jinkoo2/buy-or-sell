

def save_dict_as_json(data, filepath):
    import json
    with open(filepath, 'w') as json_file:
        json.dump(data, json_file)


def get_ticker_list():
    import pandas as pd
    csv_file = 'nasdaq_screener_1688487590280.csv'
    data = pd.read_csv(csv_file)

    return [ str for str in data['Symbol'].astype(str) if '^' not in str and '/' not in str]
