"""
Wimbledon
Estimate: 70 minutes
Actual:   84 minutes

"""


def main():
    FILENAME = "wimbledon.csv"
    records = create_records(FILENAME)
    champions_to_wins = {}
    champions = extract_record(records, 2)
    countries = extract_record(records, 1)
    countries.sort()
    count_champion_wins(champions, champions_to_wins, records)
    print_wimbledon_champs(champions_to_wins)
    winning_countries = ", ".join(countries)
    print(f"These {len(countries)} countries have won Wimbledon:\n"
          f"{winning_countries}")


def print_wimbledon_champs(champions_to_wins):
    """Print all champions and wins"""
    print("Wimbledon Champions:")
    for champion, wins in champions_to_wins.items():
        print(champion, wins)


def count_champion_wins(champions, champions_to_wins, records):
    """Count number of wins for each champions"""
    for champion in champions:
        total_wins = 0
        for record in records:
            if record[2] == champion:
                total_wins += 1
        champions_to_wins[champion] = total_wins


def create_records(FILENAME):
    """Create records from file and returns as list of list"""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            records.append(line.strip("\n").split(","))
    return records


def extract_record(records, i):
    """Extract data from records and returns as list"""
    list_of_items = []
    for record in records:
        if record[i] not in list_of_items:
            list_of_items.append(record[i])
    return list_of_items


main()
