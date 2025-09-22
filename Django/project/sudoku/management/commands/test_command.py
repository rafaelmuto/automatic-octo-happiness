from django.core.management.base import BaseCommand
import pprint

class Command(BaseCommand):
    help = 'Test command help'

    def add_arguments(self, parser):
        parser.add_argument('arg_1', type=int, help='required integer argument')
        parser.add_argument('--arg_2', type=str, help='required string argument', default='default value')


    def handle(self, *args, **kwargs):
        self.stdout.write('Test command')

        self.stdout.write(f' Required Argument 1: {kwargs["arg_1"]}')
        self.stdout.write(f' Optional Argument 2: {kwargs["arg_2"]}')

        self.stdout.write(self.style.SUCCESS('SUCCESS'))
        self.stdout.write(self.style.ERROR('ERROR'))
        self.stdout.write(self.style.WARNING('WARNING'))
        self.stdout.write(self.style.NOTICE('NOTICE'))

        sudokuEx01 = [ # open
            [0, 0, 7, 0, 4, 0, 0, 0, 0],
            [3, 0, 5, 0, 0, 6, 0, 0, 7],
            [9, 2, 0, 7, 9, 0, 0, 1, 0],
            [0, 3, 0, 0, 2, 0, 0, 7, 4],
            [0, 0, 0, 0, 9, 0, 0, 0, 0],
            [5, 7, 0, 0, 6, 0, 0, 9, 0],
            [0, 1, 0, 0, 5, 9, 0, 6, 8],
            [6, 0, 0, 8, 0, 0, 1, 0, 3],
            [0, 0, 0, 0, 3, 0, 2, 0, 0]
            ]

        sudokuEx02 = [
            [0, 2, 0, 4, 5, 6, 7, 8, 9],
            [4, 5, 7, 0, 8, 0, 2, 3, 6],
            [6, 8, 9, 2, 3, 7, 0, 4, 0],
            [0, 0, 5, 3, 6, 2, 9, 7, 4],
            [2, 7, 4, 0, 9, 0, 6, 5, 3],
            [3, 9, 6, 5, 7, 4, 8, 0, 0],
            [0, 4, 0, 6, 1, 8, 3, 9, 7],
            [7, 6, 1, 0, 4, 0, 5, 2, 8],
            [9, 3, 8, 7, 2, 5, 0, 6, 0]
            ]

        sudokuEx03 = [
            [0, 2, 0, 4, 0, 6, 0, 0, 9],
            [4, 0, 7, 0, 8, 0, 2, 3, 6],
            [0, 8, 0, 2, 0, 7, 0, 4, 0],
            [0, 0, 0, 0, 0, 2, 0, 7, 0],
            [0, 0, 4, 0, 0, 0, 6, 5, 0],
            [3, 9, 0, 5, 0, 0, 0, 0, 0],
            [0, 0, 0, 6, 0, 8, 0, 9, 7],
            [7, 6, 1, 0, 4, 0, 5, 2, 8],
            [0, 3, 0, 7, 2, 5, 0, 6, 0]
            ]

        sudokuEx04 = [ # open
            [9, 0, 7, 0, 1, 0, 0, 4, 0],  
            [0, 8, 2, 0, 0, 4, 0, 0, 7],
            [1, 4, 0, 7, 3, 0, 0, 0, 0],
            [0, 0, 0, 4, 0, 7, 0, 0, 3],
            [0, 7, 0, 0, 0, 0, 0, 2, 0],
            [2, 0, 0, 5, 0, 9, 0, 0, 0],
            [0, 0, 0, 0, 4, 3, 0, 9, 8],
            [7, 0, 0, 6, 0, 0, 1, 3, 0],
            [0, 9, 0, 0, 7, 0, 6, 0, 2]
            ]

        sudokuEx05 = [
            [6, 0, 0, 7, 0, 0, 0, 0, 0],
            [0, 8, 0, 0, 6, 4, 0, 0, 5],
            [0, 0, 5, 0, 1, 8, 0, 0, 0],
            [2, 0, 4, 0, 7, 3, 5, 0, 8],
            [0, 6, 0, 8, 4, 9, 0, 3, 0],
            [7, 0, 8, 5, 2, 0, 4, 0, 1],
            [0, 0, 0, 4, 8, 0, 3, 0, 0],
            [1, 0, 0, 3, 5, 0, 0, 7, 0],
            [0, 0, 0, 0, 0, 7, 0, 0, 2]
            ]

        sudokuEx06 = [ # open
            [0, 0, 7, 0, 4, 0, 0, 0, 0],
            [3, 0, 5, 0, 0, 6, 0, 0, 7],
            [9, 2, 0, 7, 9, 0, 0, 1, 0],
            [0, 3, 0, 0, 2, 0, 0, 7, 4],
            [0, 0, 0, 0, 9, 0, 0, 0, 0],
            [5, 7, 0, 0, 6, 0, 0, 9, 0],
            [0, 1, 0, 0, 5, 9, 0, 6, 8],
            [6, 0, 0, 8, 0, 0, 1, 0, 3],
            [0, 0, 0, 0, 3, 0, 2, 0, 0]
            ]

        sudokuExs = [sudokuEx01, sudokuEx02, sudokuEx03, sudokuEx04, sudokuEx05, sudokuEx06]

        from sudoku.models import Sudoku

        for sudoku_grid in sudokuExs:
            pprint.pprint(Sudoku._stringfy_grid(sudoku_grid))


        