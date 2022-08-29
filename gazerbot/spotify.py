import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from gazerbot import helpers
from gazerbot import secrets

def credentials():
    return SpotifyClientCredentials(
        client_id=secrets.SPOTIFY_ID,
        client_secret=secrets.SPOTIFY_SECRET)


def get_user_playlists(user):
    spotify = spotipy.Spotify(auth_manager=credentials())
    playlist_response = spotify.user_playlists(user)
    playlists = []

    # go through each page of api responses and compile the total list of user playlists
    while playlist_response:
        for i, playlist in enumerate(playlist_response['items']):
            playlists.append({
                'name': playlist['name'], 
                'id' : playlist['id']
            })
        if playlist_response['next']:
            playlist_response = spotify.next(playlist_response)
        else:
            playlist_response = None
    return playlists

def get_tracks_from_playlist(user, playlist_name):
    print("attempting to get tracks from playlist ", playlist_name)

    spotify = spotipy.Spotify(auth_manager=credentials())

    playlist_id = None

    # search all playlists for the specific user to get the playlist id using the playlist name
    for playlist in get_user_playlists(user):
        if helpers.normalize(playlist['name']) == helpers.normalize(playlist_name):
            playlist_id = playlist['id']
            break

    if not playlist_id:
        return []
        
    # get all information for this playlist including tracks
    playlist_tracks = spotify.user_playlist(user, playlist_id, fields='tracks,next,name')['tracks']

    track_list = []
    # create and return a list of the artist name and title of each track
    while playlist_tracks:
        for i, playlist in enumerate(playlist_tracks['items']):
            track = playlist['track']
            track_name = track['name']
            track_artist = track['artists'][0]['name']
            track_list.append({"artist": track_artist, "title": track_name})
        if playlist_tracks['next']:
            playlist_tracks = spotify.next(playlist_tracks)
        else:
            playlist_tracks = None

    print(f"playlist length: {len(track_list)} songs")
    return track_list