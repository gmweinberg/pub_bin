#!/usr/bin/bash
# make a backup of my home directory
#
# make sure the backup disk is mounted
if [ ! -d "/run/media/gweinberg/82d81899-82c5-4b58-a367-5b9a844e3e3f/" ]; then
		echo "mount the disk"
		exit 1
fi

cd
rsync -a --exclude zeeb --exclude tm Documents /run/media/gweinberg/82d81899-82c5-4b58-a367-5b9a844e3e3f/backup/
rsync -a Pictures /run/media/gweinberg/82d81899-82c5-4b58-a367-5b9a844e3e3f/backup/
rsync -a .thunderbird /run/media/gweinberg/82d81899-82c5-4b58-a367-5b9a844e3e3f/backup/
rsync -a .ssh /run/media/gweinberg/82d81899-82c5-4b58-a367-5b9a844e3e3f/backup/
# individual files
rsync -a .bashrc /run/media/gweinberg/82d81899-82c5-4b58-a367-5b9a844e3e3f/backup/
rsync -a .gitconfig /run/media/gweinberg/82d81899-82c5-4b58-a367-5b9a844e3e3f/backup/
rsync -a aascratch /run/media/gweinberg/82d81899-82c5-4b58-a367-5b9a844e3e3f/backup/
rsync -a bin/backhome.sh /run/media/gweinberg/82d81899-82c5-4b58-a367-5b9a844e3e3f/backup/bin
