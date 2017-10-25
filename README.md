# whatsthere

A hard drive observer.

The program scans the directory and displays the following information depending on the option selected:

- Total statistics
    - Total number of entries (files or directories or symlinks) in the directory.
    - Total number of subdirectories in the directory.
    - Total number of files in the directory
- Detailed information table depending on the option.
    - Entry extension and total number of files with that extension (displayed by default)
    - Entry names and sizes
    - Subdirectory names and sizes
    - File names and sizes
    - Entry extension, total size of files with that extension, list of files with each extension and their own sizes.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

To use this software you will need following python3 packages

- PrettyPrinter
- PrettyTable

You can install the packages required you can use `pip3` or `make init` command.

## Usage

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

## Note

## Authors

* **Nikolai Gaiduchenko** - *MIPT student, 515 group* - [Yozh2](https://github.com/Yozh2)

## Acknowledgments
