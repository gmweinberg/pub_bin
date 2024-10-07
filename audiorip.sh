#!/usr/bin/sh

# save audio output to a fil
#
#
if [ -z "${FILE}" ]; then
    echo "please set 'FILE' environment vairiable"
	exit 1
fi
if [ -z "${TIME}" ]; then
    echo "please set 'TIME' environment vairiable"
	exit 1
fi
cd ${HOME}/docs/audio
ffmpeg -f pulse -i alsa_output.pci-0000_06_00.4.analog-stereo.monitor -af "volume=2.0" -acodec libmp3lame -ac 2 -ab 128k -t $TIME "$FILE"
