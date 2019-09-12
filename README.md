# Stream Video Dowlnloader using python script

Example App using python to download a stream video in ubuntu system using terminal / web / browser and see as offline video

## Install Packages

`pip install m3u8`

`pip install requests`

`pip install tqdm`

`pip install subprocess`

## Prerequisite

- Click `Ctrl+Shift+I` or `F12` in chrome browser

- Look for **master.m3u8** file in **Network** tab
  * **master.m3u8** file is the collection of all **segment.ts** files uri
  * **segment.ts** files are small segment of streams from the database as blob type
  * Sometimes Look for other.m3u8 files in **Network** tab which will be belongs to master.m3u8 file(`basically master.m3u8 is collection of other.m3u8 files' urls & other.m3u8 files are collection of segment.ts files' urls`)

![master m3u8](/images/master-m3u8-file.jpg)

- Look for segment.ts in **Network** tab

![master m3u8](/images/segment-ts.jpg)




## Run

- Click `Ctrl+Shift+I` or `F12` in chrome browser

1. **For mp4 video files**

- *If found `<video src="video.mp4"></video>` tag*

- **Run** `python video_stream_downloader_mp4.py`

2. **For blob video files**

- *If found `<video src="src="blob:https://www.hotstar.com/03ca18dc-3d56-4995-a253-60e2770a69a9"></video>` tag*

- Look for **master.m3u8** file link in **Network** tab & `refer Prerequisite` & replace the url with **master.m3u8** url

- **Run** `python video_stream_downloader_blob.py`

**Sample Output:** converting ts file into mp4 file using ffmpeg

![Sample Output](/images/blob-video.png)
