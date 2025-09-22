from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

class Sudoku(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
        ('expert', 'Expert'),
    ]
    
    # Basic fields
    puzzle = models.CharField(max_length=81)  # 9x9 grid as string
    solution = models.CharField(max_length=81, null=True)  # Solved puzzle
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Optional: Link to user who created it
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']  # Newest first
        verbose_name = 'Sudoku Puzzle'
        verbose_name_plural = 'Sudoku Puzzles'
    
    def __str__(self):
        return f"Sudoku {self.id} - {self.difficulty.title()}"
    
    def get_grid(self):
        """Convert string representation to 9x9 grid"""
        return self._gridify_string(self.puzzle)
    
    def set_grid(self, grid):
        """Convert 9x9 grid to string representation"""
        self.puzzle = self._stringify_grid(grid)
    
    @staticmethod
    def _stringify_grid(grid: list) -> str:
        stringfied_grid = ''
        for row in grid:
            for cell in row:
                if type(cell) == int:
                    stringfied_grid += str(cell)
                else:
                    stringfied_grid += cell
        return stringfied_grid

    @staticmethod
    def _gridify_string(grid_string: str) -> list:
        list = []
        for i in range(9):
            row = []
            for j in range(9):
                row.append(grid_string[i*9 + j])
            list.append(row)
        return list

    def _is_valid_string(grid_string: str) -> bool:
        pattern = r'^[0-9]{81}$'
        return bool(re.match(pattern, grid_string))
            

    def _is_valid_grid(grid: list) -> bool:
        if len(grid) != 9:
            return False
        for row in grid:
            if len(row) != 9:
                return False
            for cell in row:
                if cell not in range(1, 10):
                    return False
        return True