from pathlib import Path

folder_path = Path(__file__).parent

big_data_set = folder_path / "big_data.txt"
small_data_set = folder_path / "small_data.txt"


def get_and_parse_data(data_path):
    ranges = []
    ids = []

    with open(data_path, "r") as f:
        ranges_text, ids_text = f.read().split("\n\n")

    for id_range in ranges_text.strip().split("\n"):
        start, end = map(int, id_range.split("-"))
        ranges.append((start, end))

    for id in ids_text.strip().split("\n"):
        ids.append(int(id))

    return ranges, ids


#------------Part One------------#

def count_fresh_ingredients():
    ranges, ids = get_and_parse_data(big_data_set)
    fresh_count = 0

    for ingredient_id in ids:
        for start, end in ranges:
            if start <= ingredient_id <= end:
                fresh_count += 1
                break
                
    return fresh_count



#------------Part Two------------#

def count_all_fresh_ingredients():
    ranges, _ = get_and_parse_data(big_data_set)
    ranges.sort(key=lambda x: x[0])
    
    merged = []
    for start, end in ranges:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    
    total = sum((end - start + 1) for start, end in merged)
    return total

print(f"Solution 1: {count_fresh_ingredients()}")
print(f"Solution 2: {count_all_fresh_ingredients()}")