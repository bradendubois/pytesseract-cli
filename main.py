from PIL import Image
import pytesseract

from argparse import ArgumentParser

tess_loc = '/usr/bin/tesseract'

pytesseract.pytesseract.tesseract_cmd = tess_loc

print(pytesseract.image_to_string(Image.open('test.png')))

