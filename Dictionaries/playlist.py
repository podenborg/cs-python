playlist = {
  'title': 'patagonia bus',
  'author': 'colt steele',
  'songs': [
    { 'title': 'song1', 'artist': ['blue'], 'duration': 2.5 },
    { 'title': 'song2', 'artist': ['kitty', 'djcat'], 'duration': 5.25 },
    { 'title': 'song3', 'artist': ['garfield'], 'duration': 2 },
  ]
}

for song in playlist['songs']:
  print(song['duration'])