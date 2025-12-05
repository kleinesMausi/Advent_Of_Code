from pathlib import Path

folder_path = Path(__file__).parent

big_data_set = folder_path / "big_data.txt"
small_data_set = folder_path / "small_data.txt"

def get_and_parse_data(data_path):
    with open(data_path, "r") as f:
        ids = f.read()

    return [pair.split("-") for pair in ids.split(",")]

#------------Part One------------#

def check_id_1():
    ids_seperated = get_and_parse_data(big_data_set)
    total = 0
    for start, end in ids_seperated:
        for id in range(int(start), int(end) + 1):
            id_str = str(id)
            length = len(id_str)
            if id_str[length//2:] == id_str[:length//2]:
                total += id
    return total

#------------Part Two------------#


def is_invalid_repetition(id):
    length = len(id)
    for window_size in range(1, length):
        if length % window_size == 0:                 
            repeats = length // window_size
            if repeats >= 2:           
                pattern = id[:window_size]
                if pattern * repeats == id:
                    return True
    
    return False

def check_id_2():
    ids_seperated = get_and_parse_data(big_data_set)
    total = 0

    for start, end in ids_seperated:
        for id in range(int(start), int(end) + 1):
            if is_invalid_repetition(str(id)):
                total += id

    return total


print(f"Solution 1: {check_id_1()}")
print(f"Solution 2: {check_id_2()}")