#!/bin/sh

# ALWAYS DOWNLOAD DELPH-IN REMOTES TO THIS FOLDER  "appName/delphin/"
DIRECTORY=$(cd `dirname $0` && pwd)

echo "<b>CONNECTING to GITHUB remote: INDRA</b>"
echo

# Download/Update INDRA
if [ -d $DIRECTORY/indra ]; then
    echo "<b>FOUND the folder delphin/indra</b>"
    echo "<b>UPDATING it now...</b>"
    cd $DIRECTORY/indra
    git pull
    cd ~/
else
    echo "<b>COULD NOT FIND the folder delphin/indra</b>"
    echo "<b>CREATING folder delphin/indra</b>"
    echo "<b>PERFORMING GIT CLONE for INDRA</b>"
    git clone https://github.com/davidmoeljadi/INDRA.git $DIRECTORY/indra
fi

echo
echo "<b>CREATINGACE grammar file (indra.dat)</b> "

ace -G $DIRECTORY/indra.dat -g $DIRECTORY/indra/ace/config.tdl
