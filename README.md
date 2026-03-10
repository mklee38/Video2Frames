# Video2Frames

Simple CLI tool to extract evenly-spaced screenshots from videos in a folder.

Requirements
- `ffmpeg` (includes `ffprobe`) installed on your system. On Debian/Ubuntu: `sudo apt install ffmpeg`.
- Python 3.8+

Usage

- Run interactively and follow the prompt:

You can run the script two ways:

- Pass the target root folder which contains (or will contain) a `video` subfolder. The script looks for videos in `<target>/video` and writes outputs inside the `video` folder (e.g., `<target>/video/<video_name>`).
- Or pass the `video` folder directly; outputs will be written inside the `video` folder (e.g., `/path/to/target-folder/video/<video_name>`).

Run interactively and follow the prompt:

```bash
python3 app.py /path/to/target-folder
```

Or pass the `video` folder directly:

```bash
python3 app.py /path/to/target-folder/video -n 4
```

- Or pass number of screenshots per video directly:

```bash
python3 app.py /path/to/folder -n 5
```

Behavior

- The script scans the provided folder for video files (mp4, mov, avi, mkv, webm, flv, wmv).
- For each video it creates a folder next to the video using the video's filename (without extension) and saves screenshots named `<video>_shot_XXX.jpg`.
- Screenshots are taken at evenly spaced timestamps across the video duration.

- The script expects videos to be inside `<target>/video`. For each video it creates an output folder in `<target>/<video_name>/` (not inside the `video` folder).

Example

If you have `example.mp4` in `/data/videos`, running `python3 app.py /data/videos -n 4` will create a folder `/data/videos/example` containing 4 JPG screenshots taken from `example.mp4`.

Notes
- No Python packages are required; the script uses `ffmpeg` via subprocess.
