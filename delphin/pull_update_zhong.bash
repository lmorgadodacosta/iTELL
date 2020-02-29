#!/bin/sh

# ALWAYS DOWNLOAD DELPH-IN REMOTES TO THIS FOLDER  "appName/delphin/"
DIRECTORY=$(cd `dirname $0` && pwd)

echo "<b>CONNECTING to GITHUB remote: ZHONG</b>"
echo

# Download/Update Zhong
if [ -d $DIRECTORY/zhong ]; then
    echo "<b>FOUND the folder delphin/zhong</b>"
    echo "<b>UPDATING it now...</b>"
    cd $DIRECTORY/zhong
    git pull
    cd ~/
else
    echo "<b>COULD NOT FIND the folder delphin/zhong</b>"
    echo "<b>CREATING folder delphin/zhong</b>"
    echo "<b>PERFORMING GIT CLONE for ZHONG</b>"
    git clone https://github.com/delph-in/zhong.git $DIRECTORY/zhong
fi

echo
echo "<b>CREATINGACE grammar file (zhong.dat)</b> "

ace -G $DIRECTORY/zhong.dat -g $DIRECTORY/zhong/cmn/zhs/ace/config.tdl
