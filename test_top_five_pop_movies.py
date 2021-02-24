"""
Testing top_five_pop_movies()
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


class TestTMDB(unittest.TestCase):
    """
    Testing top_5_movies() function with 3 test cases.
    """
    def test_full_data(self):
        """
        Test Case 1 using TMDB_10000_Popular_Movies.csv with all of database.
        """
        input1 = 'TMDB_10000_Popular_Movies.csv'
        actual_result = DevStats.top_five_movies(input1)
        expected_result = {
            'Ad Astra': 463.487,
            'Bad Boys for Life': 255.068,
            'Bloodshot': 235.701,
            'Birds of Prey (and the Fantabulous Emancipation of One Harley Quinn)': 192.582,
            'Sonic the Hedgehog': 184.724
            }
        self.assertDictEqual(actual_result, expected_result)

    def test_20_lines(self):
        """
        Test Case 2 using empty.csv with all of database.
        """
        input1 = 'dataset_20_lines.csv'
        actual_result = DevStats.top_five_movies(input1)
        expected_result = {
            'Ad Astra': 463.487,
            'Bad Boys for Life': 255.068,
            'Bloodshot': 235.701,
            'Birds of Prey (and the Fantabulous Emancipation of One Harley Quinn)': 192.582,
            'Sonic the Hedgehog': 184.724
            }
        self.assertDictEqual(actual_result, expected_result)

    def test_empty_file(self):
        """
        Test Case 2 using empty.csv with all of database.
        """
        input1 = 'empty.csv'
        actual_result = DevStats.top_five_movies(input1)
        expected_result = {'': 0.0}
        self.assertDictEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
