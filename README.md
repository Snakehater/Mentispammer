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
To create app:
pip3 install -U git+https://github.com/metachris/py2app.git@master
py2applet --make-setup GUI.py
<br>
<br>
create python script:
from setuptools import setup

APP = ['GUI.py']
DATA_FILES = ['botFunc.py']
OPTIONS = {'argv_emulation': True}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
<br>
<br>
run with:
python3 setup.py py2app -A
