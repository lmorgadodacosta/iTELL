# iTELL: Intelligent Technologically Enhanced Language Learning


Includes:
- LCC-NTU English Writing Support System
- CALLIG: Computer-Assisted Language Learning using Improvisational Games
- iXue: an intelligent system to support Mandarin Chinese learners   


### 

I highly reccomend to create a Python environment using virtualenv to install such versions
You must install all libraries in [`requriements.txt`](requirements.txt)


sudo apt-get install python-nltk



```bash
$ sudo apt-get update
$ sudo apt-get -y upgrade
$ sudo apt-get install -y python3-pip
$ sudo apt-get install build-essential libssl-dev libffi-dev python-dev
$ sudo apt-get install -y python3-dev python3-venv
$ sudo apt-get install virtualenv


```


```bash
$ cd ~/
$ mkdir environments
$ cd environments/
environments/$ virtualenv -p python3 itell_env
environments/$ source itell_env/bin/activate
(itell_env) environments/$ pip install -r /var/www/itell/requirements.txt
```



Make sure you have the NLTK available from a publicly visible location. For example:

```bash
sudo python -m nltk.downloader -d /usr/local/share/nltk_data wordnet
sudo python -m nltk.downloader -d /usr/local/share/nltk_data omw
sudo python -m nltk.downloader -d /usr/local/share/nltk_data punkt
sudo python -m nltk.downloader -d /usr/local/share/nltk_data cmudict
sudo python -m nltk.downloader -d /usr/local/share/nltk_data averaged_perceptron_tagger
```


Make sure you have the grammars in place (app-folder/static/...).


Run:
/var/www/itell/bin$ bash build_db.bash 
/var/www/itell/bin$ python dump_wn.py 


Both the folders and content of [`db\`](db\) and  [`delphin\`](delphin\) need to be accessible by 'www-data', with read, write and executing permissions. 

The best way to do this is to change the group ownership of these folders to 'www-data' 

Failing to do this will, among other things,  show the access to dbs as "locked".





Copy this into your apache2 config.

```bash
########################################################################
# This should be running under a virtual-env for python3.
#
# The path should be the root directory of the virtual environment,
# which in turn contains the bin and lib directories.
#
# Apache needs to be able to run your environment!
# Rather than change the permissions on your home directory,
# it might be better to consider locating your WSGI application code
# and any Python virtual environment outside of your home directory.
#
# source:
# https://modwsgi.readthedocs.io/en/develop/user-guides/virtual-environments.html
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

export LANG='en_US.UTF-8'
export LC_ALL='en_US.UTF-8'





Make sure ACE is on path.

You can find this out by choosing to put the ACE binary in one the locations shown by running [`$PATH`]($PATH) in your command line.
