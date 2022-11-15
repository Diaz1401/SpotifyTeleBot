#!/bin/bash

# ffmpeg comp tool

upload() {
        touch link.txt
        ./transfer wet "$1" | grep Download > link.txt
}

ZIPNAME=$(date +%s)

if [[ $3 == "" ]]; then
        echo "Please send a link / Query!" > link.txt
        exit
fi

if [[ $2 == "flac" ]]; then #flac
        ./spotdl "$1" --format flac
elif [[ $2 == "m4a" ]]; then #m4a
        ./spotdl "$1" --format m4a
elif [[ $2 == "mp3" ]]; then #mp3
        ./spotdl "$1"
elif [[ $2 == "-sc" ]]; then # soundcloud
        scdl -l "$1"
        MUSIC=$(ls | grep .mp3)
fi

if [[ $2 == "flac" && $3 == "-t" ]]; then
        MUSIC=$(ls | grep .flac)
elif [[ $2 == "mp3" && $3 == "-t" ]]; then
        MUSIC=$(ls | grep .mp3)
elif [[ $2 == "m4a" && $3 == "-t" ]]; then
        MUSIC=$(ls | grep .m4a)
fi

if [[ $3 == "-a" || $3 == "-p" ]];then
        if [[ $2 == "flac" ]]; then
                zip -r $ZIPNAME.zip *.flac
                MUSIC=$ZIPNAME.zip
        elif [[ $2 == "mp3" ]]; then
                zip -r $ZIPNAME.zip *.mp3
                MUSIC=$ZIPNAME.zip
        elif [[ $2 == "m4a" ]]; then
                zip -r $ZIPNAME.zip *.m4a
                MUSIC=$ZIPNAME.zip
        fi
fi

echo $MUSIC

if [[ $3 != "" ]]; then
        upload "$MUSIC" "Playlist / Album"
else
        upload "$MUSIC" $MUSIC
fi

sed -i "s/Link/$MUSIC at/g" link.txt

if [[ ! -n $(ls | grep .zip) &&  ! -n $(ls | grep .flac) &&  ! -n $(ls | grep .mp3) &&  ! -n $(ls | grep .m4a) ]]; then
        echo "Something went wrong. Check your entries and try again." > link.txt
fi

rm -rf *.flac
rm -rf *.mp3
rm -rf *.m4a
rm -rf *.zip