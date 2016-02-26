#!/usr/bin/env 
# Zipho Masholoigu (SANBI-UWC)

import sys
import os
import tempfile
import shutil
import optparse
import urllib2
import subprocess

import logging
log = logging.getLogger( __name__ )

LICENCE_TARGET_DIRECTORY = "tool-data/novoalign/"

#Parse Command Line
parser = optparse.OptionParser()
args = parser.parse_args()
    
filename = args[0]
    
#read the contents of the license file
license_str = open( filename ).read()
    
#create the licence target directory
os.mkdir( LICENCE_TARGET_DIRECTORY )
    
#save info to json file
open( filename, 'wb' ).write( license_str )
