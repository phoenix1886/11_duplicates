import os
from collections import Counter


class File:

    def __init__(self, dir_path, name):
        self.dir_path = dir_path
        self.name = name
        self.file_path = os.path.join(dir_path, name)
        self.size = os.path.getsize(self.file_path)

        self._hash_value = hash((self.name, self.size))

    def __eq__(self, other):
        return self.name, self.size == other.name, other.size

    def __hash__(self):
        return self._hash_value

    def __str__(self):
        return "{name} ({size} bytes): at {path}".format(name=self.name,
                                                         path=self.dir_path,
                                                         size=self.size)

    def __repr__(self):
        return "File({}, {})".format(self.dir_path, self.name)


def get_files_list(path):
    directory_tree = os.walk(path)
    files_list = []
    for dir_path, folders, file_names in directory_tree:
        files = [File(dir_path, file_name) for file_name in file_names]
        files_list.extend(files)
    return files_list


def find_duplicates(files_list):
    files_counter = Counter(files_list)
    duplicates = [file for file in files_list
                  if files_counter[file] > 1]
    duplicates.sort(key=lambda file: (file.name, file.size))
    return duplicates


if __name__ == '__main__':
    path = '/Users/KirillMaslov/Documents/Projects/devman'
    files_counter = get_files_list(path)
    duplicate_files = find_duplicates(files_counter)
    for file in duplicate_files:
        print(file)
