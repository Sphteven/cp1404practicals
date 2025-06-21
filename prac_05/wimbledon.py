"""
Wimbledon
Estimate: 70 minutes
Actual:   60 minutes

"""

FILENAME = "wimbledon.csv"
records = []
champions = []

with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
    in_file.readline()
    for line in in_file:
        records.append(line.strip("\n").split(","))
champions_to_wins = {}
countries = []
for record in records:
    if record[2] not in champions:
        champions.append(record[2])
    if record[1] not in countries:
        countries.append(record[1])
countries.sort()
for champion in champions:
    total_wins = 0
    for record in records:
        if record[2] == champion:
            total_wins += 1
    champions_to_wins[champion] = total_wins
