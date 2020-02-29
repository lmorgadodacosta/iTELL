#!/bin/sh

# ALWAYS DOWNLOAD DELPH-IN REMOTES TO THIS FOLDER  "appName/delphin/"
DIRECTORY=$(cd `dirname $0` && pwd)

echo "<b>CONNECTING to SVN remote: ERG-TRUNK</b>"
echo
# Download/Update ERG_TRUNK
if [ -d $DIRECTORY/erg_trunk ]; then
    echo "<b>FOUND the folder delphin/erg_trunk</b>"
    echo "<b>UPDATING it now...</b>"
    cd $DIRECTORY/erg_trunk
    svn update
else
    echo "<b>COULD NOT FIND the folder delphin/erg_trunk</b>"
    echo "<b>CREATING folder delphin/erg_trunk</b>"
    echo "<b>PERFORMING SVN CHECKOUT for ERG-TRUNK</b>"
    svn checkout http://svn.delph-in.net/erg/trunk/  $DIRECTORY/erg_trunk
fi

echo
echo "<b>CREATING ACE grammar file (erg_trunk.dat)</b> "

ace -G $DIRECTORY/erg_trunk.dat -g $DIRECTORY/erg_trunk/ace/config.tdl

echo
echo
echo "<b>CREATING ACE grammar file (mal-erg_trunk.dat)</b> "

ace -G $DIRECTORY/mal-erg_trunk.dat -g $DIRECTORY/erg_trunk/ace/config-educ.tdl
