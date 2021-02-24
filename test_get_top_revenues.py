"""
Testing get_top_revenues()
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


class TestRevenue(unittest.TestCase):
    """
    Testing get_top_budget() function with 3 test cases.
    """
    def test_full_data(self):
        """
        Test Case 1 using TMDB_10000_Popular_Movies.csv with all of database.
        """
        input1 = 'TMDB_10000_Popular_Movies.csv'
        actual_result = DevStats.get_top_revenues(input1)
        expected_result = [
            ('Avengers: Endgame', 2797800564),
            ('Avatar', 2787965087),
            ('Star Wars: The Force Awakens', 2068223624),
            ('Avengers: Infinity War', 2046239637),
            ('Titanic', 1845034188)]
        self.assertEqual(actual_result, expected_result)

    def test_20_lines(self):
        """
        Test Case 2 using dataset_20_lines.csv with all of database.
        """
        input1 = 'dataset_20_lines.csv'
        actual_result = DevStats.get_top_revenues(input1)
        expected_result = [
            ('Star Wars: The Rise of Skywalker', 1073604458),
            ('The Twilight Saga: Eclipse', 698491347),
            ('Ant-Man', 519311965),
            ('Live Free or Die Hard', 383531464),
            ('Jumanji: The Next Level', 310830000)]
        self.assertEqual(actual_result, expected_result)

    def test_empty_file(self):
        """
        Test Case 3 using empty.csv with all of database.
        """
        input1 = 'empty.csv'
        actual_result = DevStats.get_top_revenues(input1)
        expected_result = []
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
