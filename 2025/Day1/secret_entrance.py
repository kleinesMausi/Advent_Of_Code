from pathlib import Path

folder_path = Path(__file__).parent

big_data_set = folder_path / "big_data.txt"
small_data_set = folder_path / "small_data.txt"

def get_and_parse_data(data_path):
    with open(data_path, "r") as f:
        instructions = f.read()

    return instructions.strip().split("\n")

#------------Part One------------#

def rotate(start = 50):
    zeros_seen = 0
    instructions = get_and_parse_data(big_data_set)
    pos = start
    
    for instruction in instructions:
        direction = 1 if instruction[0] == "R" else -1
        distance = direction * int(instruction[1:])

        pos = (pos + distance) % 100
        # print(f"Instruction: {instruction}\nDistance: {distance}\nCurrent Value: {pos}\n========================")
        if pos == 0:
            zeros_seen += 1

    return zeros_seen

# print(rotate(orders))

#------------Part Two------------#

def rotate_count_steps(start = 50):
    zeros_seen = 0
    instructions = get_and_parse_data(big_data_set)
    pos = start
    for instruction in instructions:

        direction = 1 if instruction[0] == "R" else -1
        distance = int(instruction[1:])

        for _ in range(abs(distance)):
            pos = (pos + direction) % 100
            if pos == 0:
                zeros_seen += 1

    return zeros_seen

print(f"Solution 1: {rotate()}")
print(f"Solution 2: {rotate_count_steps()}")