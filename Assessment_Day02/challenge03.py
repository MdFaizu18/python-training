# Filter odd IDs

player_id = [101, 102, 103, 104, 105]
odd_id = list(filter(lambda x: x % 2 != 0, player_id))
print(odd_id)