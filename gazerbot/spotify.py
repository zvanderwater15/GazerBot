import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from gazerbot import secrets

def generate_token():
    """ Generate the token. Please respect these credentials :) """
    credentials = SpotifyClientCredentials(
        client_id=secrets.SPOTIFY_ID,
        client_secret=secrets.SPOTIFY_SECRET)
    token = credentials.get_access_token()
    return token


def get_user_playlists(user, limit=50):
    token = generate_token()
    spotify = spotipy.Spotify(auth=token)

    return spotify.user_playlists(user, limit=limit)

def get_tracks_from_playlist(user, playlist_name):
    token = generate_token()
    spotify = spotipy.Spotify(auth=token)

    playlist_id = None

    # search all playlists for the specific user to get the playlist id using the playlist name
    for playlist in get_user_playlists(user, 10)['items']:
        if playlist['name'] == playlist_name:
            playlist_id = playlist['id']
            break

    # get all information for this playlist including tracks
    playlist_tracks = spotify.user_playlist(user, playlist_id,
                                    fields='tracks,next,name')

    # create and return a list of the artist name and title of each track
    track_artist_title_list = []
    for playlist_track in playlist_tracks['tracks']['items']:
        track = playlist_track['track']
        track_name = track['name']
        track_artist = track['artists'][0]['name']
        track_artist_title_list.append({"artist": track_artist, "title": track_name})

    return track_artist_title_list