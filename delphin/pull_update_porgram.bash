#!/bin/sh

# ALWAYS DOWNLOAD DELPH-IN REMOTES TO THIS FOLDER  "appName/delphin/"
DIRECTORY=$(cd `dirname $0` && pwd)

echo "<b>CONNECTING to GITHUB remote: PorGram</b>"
echo

# Download/Update PorGram
if [ -d $DIRECTORY/zhong ]; then
    echo "<b>FOUND the folder delphin/porgram</b>"
    echo "<b>UPDATING it now...</b>"
    cd $DIRECTORY/porgram
    git pull
    cd ~/
else
    echo "<b>COULD NOT FIND the folder delphin/porgram</b>"
    echo "<b>CREATING folder delphin/porgram</b>"
    echo "<b>PERFORMING GIT CLONE for PorGram</b>"
    git clone https://github.com/LR-POR/PorGram.git $DIRECTORY/porgram
fi

echo
echo "<b>PorGram does not yet have an ACE config file.</b> "

# echo "<b>CREATINGACE grammar file (porgram.dat)</b> "

# ace -G $DIRECTORY/porgram.dat -g $DIRECTORY/zhong/cmn/zhs/ace/config.tdl
