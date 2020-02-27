# ALWAYS DOWNLOAD DELPH-IN REMOTES TO THIS FOLDER  "appName/delphin/"
DIRECTORY=$(cd `dirname $0` && pwd)

# Download/Update ERG_TRUNK
if [ -d $DIRECTORY/erg_trunk ]; then
    printf "\033[1;32m FOUND delphin/erg_trunk \033[0m \n"  #GREEN
    printf "\033[1;32m Will update it now... \033[0m \n"  #GREEN
    cd $DIRECTORY/erg_trunk
    svn update
else
    printf "\033[1;31m Couldn't find erg_trunk \033[0m \n" #RED
    printf "\033[1;32m Will do a SVN checkout... \033[0m \n"  #GREEN
    svn checkout http://svn.delph-in.net/erg/trunk/  $DIRECTORY/erg_trunk
fi

# Download/Update ERG_2018
if [ -d $DIRECTORY/erg2018 ]; then
    printf "\033[1;32m FOUND delphin/erg2018 \033[0m \n"  #GREEN
    printf "\033[1;32m Will update it now... \033[0m \n"  #GREEN
    cd $DIRECTORY/erg2018
    svn update
else
    printf "\033[1;31m Couldn't find delphin/erg2018 \033[0m \n" #RED
    printf "\033[1;32m Will do a SVN checkout... \033[0m \n"  #GREEN
    svn checkout http://svn.delph-in.net/erg/tags/2018  $DIRECTORY/erg2018
fi


# Download/Update Zhong
if [ -d $DIRECTORY/zhong ]; then
    printf "\033[1;32m FOUND delphin/zhong \033[0m \n"  #GREEN
    printf "\033[1;32m Will update it now... \033[0m \n"  #GREEN
    cd $DIRECTORY/zhong
    git pull
    cd ~/
else
    printf "\033[1;31m Couldn't find delphin/zhong \033[0m \n" #RED
    printf "\033[1;32m Will do a git clone... \033[0m \n"  #GREEN
    git clone https://github.com/delph-in/zhong.git $DIRECTORY/zhong
fi

