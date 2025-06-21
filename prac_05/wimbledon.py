"""
Wimbledon
Estimate: 70 minutes
Actual:   60 minutes

"""


def main():
    FILENAME = "wimbledon.csv"
    records = []
    champions = []
    countries = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            records.append(line.strip("\n").split(","))
    champions_to_wins = {}
    champions = extract_record(champions, records,2)
    countries = extract_record(countries, records,1)
    countries.sort()
    for champion in champions:
        total_wins = 0
        for record in records:
            if record[2] == champion:
                total_wins += 1
        champions_to_wins[champion] = total_wins


def extract_record(list_of_items, records, i):
    for record in records:
        if record[i] not in list_of_items:
            list_of_items.append(record[i])
    return list_of_items

main()