#!/bin/sh

# ALWAYS DOWNLOAD DELPH-IN REMOTES TO THIS FOLDER  "appName/delphin/"
DIRECTORY=$(cd `dirname $0` && pwd)

echo "<b>CONNECTING to GITHUB remote: JACY</b>"
echo

# Download/Update JACY
if [ -d $DIRECTORY/jacy ]; then
    echo "<b>FOUND the folder delphin/jacy</b>"
    echo "<b>UPDATING it now...</b>"
    cd $DIRECTORY/jacy
    git pull
    cd ~/
else
    echo "<b>COULD NOT FIND the folder delphin/jacy</b>"
    echo "<b>CREATING folder delphin/jacy</b>"
    echo "<b>PERFORMING GIT CLONE for JACY</b>"
    git clone https://github.com/delph-in/jacy.git $DIRECTORY/jacy
fi

echo
echo "<b>CREATINGACE grammar file (jacy.dat)</b> "

ace -G $DIRECTORY/jacy.dat -g $DIRECTORY/jacy/ace/config.tdl
