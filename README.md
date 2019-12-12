# mentimeter-spammer
A simple voting bot for Mentimeter

Requires Python 3.x

Requires:
<br>
pip3 install requests
<br>
pip3 install grequests
<br>
pip3 install mttkinter
<br>

run with:
<br>
python3 bot.py
<br>
<br>
or:
<br>
sh start.sh


<br><br><br><br><br><br><br><br><br><br>
To create app:<br>
pip3 install -U git+https://github.com/metachris/py2app.git@master
<br><br>
py2applet --make-setup GUI.py
<br>
<br>
create python script:<br>
from setuptools import setup<br>
<br>
APP = ['GUI.py']<br>
DATA_FILES = ['botFunc.py']<br>
OPTIONS = {'argv_emulation': True}<br>
<br>
setup(<br>
    app=APP,<br>
    data_files=DATA_FILES,<br>
    options={'py2app': OPTIONS},<br>
    setup_requires=['py2app'],<br>
)<br>
<br>
<br>
run with:<br>
python3 setup.py py2app -A
