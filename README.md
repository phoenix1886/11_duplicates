# Anti-Duplicator

This script lists all duplicate files in a given directory.

# How to use
To use this script, one should use python3.5.
The script takes one positional argument:
* path: the path of the directory we are searching in

## Example
This example shows how to find all duplicates in 'UserName/problem3' directory
```
$ python duplicates.py 'UserName/problem3'

***duplicate files**
../../problem3/3_bars/three_bars_project/lib/python3.5/site-packages/pip/_vendor/packaging/_compat.py
../../problem3/3_bars/three_bars_project/lib/python3.5/site-packages/pkg_resources/_vendor/packaging/_compat.py

***duplicate files**
../../problem3/3_bars/three_bars_project/lib/python3.5/site-packages/pip/_vendor/requests/hooks.py
../../problem3/3_bars/three_bars_project/lib/python3.5/site-packages/requests/hooks.py
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
