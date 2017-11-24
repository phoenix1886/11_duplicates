import os
from collections import Counter
import argparse

class File:

    def __init__(self, dir_path, file_name):
        self.dir_path = dir_path
        self.file_name = file_name
        self.file_path = os.path.join(dir_path, file_name)
        self.size = os.path.getsize(self.file_path)

        self._hash_value = hash((self.file_name, self.size))

    def __eq__(self, other):
        return self.file_name, self.size == other.file_name, other.size

    def __hash__(self):
        return self._hash_value

    def __str__(self):
        return "{file_name} ({size} bytes): at {path}".format(
            file_name=self.file_name, path=self.dir_path, size=self.size)

    def __repr__(self):
        return "File({}, {})".format(self.dir_path, self.file_name)


def arguments_parser():
    parser = argparse.ArgumentParser(description="Anti-duplicator script")
    parser.add_argument(
        'path', help='directory path, where duplicates should be searched')
    return parser


def get_files(path):
    directory_tree = os.walk(path)
    files = []
    for dir_path, folders, file_names in directory_tree:
        files_in_current_directory = [File(dir_path, file_name)
                                      for file_name in file_names]
        files.extend(files_in_current_directory)
    return files


def find_duplicates(files_list):
    files_counter = Counter(files_list)
    duplicates = [file for file in files_list
                  if files_counter[file] > 1]
    duplicates.sort(key=lambda file: (file.file_name, file.size))
    return duplicates


if __name__ == '__main__':
    args_parser = arguments_parser()
    arguments = arguments_parser().parse_args()

    directory_path = arguments.path
    files = get_files(directory_path)
    duplicate_files = find_duplicates(files)
    for file in duplicate_files:
        print(file)
