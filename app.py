#!/usr/bin/env python3
import sys
import subprocess
from pathlib import Path

VIDEO_EXTS = {'.mp4', '.mov', '.avi', '.mkv', '.webm', '.flv', '.wmv'}


def check_tools():
    from shutil import which
    if which('ffmpeg') is None or which('ffprobe') is None:
        print('ffmpeg and ffprobe are required. Install them (e.g., sudo apt install ffmpeg).')
        sys.exit(1)


def get_duration(path: Path) -> float:
    cmd = [
        'ffprobe', '-v', 'error', '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1', str(path)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(res.stderr.strip() or 'ffprobe failed')
    return float(res.stdout.strip())


def extract_frame(input_path: Path, ts: float, out_path: Path):
    # use -ss before -i for fast seeking
    cmd = ['ffmpeg', '-y', '-ss', f'{ts:.3f}', '-i', str(input_path), '-frames:v', '1', '-q:v', '2', str(out_path)]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f'ffmpeg failed for {input_path.name} at {ts:.2f}s: {e.stderr.strip()}')
        raise


def process_video(path: Path, count: int, output_root: Path):
    dur = get_duration(path)
    if count <= 0:
        return
    timestamps = [dur * (i + 1) / (count + 1) for i in range(count)]
    out_dir = path.with_suffix('').name
    out_dir_path = output_root / out_dir
    out_dir_path.mkdir(parents=True, exist_ok=True)
    for idx, ts in enumerate(timestamps, start=1):
        out_file = out_dir_path / f"{path.stem}_shot_{idx:03d}.jpg"
        print(f'Extracting {out_file.name} at {ts:.2f}s')
        extract_frame(path, ts, out_file)


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Extract evenly spaced screenshots from videos in a folder.')
    parser.add_argument('folder', nargs='?', default='.', help='Folder containing videos')
    parser.add_argument('-n', '--num', type=int, help='Number of screenshots per video')
    args = parser.parse_args()

    folder = Path(args.folder)
    if not folder.exists() or not folder.is_dir():
        print('Folder not found:', folder)
        sys.exit(1)

    check_tools()

    if args.num is None:
        try:
            num = int(input('How many screenshots per video? '))
        except Exception:
            print('Invalid number')
            sys.exit(1)
    else:
        num = args.num

    # Support two modes:
    # 1) user passes the target root (contains a 'video' subfolder) -> videos are in <folder>/video and outputs go to <folder>
    # 2) user passes the 'video' folder directly -> videos are in <folder> and outputs go to <folder>.parent
    if folder.name == 'video':
        videos_dir = folder
    else:
        videos_dir = folder / 'video'

    # Place outputs inside the same folder that contains the videos (the input folder)
    output_root = videos_dir

    # ensure the videos folder exists
    videos_dir.mkdir(parents=True, exist_ok=True)

    print(f'Looking for videos in: {videos_dir}')

    for f in sorted(videos_dir.iterdir()):
        if f.is_file() and f.suffix.lower() in VIDEO_EXTS:
            print('Processing', f.name)
            try:
                process_video(f, num, output_root)
            except Exception as e:
                print('Error processing', f.name, '-', e)


if __name__ == '__main__':
    main()
