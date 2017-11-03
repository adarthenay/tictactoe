import unittest
from src.board import Board
 
class TestBoard(unittest.TestCase):
    def test_is_empty(self):
        self.assertTrue(Board().is_empty())
        self.assertFalse(Board("000 010 000").is_empty())
        
        
    def test_grid(self):
        self.assertEqual(Board().grid, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.assertEqual(Board("000 010 000").grid, [[0, 0, 0], [0, 1, 0], [0, 0, 0]])
        self.assertEqual(Board("""
            201
            112
            212""").grid, [[2, 0, 1], [1, 1, 2], [2, 1, 2]])
            
    def test_has_a_winner(self):
        self.assertEqual(Board().winner(), 0)
        self.assertEqual(Board("""
            111
            022
            200""").winner(), 1)
        self.assertEqual(Board("""
            011
            001
            222""").winner(), 2)
        self.assertEqual(Board("""
            110
            122
            100""").winner(), 1)
        self.assertEqual(Board("""
            012
            021
            202""").winner(), 2)
        self.assertEqual(Board("""
            112
            011
            201""").winner(), 1)
        
if __name__ == '__main__':
    unittest.main()