# iTELL: Intelligent Technologically Enhanced Language Learning


Includes:
- LCC-NTU English Writing Support System
- CALLIG: Computer-Assisted Language Learning using Improvisational Games
- iXue: an intelligent system to support Mandarin Chinese learners   
- Grammarium 

### 

I highly reccomend to create a Python environment using virtualenv to install such versions
You must install all libraries in [`requriements.txt`](requirements.txt)


Make sure ACE and ART are on path to the WSGI.  Both binaries need to be in a place where WSGI can see it. In your own bin it will not work. I chose to put it in `/usr/bin/ace`  and it works fine.


You need to start by installing some basics:


```bash
$ sudo apt-get update
$ sudo apt-get -y upgrade
$ sudo apt-get install -y python3-pip
$ sudo apt-get install build-essential libssl-dev libffi-dev python-dev
$ sudo apt-get install -y python3-dev python3-venv
$ sudo apt-get install virtualenv
$ sudo apt-get install subversion
$ sudo apt-get install python-nltk

```

Now you need to install the python dependencies. We will use requirements.txt for this:  

```bash
$ cd ~/
$ mkdir environments
$ cd environments/
environments/$ virtualenv -p python3 itell_env
environments/$ source itell_env/bin/activate
(itell_env) environments/$ pip install -r /var/www/itell/requirements.txt
```



Make sure you have the NLTK data available from a publicly visible location. For example:

```bash
sudo python -m nltk.downloader -d /usr/local/share/nltk_data wordnet
sudo python -m nltk.downloader -d /usr/local/share/nltk_data omw
sudo python -m nltk.downloader -d /usr/local/share/nltk_data punkt
sudo python -m nltk.downloader -d /usr/local/share/nltk_data cmudict
sudo python -m nltk.downloader -d /usr/local/share/nltk_data averaged_perceptron_tagger
```


Make sure you have the grammars in place (app-folder/static/...).

First run:

```bash
/var/www/itell/delphin$ bash pull_update_erg2018.bash
/var/www/itell/delphin$ bash pull_update_ergTRUNK.bash
/var/www/itell/delphin$ bash pull_update_zhong.bash
```

Then, for now, you need to compile and copy these grammars to /var/www/itell/static/
erg.dat erg-mal.dat zhong.dat


Build databases and basic data files:
/var/www/itell/bin$ bash build_db.bash 
/var/www/itell/bin$ python dump_wn.py 


Both the folders and content of [`db\`](db\) and  [`delphin\`](delphin\) need to be accessible by 'www-data', with read, write and executing permissions. 

The best way to do this is to change the group ownership of these folders to 'www-data' 

Failing to do this will, among other things,  show the access to dbs as "locked".


sudo chgrp -R www-data  delphin/
sudo chgrp -R www-data  db/



Copy something this into your apache2 config.

```bash
########################################################################
# This is running under a virtual-env for python3.
#
# The path should be the root directory of the virtual environment,
# which in turn contains the bin and lib directories.
#
# Apache needs to be able to run your environment!
# Rather than change the permissions on your home directory, it might
# be better to consider locating your WSGI application code and any
# Python virtual environment outside of your home directory.
#
# source:
# modwsgi.readthedocs.io/en/develop/user-guides/virtual-environments.html
########################################################################
WSGIDaemonProcess itell user=www-data group=www-data threads=5  python-home=/home/lmc/environments/itell_env
WSGIScriptAlias /itell /var/www/itell/run_itell.wsgi
<Directory /var/www/itell/>
    WSGIProcessGroup itell
    WSGIApplicationGroup %{GLOBAL}
    WSGIScriptReloading On
    Require all granted
</Directory>
```


Additional Tweakings for Apache Enconding Errors

In the event you get errors such as: UnicodeEncodeError: 'ascii' codec can't encode character 'xxx' in position xxx: ordinal not in range(128)

This is likely due to the default enconding configs available to apache2, and that are possibly incomplete in your machine.
To avoid these issues, ensure that the following lines are included in your apache envvars file (typically found in /etc/apache2/envvars).

```bash
export LANG='en_US.UTF-8'
export LC_ALL='en_US.UTF-8'
```
