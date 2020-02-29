#!/bin/sh

# ALWAYS DOWNLOAD DELPH-IN REMOTES TO THIS FOLDER  "appName/delphin/"
DIRECTORY=$(cd `dirname $0` && pwd)

echo "<b>CONNECTING to SVN remote: ERG2018</b>"
echo
# Download/Update ERG_2018
if [ -d $DIRECTORY/erg2018 ]; then
    echo "<b>FOUND the folder delphin/erg2018</b>"
    echo "<b>UPDATING it now...</b>"
    cd $DIRECTORY/erg2018
    svn update
else
    echo "<b>COULD NOT FIND the folder delphin/erg2018</b>"
    echo "<b>CREATING folder delphin/erg2018</b>"
    echo "<b>PERFORMING SVN CHECKOUT for ERG2018</b>"
    svn checkout http://svn.delph-in.net/erg/tags/2018  $DIRECTORY/erg2018
fi

echo
echo "<b>CREATING ACE grammar file (erg2018.dat)</b> "

ace -G $DIRECTORY/erg2018.dat -g $DIRECTORY/erg2018/ace/config.tdl

echo
echo
echo "<b>CREATING ACE grammar file (mal-erg2018.dat)</b> "

ace -G $DIRECTORY/mal-erg2018.dat -g $DIRECTORY/erg2018/ace/config-educ.tdl
