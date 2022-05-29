
# telenav-assets

Repository of images, diagrams, logos, icons, backgrounds and other assets used on Telenav OSS web sites.
Graphic images in this repository are licensed under [Apache 2.0 License](graphics/LICENSE).

    telenav-assets
    └── docs
        ├── png
        └── svg
    graphics
    └── source
    maps
    └── administrative-borders
        ├── 0.9.0
        ├── 0.9.1
        └── source

## Github Pages

The *docs* folder in this repository is mapped by Github Pages to `https://telenav.github.io/telenav-assets/`

> IMPORTANT NOTE
> 
> The contents of this folder should be considered *volatile*.
> Changes to graphic assets should be made under the *graphics* 
> folder and copied into the *docs* folder.

## Source Graphics

The *graphics* folder contains original graphics files that can be built
with the build.sh script into scaled png images that can then be copied
to the *docs* folder. Other graphics, such as .svg files, can be copied as-is.

## Map Data

The *maps* folder contains map data. The *maps/administrative-borders* folder
contains border polylines for continents, countries, states, counties,
metropolitan areas, and time zones. Different versions are available for backwards
compatibility, and the source data files can be found under *source*.
