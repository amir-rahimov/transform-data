### Credits
- Kaggle TMDb Datasets
- Amir Rahimov
- Chris Puzzo(Code Reviewer)

## TBMD Popular Movies Project
The TBMD Popular Movies Project consumes a csv dataset to get the filtered
information we need. The dataset has 10,000 most popular movies across the
globe collected from the TBMD database and assembled by Kaggle.
By interpreting the data collected from the dataset, we
hope to find these answers.

## Objectives
1. Find the top 5 movies in the past 10 years by popularity.
2. We also want to find the top 5 movies by budget of all time.
3. We also want to find the top 5 movies by revenue of all time.
4. Find the requested top movie of the genre of all time.


### Packages
- csv module
- datetime module
- collections module
- inittest module
- os and sys module - transport the driver functions into the testing folder

## Driver Functions
##### top_five_movies()
##### get_top_budget()
##### get_top_revenues()
##### get_top_genre()

## Running the Program
The program is run from bash using the command python `filename`. The file
we run is the testing file for each function we developed from the tests folder
You need the unittest module for the testing file and the python program. No
other packages are necessary.

## Evaluations:
### What Works and Scope Assumptions 	
Each objective works as intended. The get_top_genre() function can even take
in any genre in string form as an argument and return the requested genre's
top movie by popularity of all time. The program could only work on this
specific dataset, unless the other dataset has the same purpose and
header columns
### Immediate Further Development
The project could analyze the relation between the budget cost and revenue of
the movie and come to the appropriate conclusion.

### class DevStats():
```
    """
    Find the requested information based on the functions from the TMDB
        database. It's purpose is to refer to the functions from the testing
        modules
    """
```

### def top_five_movies(filename):
```
@staticmethod
def top_five_movies(filename):
    """
    Finds the top 5 popular movies for the past 10 years by popularity rating.
    Input: would be a location and the name of the csv file containing the
        dataset.
    Return: Dictionary
        Keys: string movie name
        Values: integers popularity rating
    """
```
* import csv module to read the excel database file.
* Import datetime module to get the current year for the function
* Create a dictionary as a `data_structure` with an empty variable to store
    that organizes titles by popularity.
* Create a list `top_popularity` with the lowest floats with 5 values to store
    out popularity scores.
* Create another list `top_title` to store all the top 5 movie names and
    Initialize it with 5 empty strings.
* create a variable `idx` and initialize it with 0 to eventually use it
    as a counter for index.
* create a variable `date_released_year` and initialize it to 0 to have it
    as an integer.
* We open the `filename` containing the csv as a `csvfile`. We make sure that
    it uses the `utf-8` encoding to ignore special characters.
* We use the csv module method `csv.reader()` to read the `csv_file` and
    name the variable `reader`
* Next, we iterate through `aline` in `reader` to get the value in each line.
    * to find the `title` we find the index position in the database and
        put it as an index of `aline` in index 2.
    * to find the `popularity` we find the index position in the database
        and put it as an index of `aline` in index 15.
    * for the `date_rel_year`, we want to make sure the value doesnt
        have any empty strings or have the top title string -  `Release_Date`.
            * We check if there is a '-' in the line to make sure we don't
                get the error and to the last 2 digits of the year we add 2000    
            * Else we initialize the variable `date_rel_year` with the 9th
                index, but take only the last four digits using index to get
                    only the year.
    * Next, we check that `title` variable doesn't have a string `Title`,
        and variable `date_rel_year` is greater than or equal to the
            current year `now.year` minus 10, to get the last 10 years
                from the database.
    *  Check if the new `popularity` is greater than the 1st
        `top_popularity` list so far.
    * Then we move the top 4 down one position so we can insert the new rating
        from the database to our `top_popularity` list until the largest
            number is at the front index 0. We do the same thing with the
                `top_title`: update it via the index.
    * If the `popularity` value is higher that the second highest value in
        `top_popularity`, we replace it with the new value of `popularity`.
            It goes until the 5th element in the list.
* Now, we construct a data_structure with top 5 `titles` and `popularity`
* Loop through the `titles` in the list `top_title` to get the top movie names.
    * we add the `title` to the `data_structure` as a key. And the
        `top_popularity` as a value with an index of `idx` as a counter.
    * We add 1 to `idx` each time we loop for the counter.

* we close the csv after we are done using `.close` method.
* We return the `data_structure` to get the movie title and its popularity.


### def get_top_revenues(filename):
```
@staticmethod
def get_top_revenues(filename):
    """
    Finds the top 5  movies of all time by revenue.
    Input: would be a location and the name of the csv file containing the
        dataset.
    Return: List of tuples. Each tuple has the title and the revenue value
    """
```
*  Import counter function from collections to sort the dictionary by its
    value.
* Create an empty dictionary called `all_movie_revenues` to store all the
    titles and budgets.
* We open the `filename` containing the csv as a `csvfile`. We make sure that
    it uses the `utf-8` encoding to ignore special characters.
* We use the csv module method `csv.reader()` to read the `csv_file` and
    name the variable `reader`
* Next, we iterate through `aline` in `reader` to get the value in each line.
    * to find the `title` we find the index position in the database and
        put it as an index of `aline` in index 2.
    * to find the `Budget` we find the index position in the database
        and put it as an index of `aline` in index -2.
    * Next, we check that `title` variable doesn't have a string `'Title'`,
        and the `revenue` variable doesn't have a string `'Revenue'` or have
            an empty string.
        * We add the title as key to the dict `all_movie_revenues`
            and the `revenue` as an integer value.
    * We then use `counter` on the `all_movie_revenues` to create a container
        that holds the dictionary and put it in a variable `sorted_dict`.
    * We then use the `most_common()` function of counter to get the top
        5 from the `sorted_dict` and put into a variable `top_movie_revenues`.
    * Finally we return the `top_movie_revenues` dictionary to have our output.


### def get_top_genre(genre_submitted, filename):
```
@staticmethod
def get_top_genre(genre_submitted, filename):
    """
    Finds the top movie of the genre of all time by popularity.
    Input: The string containing the genre wanted and the location with the
        name of the csv file containing the
            dataset.
    Return: List of tuples. Each tuple has the title and the revenue value
    """
```
* Initiate an empty dictionary `genre_d` that would contain all titles and
    popularity of the genre.
* We use the `try` and `except` block to return none if the file is empty
* We open the `filename` containing the csv as a `csvfile`. We make sure that
    it uses the `utf-8` encoding to ignore special characters.
* We use the csv module method `csv.reader()` to read the `csv_file` and
    name the variable `reader`
* Next, we iterate through `aline` in `reader` to get the value in each line.
    * to find the `title` we find the index position in the database and
        put it as an index of `aline` in index 2.
    * to find the `genre` we find the index position in the database
        and put it as an index of `aline` in index 5.
    * to find the `popularity` we find the index position in the database
        and put it as an index of `aline` in index 15.
    * Next, we check that `title` variable doesn't have a string `'Title'`,
        and the `genre_submitted` argument is filtered in to have only the
            values of the genre we want.
        * We add the title as key to the dict `genre_d`and the
            `popularity` as an integer value.
* We then filter out the values of the `genre_d` to get the maximum popularity
    and put it into a new variable `top_genre`
