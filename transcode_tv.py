#!/usr/bin/env python3

import argparse
import subprocess
from pathlib import Path

VIDEO_EXTS = {".mp4", ".avi", ".mkv", ".mov", ".webm"}

def is_video_file(path: Path) -> bool:
    """
    Uses ffprobe to check whether a file contains a video stream.
    """
    try:
        result = subprocess.run(
            [
                "ffprobe",
                "-v", "error",
                "-select_streams", "v",
                "-show_entries", "stream=index",
                "-of", "csv=p=0",
                str(path),
            ],
            capture_output=True,
            text=True,
            check=True,
        )
        return bool(result.stdout.strip())
    except subprocess.CalledProcessError:
        return False


def transcode(input_path: Path, output_path: Path):
    output_path.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "ffmpeg",
        "-y",
        "-i", str(input_path),
        "-c:v", "libx264",
        "-profile:v", "main",
        "-level", "4.1",
        "-pix_fmt", "yuv420p",
        "-preset", "slow",
        "-crf", "18",
        "-c:a", "aac",
        "-b:a", "192k",
        str(output_path),
    ]

    print(f"Transcoding: {input_path} → {output_path}")
    subprocess.run(cmd, check=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output_dir", type=Path)
    parser.add_argument("--preserve_tree", action="store_true")
    args = parser.parse_args()

    input_path = args.input.resolve()
    output_dir = args.output_dir.resolve()

    if not input_path.exists():
        raise FileNotFoundError(input_path)

    # rglob works for both files and directories
    files = [input_path] if input_path.is_file() else input_path.rglob("*")

    for path in files:
        if not path.is_file():
            continue

        # Optional cheap pre-filter by extension
        if path.suffix.lower() not in VIDEO_EXTS:
            continue

        if not is_video_file(path):
            continue

        rel_path = path.relative_to(input_path.parent if input_path.is_file() else input_path)
        if args.preserve_tree:
            output_path = (output_dir / rel_path).with_suffix(".mp4")
        else:
            output_path = output_dir / (path.stem + ".mp4")

        if output_path.exists():
            print(f"Skipping (exists): {output_path}")
            continue

        transcode(path, output_path)


if __name__ == "__main__":
    main()
