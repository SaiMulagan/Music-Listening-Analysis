#!/usr/bin/env python
# coding: utf-8

# <div style="border:solid green 2px; padding: 20px">
#     
# <b>Hello Sai!</b> We're glad to see you in code-reviewer territory. You've done a great job on the project, but let's get to know each other and make it even better! We have our own atmosphere here and a few rules:
# 
# 
# 1. My name is Alexander Matveevsky. I work as a code reviewer, and my main goal is not to point out your mistakes, but to share my experience and help you become a data analyst.
# 2. We speak on a first-come-first-served basis.
# 3. if you want to write or ask a question, don't be shy. Just choose your color for your comment.  
# 4. this is a training project, you don't have to be afraid of making a mistake.  
# 5. You have an unlimited number of attempts to pass the project.  
# 6. Let's Go!
# 
# 
# ---
# I'll be color-coding comments, please don't delete them:
# 
# <div class="alert alert-block alert-danger">✍
#     
# 
# __Reviewer's comment №1__
# 
# Needs fixing. The block requires some corrections. Work can't be accepted with the red comments.
# </div>
#     
# ---
# 
# <div class="alert alert-block alert-warning">📝
#     
# 
# __Reviewer's comment №1__
# 
# 
# Remarks. Some recommendations.
# </div>
# 
# ---
# 
# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №1__
# 
# Success. Everything is done succesfully.
# </div>
#     
# ---
#     
# I suggest that we work on the project in dialogue: if you change something in the project or respond to my comments, write about it. It will be easier for me to track changes if you highlight your comments:   
#     
# <div class="alert alert-info"> <b>Student сomments:</b> Student answer..</div>
#     
# All this will help to make the recheck of your project faster. If you have any questions about my comments, let me know, we'll figure it out together :)   
#     
# ---

# # Yandex.Music

# # Contents <a id='back'></a>
# 
# * [Introduction](#intro)
# * [Stage 1. Data overview](#data_review)
#     * [Conclusions](#data_review_conclusions)
# * [Stage 2. Data preprocessing](#data_preprocessing)
#     * [2.1 Header style](#header_style)
#     * [2.2 Missing values](#missing_values)
#     * [2.3 Duplicates](#duplicates)
#     * [2.4 Conclusions](#data_preprocessing_conclusions)
# * [Stage 3. Testing the hypotheses](#hypotheses)
#     * [3.1 Hypothesis 1: user activity in the two cities](#activity)
#     * [3.2 Hypothesis 2: music preferences on Monday and Friday](#week)
#     * [3.3 Hypothesis 3: genre preferences in Springfield and Shelbyville](#genre)
# * [Findings](#end)

# ## Introduction <a id='intro'></a>
# Whenever we're doing research, we need to formulate hypotheses that we can then test. Sometimes we accept these hypotheses; other times, we reject them. To make the right decisions, a business must be able to understand whether or not it's making the right assumptions.
# 
# In this project, you'll compare the music preferences of the cities of Springfield and Shelbyville. You'll study real Yandex.Music data to test the hypotheses below and compare user behavior for these two cities.
# 
# ### Goal: 
# Test three hypotheses:
# 1. User activity differs depending on the day of the week and from city to city. 
# 2. On Monday mornings, Springfield and Shelbyville residents listen to different genres. This is also true for Friday evenings. 
# 3. Springfield and Shelbyville listeners have different preferences. In Springfield, they prefer pop, while Shelbyville has more rap fans.
# 
# ### Stages 
# Data on user behavior is stored in the file `/datasets/music_project_en.csv`. There is no information about the quality of the data, so you will need to explore it before testing the hypotheses. 
# 
# First, you'll evaluate the quality of the data and see whether its issues are significant. Then, during data preprocessing, you will try to account for the most critical problems.
#  
# Your project will consist of three stages:
#  1. Data overview
#  2. Data preprocessing
#  3. Testing the hypotheses
#  
# [Back to Contents](#back)

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №1__
# 
# Pay attention to the design of this project. It's a good practice to write out the goal and the main steps. I recommend that you take it on board.

# 

# ## Stage 1. Data overview <a id='data_review'></a>
# 
# Open the data on Yandex.Music and explore it.

# You'll need `pandas`, so import it.

# In[1]:


# importing pandas
import pandas as pd


# Read the file `music_project_en.csv` from the `/datasets/` folder and save it in the `df` variable:

# In[2]:


# reading the file and storing it to df
df = pd.read_csv('/datasets/music_project_en.csv')

print(df.describe())


# Print the first 10 table rows:

# In[3]:


# obtaining the first 10 rows from the df table
print(df.head(10))


# <div class="alert alert-block alert-warning">📝
#     
# 
# __Reviewer's comment №1__
# 
# It is better to use display() rather than print() to output a dataframe object. This way it will be clearer

# Obtaining the general information about the table with one command:

# In[4]:


# obtaining general information about the data in df
print(df.info())


# The table contains seven columns. They all store the same data type: `object`.
# 
# According to the documentation:
# - `'userID'` — user identifier
# - `'Track'` — track title
# - `'artist'` — artist's name
# - `'genre'`
# - `'City'` — user's city
# - `'time'` — the exact time the track was played
# - `'Day'` — day of the week
# 
# We can see three issues with style in the column names:
# 1. Some names are uppercase, some are lowercase.
# 2. There are spaces in some names.
# 3. The inconsistent usage of apostrophes.
# 
# The number of column values is different. This means the data contains missing values.
# 

# ### Conclusions <a id='data_review_conclusions'></a> 
# 
# Each row in the table stores data on a track that was played. Some columns describe the track itself: its title, artist and genre. The rest convey information about the user: the city they come from, the time they played the track. 
# 
# It's clear that the data is sufficient to test the hypotheses. However, there are missing values.
# 
# To move forward, we need to preprocess the data.

# [Back to Contents](#back)

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №1__
# 
# It's all good here. The conclusions in this project are very well laid out, indicating the problems that need to be solved next.

# ## Stage 2. Data preprocessing <a id='data_preprocessing'></a>
# Correct the formatting in the column headers and deal with the missing values. Then, check whether there are duplicates in the data.

# ### Header style <a id='header_style'></a>
# Print the column header:

# In[5]:


# the list of column names in the df table
print(df.columns)


# <div class="alert alert-block alert-warning">📝
#     
# 
# __Reviewer's comment №1__
# 
# 
# It is not necessary to write the print() method in the only or last line of the Jupyter code cell, unlike the simulator

# Change column names according to the rules of good style:
# * If the name has several words, use snake_case
# * All characters must be lowercase
# * Delete spaces

# In[6]:


# renaming columns
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')


# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №1__
# 
# Well done

# Check the result. Print the names of the columns once more:

# In[7]:


# checking result: the list of column names
print(df.columns)


# [Back to Contents](#back)

# ### Missing values <a id='missing_values'></a>
# First, find the number of missing values in the table. To do so, use two `pandas` methods:

# In[8]:


# calculating missing values
missing_values_count = df.isnull().sum()
print(missing_values_count)


# Not all missing values affect the research. For instance, the missing values in `track` and `artist` are not critical. You can simply replace them with clear markers.
# 
# But missing values in `'genre'` can affect the comparison of music preferences in Springfield and Shelbyville. In real life, it would be useful to learn the reasons why the data is missing and try to make up for them. But we do not have that opportunity in this project. So you will have to:
# * Fill in these missing values with markers
# * Evaluate how much the missing values may affect your computations

# Replace the missing values in `'track'`, `'artist'`, and `'genre'` with the string `'unknown'`. To do this, create the `columns_to_replace` list, loop over it with `for`, and replace the missing values in each of the columns:

# In[9]:


# looping over column names and replacing missing values with 'unknown'
columns_to_replace = ['track', 'artist', 'genre']

for column in columns_to_replace:
    df[column].fillna('unknown', inplace=True)


# Make sure the table contains no more missing values. Count the missing values again.

# In[10]:


# counting missing values
missing_values_count = df.isnull().sum()
print(missing_values_count)


# [Back to Contents](#back)

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №1__
# 
# all right

# 

# ### Duplicates <a id='duplicates'></a>
# Find the number of obvious duplicates in the table using one command:

# In[11]:


# counting clear duplicates
duplicate_count = df.duplicated().sum()
print(duplicate_count)


# Call the `pandas` method for getting rid of obvious duplicates:

# In[12]:


# removing obvious duplicates


# Count obvious duplicates once more to make sure you have removed all of them:

# In[13]:


# checking for duplicates
df.drop_duplicates(inplace=True)


# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №1__
# 
# You mastered the removal of obvious duplicates, too, well done. Ideally, overwrite the index

# Now get rid of implicit duplicates in the `genre` column. For example, the name of a genre can be written in different ways. Such errors will also affect the result.

# Print a list of unique genre names, sorted in alphabetical order. To do so:
# * Retrieve the intended DataFrame column 
# * Apply a sorting method to it
# * For the sorted column, call the method that will return all unique column values

# In[14]:


# viewing unique genre names
unique_genres = df['genre'].sort_values().unique()
print(unique_genres)


# Look through the list to find implicit duplicates of the genre `hiphop`. These could be names written incorrectly or alternative names of the same genre.
# 
# You will see the following implicit duplicates:
# * `hip`
# * `hop`
# * `hip-hop`
# 
# To get rid of them, declare the function `replace_wrong_genres()` with two parameters: 
# * `wrong_genres=` — the list of duplicates
# * `correct_genre=` — the string with the correct value
# 
# The function should correct the names in the `'genre'` column from the `df` table, i.e. replace each value from the `wrong_genres` list with the value in `correct_genre`.

# In[15]:


# function for replacing implicit duplicates
def replace_wrong_genres(wrong_genres, correct_genre):
    for wrong_genre in wrong_genres:
        df['genre'] = df['genre'].replace(wrong_genre, correct_genre)


# Call `replace_wrong_genres()` and pass it arguments so that it clears implicit duplcates (`hip`, `hop`, and `hip-hop`) and replaces them with `hiphop`:

# In[16]:


# removing implicit duplicates
wrong_genres_list = ['hip', 'hop', 'hip-hop']

# Correct genre value
correct_genre_value = 'hiphop'

# Call the function to replace wrong genres
replace_wrong_genres(wrong_genres_list, correct_genre_value)


# Make sure the duplicate names were removed. Print the list of unique values from the `'genre'` column:

# In[17]:


# checking for implicit duplicates
unique_genres = df['genre'].sort_values().unique()
print(unique_genres)


# [Back to Contents](#back)

# ### Conclusions <a id='data_preprocessing_conclusions'></a>
# We detected three issues with the data:
# 
# - Incorrect header styles
# - Missing values
# - Obvious and implicit duplicates
# 
# The headers have been cleaned up to make processing the table simpler.
# 
# All missing values have been replaced with `'unknown'`. But we still have to see whether the missing values in `'genre'` will affect our calculations.
# 
# The absence of duplicates will make the results more precise and easier to understand.
# 
# Now we can move on to testing hypotheses. 

# [Back to Contents](#back)

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №1__
# 
# Well done, you managed with the duplicates. The function is written absolutely right.

# ## Stage 3. Testing hypotheses <a id='hypotheses'></a>

# ### Hypothesis 1: comparing user behavior in two cities <a id='activity'></a>

# According to the first hypothesis, users from Springfield and Shelbyville listen to music differently. Test this using the data on three days of the week: Monday, Wednesday, and Friday.
# 
# * Divide the users into groups by city.
# * Compare how many tracks each group played on Monday, Wednesday, and Friday.
# 

# For the sake of practice, perform each computation separately. 
# 
# Evaluate user activity in each city. Group the data by city and find the number of songs played in each group.
# 
# 

# In[18]:


# Counting up the tracks played in each city
city_activity = df.groupby('city')['track'].count()
print(city_activity)


# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №1__
# 
# Great!)

# 

# Springfield has more tracks played than Shelbyville. But that does not imply that citizens of Springfield listen to music more often. This city is simply bigger, and there are more users.
# 
# Now group the data by day of the week and find the number of tracks played on Monday, Wednesday, and Friday.
# 

# In[19]:


# Calculating tracks played on each of the three days
days_activity = df[df['day'].isin(['Monday', 'Wednesday', 'Friday'])].groupby('day')['track'].count()
print(days_activity)


# Wednesday is the quietest day overall. But if we consider the two cities separately, we might come to a different conclusion.

# You have seen how grouping by city or day works. Now write a function that will group by both.
# 
# Create the `number_tracks()` function to calculate the number of songs played for a given day and city. It will require two parameters:
# * day of the week
# * name of the city
# 
# In the function, use a variable to store the rows from the original table, where:
#   * `'day'` column value is equal to the `day` parameter
#   * `'city'` column value is equal to the `city` parameter
# 
# Apply consecutive filtering with logical indexing.
# 
# Then calculate the `'user_id'` column values in the resulting table. Store the result to a new variable. Return this variable from the function.

# In[20]:


# <creating the function number_tracks()>
# We'll declare a function with two parameters: day=, city=.
# Let the track_list variable store the df rows where
# the value in the 'day' column is equal to the day= parameter and, at the same time, 
# the value in the 'city' column is equal to the city= parameter (apply consecutive filtering 
# with logical indexing).
# Let the track_list_count variable store the number of 'user_id' column values in track_list
# (found with the count() method).
# Let the function return a number: the value of track_list_count.

def number_tracks(day, city):
    track_list = df[(df['day'] == day) & (df['city'] == city)]
    track_list_count = track_list['userid'].count()
    return track_list_count
# The function counts tracked played for a certain city and day.
# It first retrieves the rows with the intended day from the table,
# then filters out the rows with the intended city from the result,
# then finds the number of 'user_id' values in the filtered table,
# then returns that number.
# To see what it returns, wrap the function call in print().
city = 'Springfield'
day = 'Monday'
print(number_tracks(day, city))


# Call `number_tracks()` six times, changing the parameter values, so that you retrieve the data on both cities for each of the three days.

# In[21]:


# the number of songs played in Springfield on Monday
print("Springfield on Monday:", number_tracks('Monday', 'Springfield'))


# In[22]:


# the number of songs played in Shelbyville on Monday
print("Shelbyville on Monday:", number_tracks('Monday', 'Shelbyville'))


# In[23]:


# the number of songs played in Springfield on Wednesday
print("Springfield on Wednesday:", number_tracks('Wednesday', 'Springfield'))


# In[24]:


# the number of songs played in Shelbyville on Wednesday
print("Shelbyville on Wednesday:", number_tracks('Wednesday', 'Shelbyville'))


# In[25]:


# the number of songs played in Springfield on Friday
print("Springfield on Friday:", number_tracks('Friday', 'Springfield'))


# In[26]:


# the number of songs played in Shelbyville on Friday
print("Shelbyville on Friday:", number_tracks('Friday', 'Shelbyville'))


# Use `pd.DataFrame` to create a table, where
# * Column names are: `['city', 'monday', 'wednesday', 'friday']`
# * The data is the results you got from `number_tracks()`

# In[27]:


# table with results
results = {
    'city': ['Springfield', 'Shelbyville', 'Springfield', 'Shelbyville', 'Springfield', 'Shelbyville'],
    'monday': [number_tracks('Monday', 'Springfield'), number_tracks('Monday', 'Shelbyville'),
               number_tracks('Monday', 'Springfield'), number_tracks('Monday', 'Shelbyville'),
               number_tracks('Monday', 'Springfield'), number_tracks('Monday', 'Shelbyville')],
    'wednesday': [number_tracks('Wednesday', 'Springfield'), number_tracks('Wednesday', 'Shelbyville'),
                  number_tracks('Wednesday', 'Springfield'), number_tracks('Wednesday', 'Shelbyville'),
                  number_tracks('Wednesday', 'Springfield'), number_tracks('Wednesday', 'Shelbyville')],
    'friday': [number_tracks('Friday', 'Springfield'), number_tracks('Friday', 'Shelbyville'),
               number_tracks('Friday', 'Springfield'), number_tracks('Friday', 'Shelbyville'),
               number_tracks('Friday', 'Springfield'), number_tracks('Friday', 'Shelbyville')]
}

# Create a DataFrame
results_df = pd.DataFrame(results)

# Print the results DataFrame
print(results_df)


# **Conclusions**
# 
# The data reveals differences in user behavior:
# 
# - In Springfield, the number of songs played peaks on Mondays and Fridays, while on Wednesday there is a decrease in activity.
# - In Shelbyville, on the contrary, users listen to music more on Wednesday. User activity on Monday and Friday is smaller.
# 
# So the first hypothesis seems to be correct.

# [Back to Contents](#back)

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №1__
# 
# Great, the first hypothesis has been solved.

# 

# ### Hypothesis 2: music at the beginning and end of the week <a id='week'></a>

# According to the second hypothesis, on Monday morning and Friday night, citizens of Springfield listen to genres that differ from ones users from Shelbyville enjoy.

# Get tables (make sure that the name of your combined table matches the DataFrame given in the two code blocks below):
# * For Springfield — `spr_general`
# * For Shelbyville — `shel_general`

# In[28]:


# create the spr_general table from the df rows, 
# where the value in the 'city' column is 'Springfield'

spr_general = df[df['city'] == 'Springfield']


# In[29]:


# create the shel_general from the df rows,
# where the value in the 'city' column is 'Shelbyville'
shel_general = df[df['city'] == 'Shelbyville']


# Write the `genre_weekday()` function with four parameters:
# * A table for data (`df`)
# * The day of the week (`day`)
# * The first timestamp, in 'hh:mm' format (`time1`)
# * The last timestamp, in 'hh:mm' format (`time2`)
# 
# The function should return info on the 15 most popular genres on a given day within the period between the two timestamps.

# In[30]:


# 1) Let the genre_df variable store the rows that meet several conditions:
#    - the value in the 'day' column is equal to the value of the day= argument
#    - the value in the 'time' column is greater than the value of the time1= argument
#    - the value in the 'time' column is smaller than the value of the time2= argument
#    Use consecutive filtering with logical indexing.

# 2) Group genre_df by the 'genre' column, take one of its columns, 
#    and use the count() method to find the number of entries for each of 
#    the represented genres; store the resulting Series to the
#    genre_df_count variable

# 3) Sort genre_df_count in descending order of frequency and store the result
#    to the genre_df_sorted variable

# 4) Return a Series object with the first 15 genre_df_sorted value - the 15 most
#    popular genres (on a given day, within a certain timeframe)

# Write your function here
def genre_weekday(df, day, time1, time2):
    # consecutive filtering
    # Create the variable genre_df which will store only those df rows where the day is equal to day=
    genre_df = df[df['day'] == day]

    # filter again so that genre_df will store only those rows where the time is smaller than time2=
    genre_df = genre_df[genre_df['time'] < time2]

    # filter once more so that genre_df will store only rows where the time is greater than time1=
    genre_df = genre_df[genre_df['time'] > time1]

    # group the filtered DataFrame by the column with the names of genres, take the genre column, and find the number of rows for each genre with the count() method
    genre_df_count = genre_df.groupby('genre')['genre'].count()

    # sort the result in descending order (so that the most popular genres come first in the Series object)
    genre_df_sorted = genre_df_count.sort_values(ascending=False)

    # we will return the Series object storing the 15 most popular genres on a given day in a given timeframe
    return genre_df_sorted[:15]


# Compare the results of the `genre_weekday()` function for Springfield and Shelbyville on Monday morning (from 7AM to 11AM) and on Friday evening (from 17:00 to 23:00):

# In[31]:


# calling the function for Monday morning in Springfield (use spr_general instead of the df table)
monday_morning_springfield = genre_weekday(spr_general, 'Monday', '07:00', '11:00')
print("Top genres in Springfield on Monday morning:")
print(monday_morning_springfield)


# In[32]:


# calling the function for Monday morning in Shelbyville (use shel_general instead of the df table)
monday_morning_shelbyville = genre_weekday(shel_general, 'Monday', '07:00', '11:00')
print("Top genres in Shelbyville on Monday morning:")
print(monday_morning_shelbyville)


# In[33]:


# calling the function for Friday evening in Springfield
friday_evening_springfield = genre_weekday(spr_general, 'Friday', '17:00', '23:00')
print("\nTop genres in Springfield on Friday evening:")
print(friday_evening_springfield)


# In[34]:


# calling the function for Friday evening in Shelbyville
friday_evening_shelbyville = genre_weekday(shel_general, 'Friday', '17:00', '23:00')
print("Top genres in Shelbyville on Friday evening:")
print(friday_evening_shelbyville)


# **Conclusion**
# 
# Having compared the top 15 genres on Monday morning, we can draw the following conclusions:
# 
# 1. Users from Springfield and Shelbyville listen to similar music. The top five genres are the same, only rock and electronic have switched places.
# 
# 2. In Springfield, the number of missing values turned out to be so big that the value `'unknown'` came in 10th. This means that missing values make up a considerable portion of the data, which may be a basis for questioning the reliability of our conclusions.
# 
# For Friday evening, the situation is similar. Individual genres vary somewhat, but on the whole, the top 15 is similar for the two cities.
# 
# Thus, the second hypothesis has been partially proven true:
# * Users listen to similar music at the beginning and end of the week.
# * There is no major difference between Springfield and Shelbyville. In both cities, pop is the most popular genre.
# 
# However, the number of missing values makes this result questionable. In Springfield, there are so many that they affect our top 15. Were we not missing these values, things might look different.

# [Back to Contents](#back)

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №1__
# 
# Everything is perfect.

# 

# ### Hypothesis 3: genre preferences in Springfield and Shelbyville <a id='genre'></a>
# 
# Hypothesis: Shelbyville loves rap music. Springfield's citizens are more into pop.

# Group the `spr_general` table by genre and find the number of songs played for each genre with the `count()` method. Then sort the result in descending order and store it to `spr_genres`.

# In[35]:


# on one line: group the spr_general table by the 'genre' column, 
# count the 'genre' values with count() in the grouping, 
# sort the resulting Series in descending order, and store it to spr_genres
spr_genres = spr_general.groupby('genre')['genre'].count().sort_values(ascending=False)


# Print the first 10 rows from `spr_genres`:

# In[36]:


# printing the first 10 rows of spr_genres
print(spr_genres.head(10))


# Now do the same with the data on Shelbyville.
# 
# Group the `shel_general` table by genre and find the number of songs played for each genre. Then sort the result in descending order and store it to the `shel_genres` table:
# 

# In[37]:


# on one line: group the shel_general table by the 'genre' column, 
# count the 'genre' values in the grouping with count(), 
# sort the resulting Series in descending order and store it to shel_genres
shel_genres = shel_general.groupby('genre')['genre'].count().sort_values(ascending=False)


# Print the first 10 rows of `shel_genres`:

# In[38]:


# printing the first 10 rows from shel_genres
print(shel_genres.head(10))


# **Conclusion**

# The hypothesis has been partially proven true:
# * Pop music is the most popular genre in Springfield, as expected.
# * However, pop music turned out to be equally popular in Springfield and Shelbyville, and rap wasn't in the top 5 for either city.
# 

# [Back to Contents](#back)

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №1__
# 
# Great, with genre preferences also figured out.

# 

# # Findings <a id='end'></a>

# We have tested the following three hypotheses:
# 
# 1. User activity differs depending on the day of the week and from city to city. 
# 2. On Monday mornings, Springfield and Shelbyville residents listen to different genres. This is also true for Friday evenings. 
# 3. Springfield and Shelbyville listeners have different preferences. In both Springfield and Shelbyville, they prefer pop.
# 
# After analyzing the data, we concluded:
# 
# 1. User activity in Springfield and Shelbyville depends on the day of the week, though the cities vary in different ways. 
# 
# The first hypothesis is fully accepted.
# 
# 2. Musical preferences do not vary significantly over the course of the week in both Springfield and Shelbyville. We can see small differences in order on Mondays, but:
# * In Springfield and Shelbyville, people listen to pop music most.
# 
# So we can't accept this hypothesis. We must also keep in mind that the result could have been different if not for the missing values.
# 
# 3. It turns out that the musical preferences of users from Springfield and Shelbyville are quite similar.
# 
# The third hypothesis is rejected. If there is any difference in preferences, it cannot be seen from this data.
# 
# ### Note 
# In real projects, research involves statistical hypothesis testing, which is more precise and more quantitative. Also note that you cannot always draw conclusions about an entire city based on the data from just one source.
# 
# You will study hypothesis testing in the sprint on statistical data analysis.

# [Back to Contents](#back)

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Reviewer's comment №1__
# 
# That's a great bottom line.
#     
#     
# ---    
#     
# You did great on your first project and mastered the basic functionality of Python for analytics. 

# 
