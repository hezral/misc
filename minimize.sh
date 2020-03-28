#!/usr/bin/env bash

for w in $(xdotool search --name '.*'); do
    xdotool windowminimize "$w"
done
