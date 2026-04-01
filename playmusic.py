import requests
import spotipy
import os
import time
import subprocess
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "acd9ded8e8944435b146980faabcbcf1"
CLIENT_SECRET = "c504d6dbdea14e47bc1be9c0130b973f"
REDIRECT_URI = "http://127.0.0.1:8888/callback"

SCOPE = "user-read-playback-state user-modify-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,
    open_browser=True
))

def open_spotify():
    try:
        subprocess.Popen("spotify")
        print("Opening Spotify...")
        time.sleep(5)  # Wait for app to fully load
    except Exception as e:
        print("Could not open Spotify:", e)

# <--GET Devices-->
def get_active_device():
    devices = sp.devices()

    if devices["devices"]:
        return devices["devices"][0]["id"]
    else:
        return None

def open_spotify():
    try:
        subprocess.Popen("spotify")
        print("Opening Spotify...")
        time.sleep(5)  # Wait for app to fully load
    except Exception as e:
        print("Could not open Spotify:", e)


# 🎵 Get Active Device


def get_active_device():
    devices = sp.devices()

    if devices["devices"]:
        return devices["devices"][0]["id"]
    else:
        return None

# 🎶 Play Requested Song

def play_song(song_name):
    print(f"Searching for: {song_name}")

    results = sp.search(q=song_name, limit=1, type='track')

    if not results["tracks"]["items"]:
        print("Song not found.")
        return

    track = results["tracks"]["items"][0]
    track_uri = track["uri"]

    print(f"Playing: {track['name']} - {track['artists'][0]['name']}")

    device_id = get_active_device()

    if device_id is None:
        print("No active device found. Opening Spotify...")
        open_spotify()
        device_id = get_active_device()

        if device_id is None:
            print("Still no device found. Open Spotify manually.")
            return

    sp.start_playback(device_id=device_id, uris=[track_uri])
def run_music():
    song = input("Enter song name: ")
    play_song(song)


if __name__ == "__main__":
    run_music()