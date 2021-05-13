from typing import Union

from PIL import Image
import pytesseract
from pdf2image import convert_from_path

from argparse import ArgumentParser

from pathlib import Path
# tess_loc = '/usr/bin/tesseract'

# pytesseract.pytesseract.tesseract_cmd = tess_loc

# print(pytesseract.image_to_string(Image.open('test.png')))

# print("Convert pdf to images...", end="")
# images = convert_from_path("./test.pdf")
# print("done")

# for image in images:
#     print(pytesseract.image_to_string(image, lang="eng"))
#     print("*********")

parse_functions = {
    "pdf": pytesseract.image_to_pdf_or_hocr,
    "txt": pytesseract.image_to_string
}


def write_parsed(contents: Union[bytes, str], destination):
    with destination.open(f"w{'+b' if isinstance(contents, bytes) else ''}") as f:
        f.write(contents)


def process_file(file: Path):

    assert file.is_file()

    result = parse_functions[parser.file_type](Image.open(file))

    if parser.join:
        parsing_buffer.append(result)
    else:
        resulting_path = file.with_suffix(f".{parser.file_type}")
        write_parsed(result, resulting_path)


def process_directory(directory: Path):

    assert directory.is_dir()

    dir_list = sorted(directory.iterdir())

    for file in filter(lambda entry: entry.isfile(), dir_list):
        process_file(file)

    if parser.recurse:
        for nested_directory in filter(lambda entry: entry.isdir(), dir_list):
            process_directory(nested_directory)


def run():

    for file in parser.files:
        process_file(file)

    for directory in parser.directories:
        process_directory(directory)

    if parser.join:
        ...


if __name__ == "__main__":

    parsing_buffer = []

    parser = ArgumentParser(prog="pytesseract-cli")

    parser.add_argument('-f', dest="files", nargs='*', type=str, help="name(s) of file(s) to perform OCR check upon")

    # TODO - Separate into a recurse option and a directory option
    parser.add_argument('-r', dest="directories", nargs='*', type=str, help="directory(s) to recurse upon")
    parser.add_argument('-j', dest="join", required=False, type=str, help="directory(s) to recurse upon")
    parser.add_argument('-t', dest="file_type", choices=parse_functions.keys(), default="pdf",
                        help="desired output filetype")

    print(parser := parser.parse_args())


    run()
