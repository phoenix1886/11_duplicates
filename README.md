# Anti-Duplicator

This script lists all duplicate files in a given directory.

The script ouputs the list in the following format:
<file_name> (<file_size> bytes) at: <file_directory>

# How to use
To use this script, one should use python3.5.
The script takes one positional argument:
* path: the path of the directory we are searching in

## Example
This example shows how to find all duplicates in 'UserName/problem11' directory, 
```
$ python duplicates.py 'UserName/problem11'
.DS_Store (6148 bytes): at UserName/problem11
.DS_Store (6148 bytes): at UserName/problem11/11_duplicates
master (41 bytes): at UserName/problem11/11_duplicates/.git/refs/heads
master (41 bytes): at UserName/problem11/11_duplicates/.git/refs/remotes/origin
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
