from argparse import ArgumentParser, Namespace
from pathlib import Path
from PIL import Image, UnidentifiedImageError
from pytesseract import get_languages, image_to_string, image_to_pdf_or_hocr
from sys import argv
from typing import Union


parse_functions = {
    "pdf": image_to_pdf_or_hocr,
    "txt": image_to_string
}


def write_parsed(contents: Union[bytes, str], destination: Path):
    """
    Write a parsed / interpreted contents of an image to some destination path
    :param contents: Parsed contents after running a pytesseract OCR function
    :param destination: A Path to write the contents to
    """
    print(destination)
    with destination.open(f"w{'+b' if isinstance(contents, bytes) else ''}") as f:
        f.write(contents)


def process_file(file: Path, namespace: Namespace):
    """
    Parse a file using pytesseract
    :param file: A Path to some file that can be opened as a PIL.Image
    :param namespace: namespace of parameters parsed from command-line input
    """

    assert file.is_file()

    try:
        image = Image.open(file)
    except UnidentifiedImageError:
        print(f"file: {file.absolute()} cannot be opened as a file : skipping")
        return

    # TODO - Include language
    result = parse_functions[namespace.file_type](image, lang=namespace.lang)

    # if parser.join:
    #     parsing_buffer.append(result)
    # else:
    resulting_path = file.with_suffix(f".{namespace.file_type}")
    write_parsed(result, resulting_path)


def process_directory(directory: Path, namespace: Namespace):
    """
    Process all valid files in a given directory.
    :param directory: A Path to some directory
    :param namespace: namespace of parameters parsed from command-line input
    """

    assert directory.is_dir()

    dir_list = sorted(directory.iterdir())

    for file in filter(lambda entry: entry.is_file(), dir_list):
        process_file(file, namespace)

    if namespace.recurse:
        for nested_directory in filter(lambda entry: entry.is_dir(), dir_list):
            process_directory(nested_directory, namespace)


def run():
    """
    "Main" of a file that interprets all command-line arguments and processes any files or
    directories accordingly.
    """

    parsing_buffer = []

    parser = ArgumentParser(prog="pytesseract-cli")

    # files and directories to process
    parser.add_argument('-f', dest="files", nargs='*', default=[], type=str, help="name(s) of file(s) to process")
    parser.add_argument('-d', dest="directories", nargs='*', default=[], type=str, help="directory(s) to process")

    parser.add_argument('-r', dest="recurse", action="store_const", const=True, default=False,
                        help="recurse on all directories listed")

    # parser.add_argument('-j', dest="join", required=False, type=str,
    #                     help="join all parsed files into one with the given file name")

    parser.add_argument('-t', dest="file_type", choices=parse_functions.keys(), default="txt",
                        help="desired output filetype")

    parser.add_argument('-l', dest="lang", type=str, help="language of the text in any image(s)", required=False)

    parser.add_argument('--list-languages', dest="list", action="store_const", const=True, default=True,
                        help="list all languages available")

    if len(argv) < 2:
        parser.print_help()
        exit(0)

    namespace = parser.parse_args()

    if namespace.list:
        print("languages available:\n-", "\n- ".join(get_languages()))
        exit(0)

    for file in namespace.files:
        process_file(Path(file), namespace)

    for directory in namespace.directories:
        process_directory(Path(directory), namespace)

    # if parser.join:
    #     ...


if __name__ == "__main__":
    run()
