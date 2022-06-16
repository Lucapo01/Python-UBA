import tekore as tk

client_id = "5422aa04b10040e18ef47834e08ec9aa"
client_secret = "a03bc8e3402949e480f4eb98036a230a"

app_token = tk.request_client_token(client_id, client_secret)

spotify = tk.Spotify(app_token)
                       
album = spotify.album('71O60S5gIJSIAhdnrDIh3N')
for track in album.tracks.items:
    print(track.track_number, track.name)