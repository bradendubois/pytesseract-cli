# pytesseract-cli

A command-line wrapper for ``pytesseract``, a Python wrapper for ``tesseract``.

## Description

This is a command-line wrapper to enable easier usage of the [Tesseract OCR engine](https://opensource.google/projects/tesseract) with multiple files and/or directories. The project itself is written in Python, and uses [pytesseract](https://pypi.org/project/pytesseract/) for interaction with `tesseract`.

Benefits of this interface include the ability to easily parse multiple images and files, as well as recurse upon directories.

## Requirements

Basic requirements are an up-to-date installation of [Python 3](https://python.org) and [Tesseract OCR](https://opensource.google/projects/tesseract).

### Tesseract 

Both the [Tesseract OCR engine](https://github.com/tesseract-ocr/tesseract) as well as any [training data](https://github.com/tesseract-ocr/tessdata) for desired languages must be installed.

Both of the above are available, for example, on the [ArchLinux User Repository](https://aur.archlinux.org/):
- ``tesseract``
- ``tesseract-data``

## Installation

This project is available on [PyPI](https://pypi.org/) under the page [pytesseract-cli](https://pypi.org/project/pytesseract-cli/).

Using [pip](https://pypi.org/project/pip/):

```shell
pip install pytesseract-cli
```

to upgrade:

```shell
pip install -U pytesseract-cli
```

## Usage

In a terminal:

```shell
$ pytesseract-cli
usage: pytesseract-cli [-h] [-f [FILES ...]] [-d [DIRECTORIES ...]] [-r] [-t {pdf,txt}] [-l LANG] [--list-languages]

optional arguments:
  -h, --help            show this help message and exit
  -f [FILES ...]        name(s) of file(s) to process
  -d [DIRECTORIES ...]  directory(s) to process
  -r                    recurse on all directories listed
  -t {pdf,txt}          desired output filetype
  -l LANG               language of the text in any image(s)
  --list-languages      list all languages available
```

## Acknowledgements

- [pytesseract](https://pypi.org/project/pytesseract/) for providing an easy-to-use wrapper for `tesseract`.
- [tesseract](https://opensource.google/projects/tesseract) for providing a free and open-source OCR engine.
