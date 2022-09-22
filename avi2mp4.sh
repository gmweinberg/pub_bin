#!/bin/bash
for MKV in "$@"
do
    MP4=${MKV::-4}.mp4
    ffmpeg -i "$MKV" -codec copy "$MP4"
done
