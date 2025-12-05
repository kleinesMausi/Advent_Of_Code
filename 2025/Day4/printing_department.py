from pathlib import Path

folder_path = Path(__file__).parent

big_data_set = folder_path / "big_data.txt"
small_data_set = folder_path / "small_data.txt"

def get_and_parse_data(data_path):
    with open(data_path, "r") as f:
        grid = f.read()

    return grid.strip().split("\n")


#------------Part One------------#

def can_forklift_access(grid, target_row, target_col):
    grid_rows = len(grid)
    grid_cols = len(grid[0])
    adjacent_paper_rolls = 0
    
    neighbor_offsets = [
        (-1, -1), (-1, 0), (-1, 1),  # top left,    top,        top right
        (0, -1),           (0, 1),   # left,                    right
        (1, -1),  (1, 0),  (1, 1)    # bottom left, bottom,     bottom right
    ]
    
    for row_offset, col_offset in neighbor_offsets:
        neighbor_row = target_row + row_offset
        neighbor_col = target_col + col_offset
        
        if 0 <= neighbor_row < grid_rows and 0 <= neighbor_col < grid_cols:
            if grid[neighbor_row][neighbor_col] == "@":
                adjacent_paper_rolls += 1
                
        if adjacent_paper_rolls >= 4:
            return False
    
    return True

def access_paper_1():
    grid = get_and_parse_data(big_data_set)
    accessible_count = 0
    
    for row_index, grid_row in enumerate(grid):
        for col_index, cell_content in enumerate(grid_row):
            if cell_content == "@":
                if can_forklift_access(grid, row_index, col_index):
                    accessible_count += 1
                
    return accessible_count


#------------Part Two------------#

def access_paper_2():
    grid_immutable =get_and_parse_data(big_data_set)
    grid = [list(row) for row in grid_immutable]
    total_removed = 0
    
    while True:
        removable_positions = []
        
        for row_index in range(len(grid)):
            for col_index in range(len(grid[0])):
                if grid[row_index][col_index] == "@":
                    if can_forklift_access(grid, row_index, col_index):
                        removable_positions.append((row_index, col_index))
        
        if not removable_positions:
            break
            
        for row, col in removable_positions:
            grid[row][col] = "."
            total_removed += 1
    
    return total_removed


print(f"Solution 1: {access_paper_1()}")
print(f"Solution 2: {access_paper_2()}")