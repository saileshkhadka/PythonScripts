#!/usr/bin/env python3

__author__ = ['[sailesh khadka](http://github.com/saileshkhadka)']
__date__ = '2015.03.25'

"""
This is a Python script that outputs the path of the current
OSX wallpaper.
This is helpful when the desktop wallpaper is randomized
across a large collection of pictures and you want to
delete the current wallpaper.
### Warning
+ This approach doesn't work with multiple monitors or virtual desktops.
### Tested On
+ OSX Yosemite 10.10.2 with a single desktop on a MBP.
### Usage
Ensure `db_path` and `wallpaper_dir` are correctly set below.
Assuming `get-osx-wallpaper.py` is on your path,
check the output with the following
```
$ get-osx-wallpaper.py
/Users/ghost/Pictures/wallpaper/nature/496.jpg
```
Please ensure this is correct before trying to remove it!
This can be paired with other commands such as `open` or `rm`.
Run `killall Dock` to refresh the changes after removing the file.
Note that the dock will be restarted and all windows will be
unminimized.
```
$ open $(get-osx-wallpaper.py)
$ rm $(get-osx-wallpaper.py) && killall Dock

alias open-wallpaper='open $(get-osx-wallpaper.py)'
alias rm-wallpaper='rm $(get-osx-wallpaper.py) && killall Dock'
```
"""


import sqlite3
from os.path import expanduser

# db_path found from: http://superuser.com/questions/664184
db_path = expanduser("~/Library/Application Support/Dock/desktoppicture.db")
wallpaper_dir = expanduser("~/Pictures/wallpaper/nature")

conn = sqlite3.connect(db_path)
c = conn.cursor()
data_table = list(c.execute('SELECT * FROM data'))

print(data_table)

# The current wallpaper is the last element in the data table.
print("{}/{}".format(wallpaper_dir, data_table[-1][0]))