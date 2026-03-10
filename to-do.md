#To-do 
- Given a folder
- create screenshots in frame of each video in that photo 
- ask user about the number of screen shots before capturing photos from video
- the screen shots should be captured evenly within the video length 
- other file formate can be ignored

#Input
- a folder containing images, videos or other files 

#output
- create folder for each video in the root folder
- folder use the the same name as the video
- each folder contain the screen shots of that video in frame

## App: Video2Frames CLI

This workspace now includes a small CLI app that implements the above requirements.

- **What it does:** Scans a folder for video files, asks (or accepts) the number of screenshots to take, and extracts evenly-spaced frames from each video using `ffmpeg`. For each video it creates a folder (same name as the video file without extension) and saves the screenshots there.
- **Supported video extensions:** mp4, mov, avi, mkv, webm, flv, wmv.
- **Ignored files:** Non-video files are skipped.

- **Files added:** `app.py`, `README.md`, `requirements.txt`.

- **Quick run:** Install `ffmpeg` on your system, then run `python3 app.py /path/to/folder` or run `python3 app.py` and follow the prompt.

- **Videos location:** Put your video files inside a `video` subfolder of the target folder (the script creates this folder if missing). Screenshots for each video are written to a folder in the target root (e.g., `/path/to/folder/<video-name>`).
 - **Videos location:** Put your video files inside a `video` subfolder of the target folder (the script creates this folder if missing). You can also pass the `video` folder directly to the script. Screenshots for each video are written to a folder in the target root (e.g., `/path/to/folder/<video-name>`).

See `README.md` for full usage details and examples.

