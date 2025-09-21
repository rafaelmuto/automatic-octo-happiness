from rest_framework import serializers
from .models import Sudoku

class SudokuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sudoku
        fields = ['id', 'puzzle', 'difficulty', 'created_at', 'updated_at', 'created_by']
        read_only_fields = ['id', 'created_at', 'updated_at', 'created_by']

    def validate_puzzle(self, value):
        if len(value) != 81:
            raise serializers.ValidationError("Puzzle must be 81 characters long")
        return value
    
    def validate_difficulty(self, value):
        if value not in ['easy', 'medium', 'hard', 'expert']:
            raise serializers.ValidationError("Invalid difficulty")
        return value