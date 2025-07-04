# Databricks notebook source
print("hello, Spotify!")

# COMMAND ----------

# MAGIC %pip install spotipy

# COMMAND ----------

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time

client_credentials_manager = SpotifyClientCredentials(client_id="c369283108564819aedb1cb32371669c", client_secret="b0123cbe32e04397a34ccfe450259c3b")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_track_info(track_name):
    try:
        results = sp.search(q=f'track:{track_name}', type='track', limit=1)
        print(results)
        items = results['tracks']['items']
        print(items)
        if items:
            track = items[0]
            return {
                'name': track['name'],
                'artist': track['artists'][0]['name'],
                'popularity': track['popularity']
            }
        else:
            return None
    except Exception as e:
         print(f"An error occurred: {e}")
         return None

track_name = "Bohemian Rhapsody"
track_info = get_track_info(track_name)

if track_info:
    print(f"Track: {track_info['name']}, Artist: {track_info['artist']}, Popularity: {track_info['popularity']}")
else:
    print(f"Track '{track_name}' not found.")

# COMMAND ----------

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time

client_credentials_manager = SpotifyClientCredentials(client_id="c369283108564819aedb1cb32371669c", client_secret="b0123cbe32e04397a34ccfe450259c3b")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
results = sp.playlist_tracks("54ZA9LXFvvFujmOVWXpHga")  # Global Top 50 playlist ID
tracks = results['items']

# Extract basic data
for track in tracks:
    name = track['track']['name']
    artist = track['track']['artists'][0]['name']
    popularity = track['track']['popularity']
    print(f"{name} by {artist} - Popularity: {popularity}")

# COMMAND ----------

import pandas as pd

# Convert API data to a list
track_data = [{"name": t['track']['name'], "artist": t['track']['artists'][0]['name'], "popularity": t['track']['popularity']} for t in tracks]

# Create a Spark DataFrame
df = spark.createDataFrame(track_data)

# Sort by popularity
top_10 = df.orderBy("popularity", ascending=False).limit(10)
top_10.show()

# COMMAND ----------

# Convert to Pandas for visualization
top_10_pd = top_10.toPandas()

# Plot in Databricks
display(top_10_pd.plot(kind="bar", x="name", y="popularity", title="Top 10 Tracks by Popularity"))

# COMMAND ----------

top_10.write.csv("/FileStore/spotify_top_10.csv", header=True)


# COMMAND ----------

dbutils.fs.ls("/FileStore/")
