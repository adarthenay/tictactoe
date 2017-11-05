import unittest
from src.board import Board

class PlayerTestCase(object):
    def test_range(self):
        turn = self.player.play(Board( "000 000 000" ))
        self.assertIsInstance(turn, tuple)
        self.assertEqual(len(turn), 2)
        self.assertIn(turn[0], range(3))
        self.assertIn(turn[1], range(3))

        turn = self.player.play(Board(" 201 021 010 "))
        self.assertIsInstance(turn, tuple)
        self.assertEqual(len(turn), 2)
        self.assertIn(turn[0], range(3))
        self.assertIn(turn[1], range(3))

        turn = self.player.play(Board(" 020 020 002 "))
        self.assertIsInstance(turn, tuple)
        self.assertEqual(len(turn), 2)
        self.assertIn(turn[0], range(3))
        self.assertIn(turn[1], range(3))

        turn = self.player.play(Board( "010 210 201" ))
        self.assertIsInstance(turn, tuple)
        self.assertEqual(len(turn), 2)
        self.assertIn(turn[0], range(3))
        self.assertIn(turn[1], range(3))

    def test_does_not_overwrite(self):
        turn = self.player.play(Board("000 010 000"))
        self.assertIsInstance(turn, tuple)
        self.assertEqual(len(turn), 2)
        self.assertIn(turn[0], range(3))
        self.assertIn(turn[1], range(3))
        self.assertNotEqual(turn, (1, 1))

        turn = self.player.play(Board("110 010 111"))
        self.assertIsInstance(turn, tuple)
        self.assertEqual(len(turn), 2)
        self.assertIn(turn[0], range(3))
        self.assertIn(turn[1], range(3))
        self.assertIn(turn, [(0, 2), (1, 0), (1, 2)])

        turn = self.player.play(Board("111 111 101"))
        self.assertIsInstance(turn, tuple)
        self.assertEqual(len(turn), 2)
        self.assertIn(turn[0], range(3))
        self.assertIn(turn[1], range(3))
        self.assertEqual(turn, (2, 1))
