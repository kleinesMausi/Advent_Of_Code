from pathlib import Path

folder_path = Path(__file__).parent

big_data_set = folder_path / "big_data.txt"
small_data_set = folder_path / "small_data.txt"

data_path = big_data_set

def mult(arr):
    total = 1
    for num in arr:
        total *= num
    return total

def get_and_parse_data(data_path):
    with open(data_path, "r") as f:
        grid = f.read()

    return grid.strip().split("\n")


#------------Part One------------#
def solve_math_problem_1(data_path):
    rows_blueprint = get_and_parse_data(data_path)
    rows = [row.split() for row in rows_blueprint]
    total = 0
    

    for col_idx in range(len(rows[0])):
        operator = rows[-1][col_idx]
        numbers = [int(rows[row_idx][col_idx]) for row_idx in range(len(rows)-1)]
        
        if operator == "+":
            result = sum(numbers)
        else:  
            result = 1
            for num in numbers:
                result *= num
        
        total += result
    
    return total


#------------Part Two------------#

def solve_math_problem_2(data_path):
    rows = get_and_parse_data(data_path)
    
    # last row just seems to loose 2 whitspaces?
    rows[-1] += "  "
    number_string = ""
    numbers = []
    col_idx = len(rows[0]) - 1
    total = 0

    while col_idx >= 0:

        for j in range(len(rows) - 1):
            char = rows[j][col_idx]
            if char != " ":
                number_string += char

        if number_string:
            numbers.append(int(number_string))
            number_string = ""

        operator = rows[-1][col_idx]

        if operator != " ":
            total += sum(numbers) if operator == "+" else mult(numbers)
            numbers = []
        col_idx -= 1

    return total






print(f"Solution 1: {solve_math_problem_1(data_path)}")
print(f"Solution 2: {solve_math_problem_2(data_path)}")