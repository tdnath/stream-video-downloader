# Download a simple .mp4 file using video tag from html page 
# <video src="https://easyhtml5video.com/assets/video/new/Penguins_of_Madagascar.mp4"></video>
# html tag

# importing packages
import requests

URL = "https://easyhtml5video.com/assets/video/new/Penguins_of_Madagascar.mp4"

# define chunk size
chunk_size = 256

# Request for URL
r = requests.get(URL, stream=True)

# Write the file as .mp4 file by collecting the chunks
with open("Penguins_of_Madagascar.mp4", "wb") as f:
    for chunk in r.iter_content(chunk_size=chunk_size):
        f.write(chunk)

		
		
