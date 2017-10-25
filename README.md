# whatsthere

A hard drive observer.

The program scans the directory and displays the following information depending on the option selected:

- Total statistics
    - Total number of entries (files or directories or symlinks) in the directory.
    - Total number of subdirectories in the directory.
    - Total number of files in the directory
- Detailed information table depending on the option.
    - `total` - Entry extension and total number of files with that extension (displayed by default)
    - `entries` - Entry names and sizes
    - `dirs` - Subdirectory names and sizes
    - `files` - File names and sizes
    - `sizes` - Entry extension, total size of files with that extension, list of files with each extension and their own sizes.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

To use this software you will need following python3 packages

- PrettyPrinter
- PrettyTable

You can install the packages required you can use `pip3` or `make init` command.

## Usage

To get more help use

```
./whatsthere/whatsthere.py -h

usage: whatsthere.py [-h] [-d] [PATH] [OPTION] [TABLE_SIZE]

positional arguments:
    PATH         The path to the directory we want to start the search from.
    OPTION       'total' to display total statistics of the directory. 'size' to
                 print table with the sizes of entries.
    TABLE_SIZE   10 by default. Maximum table size to print.

optional arguments:
  -h, --help   show this help message and exit
  -d, --debug  Print auxillary debug information while the program is running

```

### Examples of usage

Simple run `whatsthere.py` with no options. The program will list total current directory statistics and the table of file extensions and the number of files with that extension.

```
$ whatsthere/whatsthere.py

    Total entries: 10
    Directories:   4
    Files:         6
    +----------------+-----------------+
    | File Extension | Number of Files |
    +----------------+-----------------+
    |   Directory    |        4        |
    |      None      |        2        |
    |     Hidden     |        2        |
    |      .txt      |        1        |
    |      .md       |        1        |
    +----------------+-----------------+
```

You can specify the directory to scan by the first argument to the program. You can also specify the option what information to display. Finally, you can specify the number of rows given to output table.

The example below shows how to display file extensions table.

```
$ ./whatsthere/whatsthere.py ./tests/testfiles sizes 99

    Total entries: 10
    Directories:   0
    Files:         10
    +----------------+---------------------+------------+-----------+
    | File Extension | Total Size in bytes | File name  | File size |
    +----------------+---------------------+------------+-----------+
    |     .ext4      |          26         |            |           |
    |                |                     | file3.ext4 |     14    |
    |                |                     | file2.ext4 |     8     |
    |                |                     | file1.ext4 |     4     |
    |                |                     | file0.ext4 |     0     |
    |     .ext3      |          9          |            |           |
    |                |                     | file2.ext3 |     6     |
    |                |                     | file1.ext3 |     3     |
    |                |                     | file0.ext3 |     0     |
    |     .ext2      |          2          |            |           |
    |                |                     | file1.ext2 |     2     |
    |                |                     | file0.ext2 |     0     |
    |     .ext1      |          0          |            |           |
    |                |                     | file0.ext1 |     0     |
    +----------------+---------------------+------------+-----------+
```

Finally, you can simply display entries, directories of files table with entry names and sizes using commands below:

```
$ whatsthere/whatsthere.py ./. entries 99
...
$ whatsthere/whatsthere.py ./. dirs 99
...
$ whatsthere/whatsthere.py ./. files 99
...
```

This example shows how to display files in the current directory:

```
$ whatsthere/whatsthere.py ./. files 99

    Total entries: 10
    Directories:   4
    Files:         6
    +------------------+---------------+
    |     Entries      | Size in bytes |
    +------------------+---------------+
    |    README.md     |      5702     |
    |     Makefile     |      1744     |
    |    .gitignore    |      1149     |
    |     LICENSE      |      1061     |
    |  .gitattributes  |       65      |
    | requirements.txt |       19      |
    +------------------+---------------+
```

For more information read the `Testing` paragraph.

---
## Testing

### Starting tests

It is better to test it via Makefile

```
make
```
### Testing process

The program will first check all requirements and install it using `pip3` if some will be not found on the computer.

Then it creates `./test/testfiles/` subdirectory and fills it with testfiles using the `extmaker.py` script stored in `./tests/` subdirectory. Each file that was generated by `extmaker.py` will look like `fileN.extN` where `N` is a number of the extension. For additional information see `extmaker.py -h` command.

After generating testfiles, the program will perform some basic usage tests on the executable and log everything into `./tests/test.log` file. It will also include `./whatsthere/whatsthere.py.log` log file output (generated by logging module from the executable) into `./tests/test.log` file.

Finally it will open `./tests/test.log` file with the `less` command.

### Ending tests

To get rid of useless files after testing process, use

```
make clean
```

Note that the program will clean the directory itself when restarting tests. All log files will be rewritten.

---

## Author

* **Nikolai Gaiduchenko** - *MIPT student, 515 group* - [Yozh2](https://github.com/Yozh2)

## Acknowledgments
Special thanks to **Tatyana Derbysheva** for useful tips.
