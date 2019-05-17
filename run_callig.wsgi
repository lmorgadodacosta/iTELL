import sys
if sys.version_info[0]<3:       # require python3
    raise Exception("Python3 required! Current (wrong) version: '%s'" % sys.version_info)

sys.stdout = sys.stderr

sys.path.insert(0, '/var/www/callig/')
from callig import app as application
