# Video2Frames

Simple CLI tool to extract evenly-spaced screenshots from videos in a folder.

Requirements
- `ffmpeg` (includes `ffprobe`) installed on your system. On Debian/Ubuntu: `sudo apt install ffmpeg`.
- Python 3.8+

Usage

- Run interactively and follow the prompt:

```bash
python3 app.py /path/to/folder
```

- Or pass number of screenshots per video directly:

```bash
python3 app.py /path/to/folder -n 5
```

Behavior

- The script scans the provided folder for video files (mp4, mov, avi, mkv, webm, flv, wmv).
- For each video it creates a folder next to the video using the video's filename (without extension) and saves screenshots named `<video>_shot_XXX.jpg`.
- Screenshots are taken at evenly spaced timestamps across the video duration.

Example

If you have `example.mp4` in `/data/videos`, running `python3 app.py /data/videos -n 4` will create a folder `/data/videos/example` containing 4 JPG screenshots taken from `example.mp4`.

Notes
- No Python packages are required; the script uses `ffmpeg` via subprocess.
