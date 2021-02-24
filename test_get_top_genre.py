"""
Testing get_top_genres()
Amir Rahimov
Reviewer: Chris Puzzo
December 21, 2020
Comp525
"""
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(".."))
from mycode.transform import DevStats


class TestBudget(unittest.TestCase):
    """
    Testing get_top_genre() function with 3 test cases.
    """
    def test_action_genre(self):
        """
        Test Case 1 using TMDB_10000_Popular_Movies.csv with all of database
            for action genre.
        """
        input1 = 'TMDB_10000_Popular_Movies.csv'
        genre = 'Action'
        actual_result = DevStats.get_top_genre(genre, input1)
        expected_result = 'Bad Boys for Life'
        self.assertEqual(actual_result, expected_result)

    def test_horror_genre(self):
        """
        Test Case 2 using TMDB_10000_Popular_Movies.csv with all of database
            for horror genre.
        """
        input1 = 'TMDB_10000_Popular_Movies.csv'
        genre = 'Horror'
        actual_result = DevStats.get_top_genre(genre, input1)
        expected_result = 'Underwater'
        self.assertEqual(actual_result, expected_result)

    def test_empty_file(self):
        """
        Test Case 3 using empty.csv with all of database.
        """
        input1 = 'empty.csv'
        actual_result = DevStats.get_top_genre('Action', input1)
        expected_result = None
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
