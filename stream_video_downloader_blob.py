# Download a simple blob file using video tag from html page 
# <video src="blob:https://www.hotstar.com/03ca18dc-3d56-4995-a253-60e2770a69a9"></video>
# html tag

# importing packages
import m3u8
import requests
from tqdm import tqdm_notebook as tqdm
import subprocess

# Start Session 
sess = requests.Session()

# Find master.m3u8 and paste here, it may change with time dynamically
URL = "https://hses.akamaized.net/videos/movies/hindi/mohini/1260009590/1566471840414/fb9c250c675b2f0f578181c586a48c9c/master.m3u8?ladder=phone&hdnea=st=1568282199~exp=1568285799~acl=/*~hmac=3013a8a43274c35fb1f0132381698d97c5f94675ac5dc0fa79af1277ad072821"

# Request for URL
r = sess.get(URL)

# extract request text & playlist key form m3u8 file
m3u8_master = m3u8.loads(r.text)
m3u8_playlist_uris = [playlist['uri']
                      for playlist in m3u8_master.data['playlists']]

print(m3u8_master.data)

M3U8_URI = 'https://hses.akamaized.net/videos/movies/hindi/mohini/1260009590/1566471840414/fb9c250c675b2f0f578181c586a48c9c/'

# make m3u8 playlist_uri using M3U8_URI
for i, uri in enumerate(m3u8_playlist_uris):
    m3u8_playlist_uris[i] = M3U8_URI + uri
    print(m3u8_playlist_uris[i])


playlist_uri = m3u8_playlist_uris[0]
print(playlist_uri)

# Request for playlist_uri & get m3u8_segment_uris
r = sess.get(playlist_uri)
playlist = m3u8.loads(r.text)
m3u8_segment_uris = [segment['uri'] for segment in playlist.data['segments']]
print(m3u8_segment_uris[0])

M3U8_SEGMENT_URI = 'https://hses.akamaized.net/videos/movies/hindi/mohini/1260009590/1566471840414/fb9c250c675b2f0f578181c586a48c9c/media-4/'

# make m3u8 playlist_uri using M3U8_SEGMENT_URI
for i, uri in enumerate(m3u8_segment_uris):
    m3u8_segment_uris[i] = M3U8_SEGMENT_URI + uri
    print(m3u8_segment_uris[i])

# Write a single .ts file from segments of all .ts files
with open("video.ts", 'wb') as f:
    for segment_uri in tqdm(m3u8_segment_uris):
        r = sess.get(segment_uri)
        f.write(r.content)

# Convert .ts file into .mp4 file using ffmpeg and save it
subprocess.run(['ffmpeg', '-i', 'video.ts', 'video.mp4'])
