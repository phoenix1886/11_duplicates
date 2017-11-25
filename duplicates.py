import os
import argparse
import hashlib
from collections import defaultdict
import pprint


def calc_hash_sum_of_file(file_path):
    with open(file_path, 'rb') as file:
        hash_obj = hashlib.md5()
        for chunk in chunk_reader(file):
            hash_obj.update(chunk)
        return hash_obj.hexdigest()


def calc_hash_for_files(file_paths):
        hash_sums = list(map(calc_hash_sum_of_file,
                             file_paths))
        return zip(hash_sums, file_paths)


def chunk_reader(file, chunk_size=1024):
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            return
        yield chunk


def arguments_parser():
    parser = argparse.ArgumentParser(description="Anti-duplicator script")
    parser.add_argument(
        'path', help='directory path, where duplicates should be searched')
    return parser


def find_duplicates(directory_path):
    hash_paths_dict = defaultdict(list)
    directory_tree = os.walk(directory_path)

    for dir_path, folders, file_names in directory_tree:
        current_directory_files_paths = list(map(os.path.join,
                                                 [dir_path]*len(file_names),
                                                 file_names))
        hash_sum_values = calc_hash_for_files(current_directory_files_paths)

        for hash_sum, file_path in hash_sum_values:
            if os.path.getsize(file_path):
                hash_paths_dict[hash_sum].append(file_path)

    duplicates_paths = [path_list for path_list in hash_paths_dict.values()
                        if len(path_list) > 1]

    return duplicates_paths


if __name__ == '__main__':
    args_parser = arguments_parser()
    arguments = args_parser.parse_args()

    directory_path = arguments.path
    duplicates = find_duplicates(directory_path)
    for file_list in duplicates:
        print('\n***duplicate files**')
        for file_path in file_list:
            print(file_path)
