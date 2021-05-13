from PIL import Image
import pytesseract
from pdf2image import convert_from_path

from argparse import ArgumentParser

# tess_loc = '/usr/bin/tesseract'

# pytesseract.pytesseract.tesseract_cmd = tess_loc

# print(pytesseract.image_to_string(Image.open('test.png')))

# print("Convert pdf to images...", end="")
# images = convert_from_path("./test.pdf")
# print("done")

# for image in images:
#     print(pytesseract.image_to_string(image, lang="eng"))
#     print("*********")

parser = ArgumentParser(prog="pytesseract-cli")

parser.add_argument("-")
parser.add_argument('-f', dest="files", nargs='*', type=str, help="name(s) of file(s) to perform OCR check upon")
parser.add_argument('-r', dest="directories", nargs='*', type=str, help="directory(s) to recurse upon")
parser.add_argument('-j', dest="join", action="store_const", const=True, default=False, help="directory(s) to recurse upon")

print(parser.parse_args())
