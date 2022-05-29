#-------------------------------------------------------------------------------
# Name:        mapzenboundarymodifier.py
# Purpose:     Parses the boundary geojson files from MapZen and add the OSM identifier and the OSM object type as properties of the GeoJSON feature.
#              This script facilitates loading to a database since the OSM identifier can be flagged as a primary key.
#
# Author:      kristenk
#
# Created:     09/03/2016
# Copyright:   (c) Telenav, Inc. kristenk 2016
#-------------------------------------------------------------------------------

import codecs
import getopt
import json
import os
import os.path
import sys

#FUNCTION DECLARATIONS
def usage():
    print '\n\n'
    print 'Usage options for {scriptname}:'.format(scriptname=sys.argv[0])
    print '-h, --help                                       Shows help message and exits.\n'
    print '------GeoJSON Transform Settings----------------------------------------\n'
    print '-f, --file           [GeoJSON File Name]              Input File .'
    print '-o, --outputdir      [Output Directory]               Output Directory for the modified GeoJSON file. Default output Directory is the current working directory.'


def modifyMapzenGeoJSON(inputGeoJSONFilePath,outputDirectory):
    
    #Variable Declarations
    geoJSONFilePath = inputGeoJSONFilePath
    geoJSONFileName = os.path.basename(geoJSONFilePath)
    osmid = None
    osmObjectType = None
    nameInEnglish = None
    nameWithoutLanguageCode = None
    iso3166_2Code = None
    isIn = None
    geoJSONFile = None
    geoJSONOutputFileName = geoJSONFileName.split('.')[0] + '_tnmodidified.geojson'
    geoJSONOutputFilePath = os.path.join(outputDirectory,geoJSONOutputFileName)
    geoJSONOutputFile = codecs.open(geoJSONOutputFilePath,'w','utf-8')
    mapzenGeoJSONFeatures = None
    outputgeoJSONString = None

    print 'Processing {geojsonfilename}'.format(geojsonfilename=geoJSONFileName)

    geoJSONFile = open(geoJSONFilePath,'r')
    mapzenGeoJSONFeatures = json.load(geoJSONFile)

    for geoJSONFeature in mapzenGeoJSONFeatures['features']:
        osmid = geoJSONFeature['id']
        osmObjectType = geoJSONFeature['osm_type']  

        geoJSONFeature['properties']['osmid_tn'] = osmid
        geoJSONFeature['properties']['osmobjecttype_tn'] = unicode(osmObjectType)

    json.dump(mapzenGeoJSONFeatures,geoJSONOutputFile,ensure_ascii=False)
    geoJSONOutputFile.close()
    geoJSONFile.close()

    print 'finished processing {geojsonfilename}'.format(geojsonfilename=geoJSONFileName)
    print 'Outputted file to {outputdirectory}'.format(outputdirectory=outputDirectory)


def main():

    #Variable Declarations
    inputGeoJSONFilePath = None
    outputDirectory = os.getcwd()

    #PARSE AND VALIDATE COMMANDLINE ARGUMENTS
    ###Parse command line arguments
    try:
        options, remainder = getopt.getopt(sys.argv[1:],'hf:o:',['help','file=','outputdir='])
    except getopt.GetoptError as err:
            print '\nERROR:\n\t',err,'\n'
            usage()
            sys.exit(2)

    ###Process command line argument options
    for opt,arg in options:
        if opt in ('-h','--help'):
            usage()
            sys.exit(0)
        if opt in ('-f', '--file'):
            inputGeoJSONFilePath = arg
        if opt in ('-o', '--outputdir'):
            outputDirectory = arg            

    if inputGeoJSONFilePath==None:
        modeMsg = "Mapzen GeoJSON File not specified. Ending script."
        print modeMsg
        sys.exit(1) 


    if os.path.isfile(inputGeoJSONFilePath) == False:
        modeMsg = "Mapzen GeoJSON File Path invalid. Ending script."
        print modeMsg
        sys.exit(1)         

    #Modify the Mapzen GeoJSON File
    modifyMapzenGeoJSON(inputGeoJSONFilePath,outputDirectory)

if __name__ == "__main__":
    main()
