from ..models import Sudoku


def solve_sudoku(sudoku: Sudoku) -> Sudoku:
    """
    Solve a Sudoku puzzle using backtracking algorithm.
    
    Args:
        sudoku: Sudoku model instance with puzzle field containing the initial puzzle
        
    Returns:
        Sudoku model instance with solution field populated
    """
    # Convert puzzle string to 2D grid
    grid = sudoku.get_grid()
    
    # Create a copy to work with
    solution_grid = [row[:] for row in grid]
    
    # Try to solve the puzzle
    if _solve_grid(solution_grid):
        # Convert solution back to string and save
        solution_string = ''.join([''.join(row) for row in solution_grid])
        sudoku.solution = solution_string
        sudoku.save()
    else:
        # If no solution found, raise an exception
        raise ValueError("No solution exists for this Sudoku puzzle")
    
    return sudoku


def _solve_grid(grid):
    """
    Solve the Sudoku grid using backtracking algorithm.
    
    Args:
        grid: 2D list representing the 9x9 Sudoku grid
        
    Returns:
        bool: True if solution found, False otherwise
    """
    # Find empty cell
    empty_cell = _find_empty_cell(grid)
    
    # If no empty cell found, puzzle is solved
    if not empty_cell:
        return True
    
    row, col = empty_cell
    
    # Try numbers 1-9
    for num in range(1, 10):
        if _is_valid_move(grid, row, col, str(num)):
            # Place the number
            grid[row][col] = str(num)
            
            # Recursively try to solve the rest
            if _solve_grid(grid):
                return True
            
            # If this number doesn't lead to a solution, backtrack
            grid[row][col] = '0'  # Reset to empty
    
    return False


def _find_empty_cell(grid):
    """
    Find the first empty cell in the grid.
    
    Args:
        grid: 2D list representing the 9x9 Sudoku grid
        
    Returns:
        tuple: (row, col) of empty cell, or None if no empty cell found
    """
    for i in range(9):
        for j in range(9):
            if grid[i][j] == '0' or grid[i][j] == '.' or grid[i][j] == '':
                return (i, j)
    return None


def _is_valid_move(grid, row, col, num):
    """
    Check if placing a number at the given position is valid.
    
    Args:
        grid: 2D list representing the 9x9 Sudoku grid
        row: Row index
        col: Column index
        num: Number to place (as string)
        
    Returns:
        bool: True if move is valid, False otherwise
    """
    # Check row
    for j in range(9):
        if grid[row][j] == num and j != col:
            return False
    
    # Check column
    for i in range(9):
        if grid[i][col] == num and i != row:
            return False
    
    # Check 3x3 box
    box_start_row = (row // 3) * 3
    box_start_col = (col // 3) * 3
    
    for i in range(box_start_row, box_start_row + 3):
        for j in range(box_start_col, box_start_col + 3):
            if grid[i][j] == num and (i != row or j != col):
                return False
    
    return True


def is_valid_puzzle(puzzle_string):
    """
    Check if a puzzle string represents a valid Sudoku puzzle.
    
    Args:
        puzzle_string: 81-character string representing the puzzle
        
    Returns:
        bool: True if puzzle is valid, False otherwise
    """
    if len(puzzle_string) != 81:
        return False
    
    # Convert to grid
    grid = [[puzzle_string[i*9 + j] for j in range(9)] for i in range(9)]
    
    # Check if all given numbers are valid
    for i in range(9):
        for j in range(9):
            if grid[i][j] != '0' and grid[i][j] != '.' and grid[i][j] != '':
                if not _is_valid_move(grid, i, j, grid[i][j]):
                    return False
    
    return True


def get_difficulty_level(puzzle_string):
    """
    Estimate the difficulty level of a Sudoku puzzle based on the number of given clues.
    
    Args:
        puzzle_string: 81-character string representing the puzzle
        
    Returns:
        str: Difficulty level ('easy', 'medium', 'hard', 'expert')
    """
    given_clues = sum(1 for char in puzzle_string if char != '0' and char != '.' and char != '')
    
    if given_clues >= 46:
        return 'easy'
    elif given_clues >= 36:
        return 'medium'
    elif given_clues >= 28:
        return 'hard'
    else:
        return 'expert'
