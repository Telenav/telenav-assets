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
       echo "  ${resolution}x${resolution}"
       convert -size "${resolution}x${resolution}" -density 96 "$file" ./scaled/icons/"${filename%.svg}"-"$resolution".png || exit 1

       echo "  ${resolution}x${resolution}@2x"
       convert -size "${resolution}x${resolution}" -density 192 "$file" ./scaled/icons/"${filename%.svg}"-"$resolution"@2x.png || exit 1

    done

done
