# Anti-Duplicator

This script lists all duplicate files in a given directory.

The script ouputs the list in the following format:
<file_name> (<file_size> bytes) at: <file_directory_path>
    <hash_sum_md5>

# How to use
To use this script, one should use python3.5.
The script takes one positional argument:
* path: the path of the directory we are searching in

## Example
This example shows how to find all duplicates in 'UserName/problem11' directory
```
$ python duplicates.py 'UserName/problem11'
master (41 bytes): at /Users/KirillMaslov/Documents/Projects/devman/problem11/11_duplicates/.git/refs/heads
	0459474b7aaae584aca70c3884db91a8

master (41 bytes): at /Users/KirillMaslov/Documents/Projects/devman/problem11/11_duplicates/.git/refs/remotes/origin
	0459474b7aaae584aca70c3884db91a8

HEAD (990 bytes): at /Users/KirillMaslov/Documents/Projects/devman/problem11/11_duplicates/.git/logs
	d950d0646a7ef5b046125ef17fd53e79

master (990 bytes): at /Users/KirillMaslov/Documents/Projects/devman/problem11/11_duplicates/.git/logs/refs/heads
	d950d0646a7ef5b046125ef17fd53e79
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
