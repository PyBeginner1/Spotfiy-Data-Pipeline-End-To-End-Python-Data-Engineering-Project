import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3                                                # To store output into s3
from datetime import datetime


def lambda_handler(event, context):
    # Since client_id and client_secret is a secret key, we create a environment with this values
    client_id = os.environ.get("client_id")
    client_secret = os.environ.get("client_secret")
    
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    playlists = spotify.user_playlists('spotify')
    
    top_songs_url = 'https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF'
    songs_uri = top_songs_url.split('/')[-1]
    
    data = spotify.playlist_tracks(songs_uri)
    
    cl = boto3.client('s3')
    
    file_name = "spotify_raw_" + str(datetime.now()) + ".json"
    
    # Store output into s3 
    cl.put_object(
        Bucket = "spotify-etl-sn",
        Key = "raw_data/to_processed/" + file_name,
        Body = json.dumps(data)
        )
