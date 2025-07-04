Spotify Trend Analysis Project

What is this Project About?

This project is a beginner-friendly exercise to learn data analysis and API usage using Databricks Community Edition, a free cloud-based platform for data analytics. It pulls music data from the Spotify API to analyze popular tracks, focusing on the Global Top 50 playlist and a specific song ("Bohemian Rhapsody"). The project uses PySpark and Pandas in a Databricks notebook to process, visualize, and save the data. It’s a fun way to explore music trends and learn how to work with real-world data in a cloud environment!

For additional context on data analysis, you can explore Microsoft Learn’s module "Analyze sentiment in text with Keras" to learn about processing data for analytics tasks.

Project Details

What Does the Project Do?





Goal: The project fetches data about popular songs from Spotify, analyzes their popularity, and visualizes the top 10 tracks to understand music trends.



Dataset: The data comes from the Spotify API, including:





Information about a single track ("Bohemian Rhapsody"), like its name, artist, and popularity score (0–100).



Tracks from the Global Top 50 playlist (ID: 54ZA9LXFvvFujmOVWXpHga), including song names, artists, and popularity scores.



Databricks Community Edition: The project runs in Databricks Community Edition, a free cloud platform that supports PySpark for data processing, Pandas for visualization, and cloud storage for saving results.

How Data is Pulled





Spotify API: The project uses the spotipy Python library to connect to Spotify’s public API. It authenticates with a client ID and secret (unique keys) to access Spotify’s data securely.



Single Track Data: The code searches for "Bohemian Rhapsody" using the API’s search function (sp.search), retrieving details like the song’s name, artist, and popularity score.



Playlist Data: The code fetches tracks from the Global Top 50 playlist using the API’s playlist function (sp.playlist_tracks), collecting data on song names, artists, and popularity scores for each track.



Data Extraction: The API returns data in a structured format (like a list of songs), which is then processed into a table for analysis in Databricks.

What the Code Does





Fetch Single Track: Retrieves and prints details for "Bohemian Rhapsody" (e.g., name, artist, popularity).



Fetch Playlist Tracks: Pulls all tracks from the Global Top 50 playlist and prints their names, artists, and popularity scores.



Create a Table: Converts the playlist data into a Spark DataFrame (a table format in PySpark) for analysis.



Find Top Tracks: Sorts the playlist tracks by popularity and selects the top 10 most popular songs.



Visualize Data: Creates a bar chart of the top 10 tracks’ popularity scores using Pandas in Databricks’ visualization tools.



Save Results: Saves the top 10 tracks to a CSV file (spotify_top_10.csv) in Databricks’ cloud storage (/FileStore/).



Check Storage: Lists files in the storage directory (/FileStore/) to confirm the CSV file was saved.

What the Code Shows





Single Track Output: Shows details like "Track: Bohemian Rhapsody, Artist: Queen, Popularity: [score]" (e.g., 85).



Playlist Output: Lists tracks like "[Song Name] by [Artist] - Popularity: [Score]" for the Global Top 50.



Top 10 Table: Displays a table with the 10 most popular tracks, including columns for name, artist, and popularity.



Bar Chart: Visualizes the top 10 tracks’ popularity scores as a bar chart in Databricks.



Saved File: Confirms the CSV file (spotify_top_10.csv) is stored in Databricks’ /FileStore/ directory.

Skills Gained

By working on this project in Databricks Community Edition, you’ll learn these beginner-friendly skills:





API Integration: Learn how to connect to and pull data from a web API (Spotify API) using Python and the spotipy library.



Data Processing with PySpark: Gain experience using PySpark to create and manipulate DataFrames for analyzing large datasets.



Data Visualization: Practice creating bar charts with Pandas to visualize trends, like song popularity, in Databricks.



Databricks Community Edition: Understand how to use Databricks’ free cloud platform for data analytics, including notebooks, PySpark, and cloud storage.



Python Programming: Use Python libraries (spotipy, pandas) and PySpark to fetch, process, and save data.



Data Analysis Basics: Learn to sort and filter data to find insights, like identifying the most popular tracks.



Cloud Storage: Gain experience saving data to cloud storage (e.g., CSV files in /FileStore/) and verifying the results in Databricks.

Things to Know





No Machine Learning: This project focuses on data pulling and analysis, not building a prediction model. The Microsoft Learn module on sentiment analysis can guide you on adding machine learning if desired.



Beginner-Friendly: The project is simple, focusing on fetching and visualizing data, making it great for learning API usage and analytics in Databricks Community Edition.



Databricks Advantage: Databricks Community Edition provides a free environment to learn PySpark, visualize data, and store results in the cloud, ideal for small-scale projects.
