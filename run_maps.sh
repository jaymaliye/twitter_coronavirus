#!/bin/sh

for j in /data/Twitter\ dataset/geoTwitter20-*; do
    nohup ./src/map.py "--input_path=$j" &
    #echo $j
done
