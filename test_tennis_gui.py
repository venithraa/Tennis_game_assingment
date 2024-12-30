import unittest
from tkinter import Tk
from tennis_game import TennisGameGUI 
from unittest.mock import patch

class TestTennisGameGUI(unittest.TestCase):
    def setUp(self):
        # Create the Tk root and TennisGameGUI instance
        self.root = Tk()
        self.app = TennisGameGUI(self.root)

    def tearDown(self):
        # Destroy the Tk root after each test
        self.root.destroy()

    def test_display_score_regular(self):
        # Test regular scoring
        self.assertEqual(self.app.display_score(0, 0), "Love-Love")
        self.assertEqual(self.app.display_score(1, 2), "Fifteen-Thirty")
        self.assertEqual(self.app.display_score(2, 3), "Thirty-Forty")
        self.assertEqual(self.app.display_score(3, 2), "Forty-Thirty")

    def test_display_score_deuce(self):
        # Test deuce scenario
        self.assertEqual(self.app.display_score(3, 3), "Deuce")
        self.assertEqual(self.app.display_score(8, 8), "Deuce")

    def test_display_score_advantage(self):
        # Test advantage scenario
        self.assertEqual(self.app.display_score(4, 3), "Advantage for Player 1")
        self.assertEqual(self.app.display_score(3, 4), "Advantage for Player 2")
        self.assertEqual(self.app.display_score(10, 9), "Advantage for Player 1")

    def test_display_score_win(self):
        # Test win scenario
        self.assertEqual(self.app.display_score(4, 2), "Win for Player 1")
        self.assertEqual(self.app.display_score(2, 4), "Win for Player 2")
        self.assertEqual(self.app.display_score(10, 8), "Win for Player 1")

    def test_negative_input(self):
    # Test negative input in calculate_score method
        self.app.player1_score.insert(0, "-1")
        self.app.player2_score.insert(0, "3")
        with patch('tkinter.messagebox.showerror') as mock_showerror:
            self.app.calculate_score()
            mock_showerror.assert_called_with("Invalid Input", "Scores cannot be negative. Please enter valid non-negative integers.")

    def test_invalid_input(self):
    # Test invalid input like letters
        self.app.player1_score.insert(0, "abc")
        self.app.player2_score.insert(0, "2")
        with patch('tkinter.messagebox.showerror') as mock_showerror:
            self.app.calculate_score()
            mock_showerror.assert_called_with("Invalid Input", "Please enter valid integers for both scores.")


    def test_refresh_inputs(self):
        # Test the refresh_inputs method
        self.app.player1_score.insert(0, "3")
        self.app.player2_score.insert(0, "2")
        self.app.refresh_inputs()
        self.assertEqual(self.app.player1_score.get(), "")
        self.assertEqual(self.app.player2_score.get(), "")
        self.assertEqual(self.app.result_label.cget("text"), "Result: ")

if __name__ == "__main__":
    unittest.main()
