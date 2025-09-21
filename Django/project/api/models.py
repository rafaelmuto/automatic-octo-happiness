from django.db import models
from django.contrib.auth.models import User

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
        return [self.puzzle[i:i+9] for i in range(0, 81, 9)]
    
    def set_grid(self, grid):
        """Convert 9x9 grid to string representation"""
        self.puzzle = ''.join([''.join(row) for row in grid])
    