"""
Final Project code
Amir Rahimov
Comp525
Dec 21, 2020
"""
import csv
import datetime
from collections import Counter
time_now = datetime.datetime.now()


class DevStats():
    """
    Find the requested information based on the functions from the TMDB
        database. It's purpose is to refer to the functions from the testing
        modules
    """
    @staticmethod
    def top_five_movies(filename):
        """
        Finds the top 5 popular movies for the past 10 years
        by popularity rating.
        Input: location of the csv file containing the dataset.
        Return: Dictionary histogram
        Keys: movie names
        Values:  popularity ratings.
        """
        data_structure = {}
        top_popularity = [0.0, 0.0, 0.0, 0.0, 0.0]
        top_title = ['', '', '', '', '']
        idx = 0
        date_rel_year = 0
        with open(filename, 'r', encoding='utf-8') as csvfile:
            # creating a csv reader object
            reader = csv.reader(csvfile)
            for aline in reader:
                title = aline[2]
                popularity = aline[15]
                if aline[9] != '' and aline[9] != 'Release_Date':
                    if '-' in aline[9][-4:]:
                        date_rel_year = int(aline[9][-2:]) + 2000
                    else:
                        date_rel_year = int(aline[9][-4:])
                if title != 'Title' and date_rel_year >= time_now.year - 10:
                    # Check if the new popularity is greater than the
                    # 1st top so far
                    if float(popularity) > top_popularity[0]:
                        # Move the top 4 down one position so we
                        # can insert the new top popularity
                        top_popularity[4] = top_popularity[3]
                        top_title[4] = top_title[3]
                        top_popularity[3] = top_popularity[2]
                        top_title[3] = top_title[2]
                        top_popularity[2] = top_popularity[1]
                        top_title[2] = top_title[1]
                        top_popularity[1] = top_popularity[0]
                        top_title[1] = top_title[0]
                        # Insert the new top popularity
                        top_popularity[0] = float(popularity)
                        top_title[0] = title
                    # Otherwise, check if the new popularity is greater
                    # than the 2nd top one
                    elif float(popularity) > top_popularity[1]:
                        # Move the top 3 down one position
                        top_popularity[4] = top_popularity[3]
                        top_title[4] = top_title[3]
                        top_popularity[3] = top_popularity[2]
                        top_title[3] = top_title[2]
                        top_popularity[2] = top_popularity[1]
                        top_title[2] = top_title[1]
                        # Insert the new 2nd popularity
                        top_popularity[1] = float(popularity)
                        top_title[1] = title
                    elif float(popularity) > top_popularity[2]:
                        top_popularity[4] = top_popularity[3]
                        top_title[4] = top_title[3]
                        top_popularity[3] = top_popularity[2]
                        top_title[3] = top_title[2]
                        top_popularity[2] = float(popularity)
                        top_title[2] = title
                    elif float(popularity) > top_popularity[3]:
                        top_popularity[4] = top_popularity[3]
                        top_title[4] = top_title[3]
                        top_popularity[3] = float(popularity)
                        top_title[3] = title
                    elif float(popularity) > top_popularity[4]:
                        top_popularity[4] = float(popularity)
                        top_title[4] = title
                    # construct a data_structure with top 5 titles
                    # and popularity
            for title in top_title:
                data_structure[title] = top_popularity[idx]
                idx += 1
        csvfile.close()
        return data_structure

    @staticmethod
    def get_top_budget(filename):
        """
        Finds the top 5  movies of all time by budget
        Input: would be a location and the name of the csv file containing the
            dataset.
        Return: List of tuples. Each tuple has the title and the revenue value
        """
        all_movie_budgets = {}
        with open(filename, 'r', encoding='utf-8') as csvfile:
            # creating a csv reader object
            reader = csv.reader(csvfile)
            for aline in reader:
                title = aline[2]
                budget = aline[-2]
                if title != 'Title' and budget != 'Budget' and budget != '':
                    all_movie_budgets[title] = int(budget)
            sorted_dict = Counter(all_movie_budgets)
            top_movie_budgets = sorted_dict.most_common(5)
            return top_movie_budgets

    @staticmethod
    def get_top_revenues(filename):
        """
        Finds the top 5  movies of all time by revenue.
        Input: would be a location and the name of the csv file containing the
            dataset.
        Return: List of tuples. Each tuple has the title and the revenue value
        """
        all_movie_revenues = {}
        with open(filename, 'r', encoding='utf-8') as csvfile:
            # creating a csv reader object
            reader = csv.reader(csvfile)
            for aline in reader:
                title = aline[2]
                revenue = aline[-1]
                if title != 'Title' and revenue != 'Revenue' and revenue != '':
                    all_movie_revenues[title] = int(revenue)
            sorted_dict = Counter(all_movie_revenues)
            top_movie_revenues = sorted_dict.most_common(5)
            return top_movie_revenues

    @staticmethod
    def get_top_genre(genre_submitted, filename):
        """
        Finds the top movie of the genre of all time by popularity.
        Input: The string containing the genre wanted and the location with the
            name of the csv file containing the
                dataset.
        Return: List of tuples. Each tuple has the title and the revenue value
        """
        try:
            genre_d = {}
            with open(filename, 'r', encoding='utf-8') as csvfile:
                # creating a csv reader object
                reader = csv.reader(csvfile)
                for aline in reader:
                    title = aline[2]
                    genre = aline[5]
                    popularity = aline[15]
                    if genre != 'Genres' and genre_submitted in genre:
                        genre_d[title] = float(popularity)
                top_genre = max(genre_d, key=genre_d.get)
            return top_genre
        except:
            None
