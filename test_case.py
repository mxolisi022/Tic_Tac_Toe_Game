
import unittest
from unittest.mock import patch
from io import StringIO


from game import print_board, check_winner, tic_tac_toe

class TestTicTacToe(unittest.TestCase):
    
    def test_check_winner_rows(self):
        board = [["X", "X", "X"],
                 [" ", " ", " "],
                 [" ", " ", " "]]
        self.assertTrue(check_winner(board, "X"))
        

        board = [[" ", " ", " "],
                 ["O", "O", "O"],
                 [" ", " ", " "]]
        self.assertTrue(check_winner(board, "O"))
        

    def test_check_winner_columns(self):
        board = [["X", " ", " "],
                 ["X", " ", " "],
                 ["X", " ", " "]]
        self.assertTrue(check_winner(board, "X"))

        board = [[" ", "O", " "],
                 [" ", "O", " "],
                 [" ", "O", " "]]
        self.assertTrue(check_winner(board, "O"))
        

    def test_check_winner_diagonals(self):
        board = [["X", " ", " "],
                 [" ", "X", " "],
                 [" ", " ", "X"]]
        self.assertTrue(check_winner(board, "X"))

        board = [[" ", " ", "O"],
                 [" ", "O", " "],
                 ["O", " ", " "]]
        self.assertTrue(check_winner(board, "O"))
        

    def test_no_winner(self):
        board = [["X", "O", "X"],
                 ["X", "O", "O"],
                 ["O", "X", "X"]]
        self.assertFalse(check_winner(board, "X"))
        self.assertFalse(check_winner(board, "O"))
        
        
    def test_print_board(self):       # Redirect stdout to capture printed output
        captured_output = StringIO()
        expected_output = "  |   |  \n---------\n  |   |  \n---------\n  |   |  \n---------\n"
        with patch('sys.stdout', new=captured_output):
            print_board([[" "]*3 for _ in range(3)])
        self.assertEqual(captured_output.getvalue(), expected_output)
        
        
    @patch('builtins.input', side_effect=['1', '1', '2', '2', '3', '3', '1', '2', '3', 
                                          '1', '2', '3', '1', '2', '3', '1', '2', '3'])
    def test_tic_tac_toe_game(self, mock_input):      # Redirect stdout to capture printed output
        
        captured_output = StringIO()
        expected_output = "Welcome to Tic-Tac-Toe!\n  |   |  \n---------\n  |   |  \n---------\n  |   |  \n---------\nPlayer X's turn\n  |   |  \n---------\nX |   |  \n---------\n  |   |  \n---------\nPlayer O's turn\n  |   |  \n---------\nX |   |  \n---------\n  | O |  \n---------\nPlayer X's turn\nX |   |  \n---------\nX |   |  \n---------\n  | O |  \n---------\nPlayer O's turn\nX |   |  \n---------\nX |   |  \n---------\nO | O |  \n---------\nPlayer X's turn\nX | X |  \n---------\nX |   |  \n---------\nO | O |  \n---------\nPlayer O's turn\nX | X |  \n---------\nX |   |  \n---------\nO | O |  \n---------\nPlayer X's turn\nX | X | X\n---------\nX |   |  \n---------\nO | O |  \n---------\nPlayer X wins!\n"

        with patch('sys.stdout', new=captured_output):
            tic_tac_toe()
        self.assertEqual(captured_output.getvalue(), expected_output)
        

if __name__ == '__main__':
    unittest.main()