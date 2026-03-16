#!/usr/bin/env bash

SPOTDL=./.venv/bin/spotdl

if [[ $3 == "" ]]; then
        echo "Please send a link / Query!" > link.txt
        exit
fi

if [[ $2 == "flac" ]]; then #flac
        $SPOTDL "$1" --format flac --ffmpeg-args '-ar 44100'
elif [[ $2 == "m4a" ]]; then #m4a
        $SPOTDL "$1" --format m4a --ffmpeg-args '-ar 44100'
elif [[ $2 == "mp3" ]]; then #mp3
        $SPOTDL "$1" --format mp3 --ffmpeg-args '-ar 44100'
elif [[ $2 == "-sc" ]]; then # soundcloud
        $SPOTDL -l "$1"
        MUSIC=$(ls | grep .mp3)
fi

if [[ $2 == "flac" && $3 == "-t" ]]; then
        MUSIC=$(ls | grep .flac)
elif [[ $2 == "mp3" && $3 == "-t" ]]; then
        MUSIC=$(ls | grep .mp3)
elif [[ $2 == "m4a" && $3 == "-t" ]]; then
        MUSIC=$(ls | grep .m4a)
fi

echo "Uploading..." > link.txt

if [[ ! -n $(ls | grep .flac) &&
      ! -n $(ls | grep .mp3) &&
      ! -n $(ls | grep .m4a) ]]; then
        echo "Something went wrong. Check your entries and try again." > link.txt
fi
