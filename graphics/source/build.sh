#!/bin/bash

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
#  © 2011-2021 Telenav, Inc.
#  Licensed under Apache License, Version 2.0
#
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#
# IMPORTANT NOTE!
#
# Before running this script you must install imagemagick. On macOS, run this command:
#
#     brew install imagemagick
#
# Scaled images will be created in the scaled/icons folder. This folder should then be
# copied to:
#
#     /docs/png/icons
#
# This folder is mapped to the web by Github Pages, with the URL being of the form:
#
#     https://telenav.github.io/telenav-assets/png/icons/bits-16.png
#

resolutions=(16 24 32 40 48 64 96 128)

mkdir -p ./scaled/icons

for file in ./icons/*.svg; do

    filename=$(basename "$file")
    echo "Converting $file"

    for resolution in "${resolutions[@]}"
    do
       :
       resolution2x=$(( resolution * 2 ))

       echo "  ${resolution}x${resolution}"
       #convert -resize "${resolution}"x"${resolution}"^ -extent "${resolution}"x"${resolution}" -density 96 "$file" ./scaled/icons/"${filename%.svg}"-"$resolution".png || exit 1
       inkscape --batch-process --export-height "${resolution}" --export-background-opacity=0.0 --export-area-page --export-dpi=96 "$file" --export-overwrite -o "./scaled/icons/${filename%.svg}-${resolution}.png" 2>/dev/null || exit 1

       echo "  ${resolution}x${resolution}-2x"
       #convert -resize "${resolution2x}"x"${resolution2x}"^ -extent "${resolution2x}"x"${resolution2x}" -density 192 "$file" ./scaled/icons/"${filename%.svg}"-"$resolution"-2x.png || exit 1
       inkscape --batch-process --export-height "${resolution2x}" --export-background-opacity=0.0 --export-area-page --export-dpi=192 "$file" --export-overwrite -o "./scaled/icons/${filename%.svg}-${resolution}-2x.png" 2>/dev/null || exit 1

    done

done
