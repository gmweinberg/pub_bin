#!/bin/bash
MKV=$1
MP4=${MKV::-4}.mp4
ffmpeg -i "$MKV" -codec copy "$MP4"
