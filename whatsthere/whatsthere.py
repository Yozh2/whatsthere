#!/usr/local/bin/python3

"""
Обзорщик жёсткого диска:

Программа показывает следующую информацию:
- Сколько файлов какого типа (по расширению) есть в указанной директории? Сколько папок?
- Сколько места занимают файлы каждого типа?
    - файлы хранят размер
    - вывод в виде таблицы
- (++) Какие файлы и папки самые большие по размеру (папки — вместе с вложенными
  файлами)?

Аргументами командной строки задаётся:
- путь к директории, с которой начнём поиски.
- какие запросы делать (количество файлов разного типа, размер файлов разного типа)
- Максимальный размер таблицы (по умолчанию — только 10 самых часто встречающихся типов файлов).

- Таблички с результатами выводить с помощью модуля PTable
"""

from collections import defaultdict
from pprint import PrettyPrinter
import os
from sys import argv
import argparse
import logging
from prettytable import PrettyTable

def pprint(title_to_print='', obj_to_print=None):
    """Prints lists and dicts beautifully"""
    pprinter = PrettyPrinter(indent=4)
    if title_to_print != '':
        print(title_to_print)
    pprinter.pprint(obj_to_print)

def pprint_table(headers=None, rows=None):
    """Prints PrettyTable with the headers and rows given"""
    try:
        table = PrettyTable()
        table.field_names = headers
        for row in rows:
            table.add_row(row)
        print(table)
    except TypeError:
        logging.warning('HEADERS or ROWS is a NoneType object!')

def ls_scan_path(path='.'):
    """
    Get ENTRIES, DIRS, FILES and EXTS objects from the directory.
    ENTRIES - list of entries names
    DIRS    - list of tuples (directory_name, directory_size)
    FILES   - list of tuples (file_name, file_size)
    EXTS    - defaultdict with file extension strings as keys and dictionary as values
                EXTS[ext]['sizes'] - get sum of sizes of files with that extension.
                EXTS[ext]['files'] - a list of tuples (file_name, file_size) with that extension.
    """

    entries = [name for name in os.listdir(path)]

    files, dirs = [], []
    tree = lambda: defaultdict(tree)
    exts = tree()
    # Divide entries into files and directories, also filling exts dictionary
    for entry in entries:
        entry_path = os.path.join(path, entry)                  # Get entry path to use
        entry_size = os.path.getsize(entry_path)                # Get entry size
        entry_tuple = (entry, entry_size)                       # Create tuple for better use

        if os.path.isfile(entry_path):                          # If entry is a file
            files.append(entry_tuple)

            # Update extension dictionary
            filename = os.path.basename(entry_path)             # Get filename
            extension = os.path.splitext(entry_path)[1]         # get extension
            if filename[0] == '.':                              # For hidden files
                extension = 'Hidden'
            elif extension == '':                               # For files with no extension
                extension = 'None'
            exts[extension]['files'] = exts[extension].get('files', []) + [entry_tuple]
            exts[extension]['sizes'] = exts[extension].get('sizes', 0) + os.path.getsize(entry_path)

        elif os.path.isdir(entry_path):                         # If entry is a directory
            dirs.append(entry_tuple)
            extension = 'Directory'
            exts[extension]['files'] = exts[extension].get('files', []) + [entry_tuple]
            exts[extension]['sizes'] = exts[extension].get('sizes', 0) + os.path.getsize(entry_path)

    # Return everything
    return entries, dirs, files, exts

def ls_total(entries=0, dirs=0, files=0):
    """
    ls_total(entries, dirs, files)
    Prints total directory statistics to the console
    """
    print('Total entries:', entries)
    print('Directories:  ', dirs)
    print('Files:        ', files)

def print_ext_total(exts=None, max_table=10):
    """Print extension table with the total number of files with each extension."""

    try:
        ext_rows = [[ext, len(exts[ext]['files'])] for ext in
                    sorted(exts.keys(), key=lambda x: -len(exts[x]['files']))[:max_table]]

    except TypeError:
        logging.error('exts argument is NoneType')
        return
    ext_headers = ['File Extension', 'Number of Files']
    pprint_table(ext_headers, ext_rows)

def print_ext_sizes(exts=None, max_table=10):
    """
    Print extension table with the total size of files with each extension.
    Then print each file with each extension and it's own size.
    """
    # Generate extension key strings and filter them by maximum size and in alphabetical order
    try:
        ext_keys = sorted(exts.keys(), key=lambda x: (-exts[x]['sizes'],
                                                      exts[x]['files']))[:max_table]
    except AttributeError:
        logging.error('exts argument is NoneType')
        return

    ext_rows = []
    for ext in ext_keys:
        ext_rows += [[ext, exts[ext]['sizes'], ' ', ' ']]
        for entry in sorted(exts[ext]['files'], key=lambda x: (-x[1], x[0])):
            ext_rows += [[' ', ' ', entry[0], entry[1]]]

    ext_headers = ['File Extension', 'Total Size in bytes', 'File name', 'File size']
    pprint_table(ext_headers, ext_rows)

def print_entries(entries=None, max_table=10):
    """Print entry table with file_name and file_size columns. Maximum max_table rows."""
    try:
        ext_rows = sorted(entries, key=lambda x: -x[1])[:max_table]
    except TypeError:
        logging.error('entries argument is NoneType')
        return
    ext_headers = ['Entries', 'Size in bytes']
    pprint_table(ext_headers, ext_rows)

if __name__ == "__main__":

    def parse_args():
        """ Parses arguments and returns args object to the main program"""
        parser = argparse.ArgumentParser()
        parser.add_argument("PATH", type=str, nargs='?', default='.',
                            help="The path to the directory we want to start the search from.")
        parser.add_argument('OPTION', type=str, nargs='?', default='total',
                            help="'total' to display total statistics of the directory. \
                            'size' to print table with the sizes of entries.")
        parser.add_argument('TABLE_SIZE', type=int, nargs='?', default=10,
                            help="10 by default. Maximum table size to print.")
        parser.add_argument('-d', '--debug', action='store_true',
                            help="Print auxillary debug information while the \
                            program is running")
        return parser.parse_args()

    # ----------------------------------------------------------------------------------------------
    # enable logging

    logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s] \
    %(message)s', level=logging.DEBUG, filename=u'{}.log'.format(argv[0]))

    # Parse command-line arguments
    ARGS = parse_args()
    OPTION = ARGS.OPTION
    PATH = ARGS.PATH
    TABLE_SIZE = ARGS.TABLE_SIZE

    # Raise an exception if the path doens't exist
    try:
        if not os.path.exists(ARGS.PATH):
            raise FileNotFoundError

        # Get information about files and directories in PATH entry
        ENTRIES, DIRS, FILES, EXTS = ls_scan_path(path=ARGS.PATH)

        if ARGS.debug:
            pprint('ENTRIES', ENTRIES)
            pprint('DIRS', DIRS)
            pprint('FILES', FILES)
            pprint('EXTS', EXTS)

        # Print PrettyTable from EXTS Dictionary ordered by OPTION
        ls_total(len(ENTRIES), len(DIRS), len(FILES))

        # Display information based by OPTION command
        if   OPTION == 'total':
            print_ext_total(EXTS, TABLE_SIZE)
        elif OPTION == 'sizes':
            print_ext_sizes(EXTS, TABLE_SIZE)
        elif OPTION == 'files':
            print_entries(FILES, TABLE_SIZE)
        elif OPTION == 'dirs':
            print_entries(DIRS, TABLE_SIZE)
        elif OPTION == 'entries':
            print_entries(DIRS + FILES, TABLE_SIZE)
        else:
            raise UserWarning

    except FileNotFoundError:
        print('Directory Not Found')
        logging.error('Directory Not Found')
        exit()

    except UserWarning:
        print('Wrong OPTION')
        logging.warning('Wrong OPTION %s', ARGS.OPTION)
        exit()
