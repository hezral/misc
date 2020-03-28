#!/bin/bash

source_dir='/home/adi/Downloads'

for i in $source_dir/*.mp4; do
    echo $i
    #duration=`ffmpeg -i $i  2>&1 | grep Duration | cut -d " " -f 4 | sed s/,// | awk -F  ":" '/1/ {print $3}' | awk -F "." '/1/ {print $1}'`
    #echo $duration
    duration=`ffprobe -v 0 -show_entries format=duration -of compact=p=0:nk=1 $i | awk -F "." '/1/ {print $1}'`
    duration=$((duration - 19)) 

    echo $Duration

    outfile=${i::-3}trimmed.mp4

    ffmpeg -ss 0 -t $duration -i $i -c copy $outfile
done