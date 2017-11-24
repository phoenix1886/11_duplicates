import os
from collections import Counter
import argparse
import hashlib


class File:

    def __init__(self, dir_path, file_name):
        self.dir_path = dir_path
        self.file_name = file_name
        self.file_path = os.path.join(dir_path, file_name)
        self.size = os.path.getsize(self.file_path)

        self.hash_sum = self._calc_hash_sum()

    def _calc_hash_sum(self):
        with open(self.file_path, 'rb') as file:
            hash_obj = hashlib.md5()
            for chunk in self._chunk_reader(file):
                hash_obj.update(chunk)
            return hash_obj.hexdigest()

    def _chunk_reader(self, file, chunk_size=1024):
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                return
            yield chunk

    def __eq__(self, other):
        return self.file_name, self.size == other.file_name, other.size

    def __hash__(self):
        return int(self.hash_sum, 16)

    def __str__(self):
        return "{file_name} ({size} bytes): at {path}\n\t{hash}\n".format(
            file_name=self.file_name, path=self.dir_path, size=self.size,
            hash=self.hash_sum)

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
    duplicates.sort(key=lambda file: (file.hash_sum, file.file_name))
    return duplicates


if __name__ == '__main__':
    args_parser = arguments_parser()
    arguments = arguments_parser().parse_args()

    directory_path = arguments.path
    files = get_files(directory_path)
    duplicate_files = find_duplicates(files)
    for file in duplicate_files:
        print(file)
