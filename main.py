from argparse import ArgumentParser
from pathlib import Path
from PIL import Image, UnidentifiedImageError
from pytesseract import image_to_string, image_to_pdf_or_hocr
from typing import Union

parse_functions = {
    "pdf": image_to_pdf_or_hocr,
    "txt": image_to_string
}


def write_parsed(contents: Union[bytes, str], destination):
    print(destination)
    with destination.open(f"w{'+b' if isinstance(contents, bytes) else ''}") as f:
        f.write(contents)


def process_file(file: Path):

    assert file.is_file()

    try:
        image = Image.open(file)
    except UnidentifiedImageError:
        print(f"File: {file.absolute()} cannot be opened as a file : skipping")
        return

    # TODO - Include language
    result = parse_functions[parser.file_type](image, lang="eng")

    if parser.join:
        parsing_buffer.append(result)
    else:
        resulting_path = file.with_suffix(f".{parser.file_type}")
        write_parsed(result, resulting_path)


def process_directory(directory: Path):

    assert directory.is_dir()

    dir_list = sorted(directory.iterdir())

    for file in filter(lambda entry: entry.is_file(), dir_list):
        process_file(file)

    if parser.recurse:
        for nested_directory in filter(lambda entry: entry.is_dir(), dir_list):
            process_directory(nested_directory)


def run():

    for file in parser.files:
        process_file(Path(file))

    for directory in parser.directories:
        process_directory(Path(directory))

    # if parser.join:
    #     ...


if __name__ == "__main__":

    parsing_buffer = []

    parser = ArgumentParser(prog="pytesseract-cli")

    # files and directories to process
    parser.add_argument('-f', dest="files", nargs='*', default=[], type=str, help="name(s) of file(s) to process")
    parser.add_argument('-d', dest="directories", nargs='*', default=[], type=str, help="directory(s) to process")

    parser.add_argument('-r', dest="recurse", action="store_const", const=True, default=True,
                        help="recurse on all directories listed")

    # parser.add_argument('-j', dest="join", required=False, type=str,
    #                     help="join all parsed files into one with the given file name")

    parser.add_argument('-t', dest="file_type", choices=parse_functions.keys(), default="txt",
                        help="desired output filetype")

    parser = parser.parse_args()

    run()

    # if parser.join:
    #     ...
