# dbus_app_server
Proof of concept app using D-bus as the message bus between webapp serving RESTful API and a db

More details [here](http://soumyadipdm.github.io/)

Installation:
=============
Assumes Ubuntu 16.04

```
1. Install python3-gi, it's not available in PyPI
sudo apt-get install python3-gi

2. Create a virtualenv with system site-packages as you'd need python3-gi
python3 ~/bin/virtualenv-15.1.0/virtualenv.py --system-site-packages pybus

3. Activate it
source pybus/bin/activate

4. Install the required packages, mentioned in requirements.txt
pip install -r requirements.txt
```
