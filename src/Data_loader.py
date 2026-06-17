import csv


def load_transactions(file_path):
    data = []
    with open(file_path, newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data

def market_indexes(file_path):
    prices = {}

    with open(file_path, newline='\n') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            prices[row["ticker"]] = float(row["current_price"])

    return prices