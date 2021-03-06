from pathlib import Path
from setuptools import setup
from os import environ

cwd = Path(".")

README = (cwd / "README.md").read_text()
dependencies = (cwd / "requirements.txt").read_text().strip().split("\n")

# This should be set by the automated Github workflow
VERSION = environ["SEMANTIC_VERSION"]

setup(
    name="pytesseract-cli",
    version=VERSION,
    description="A pytesseract wrapper enabling OCR on images and directories.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bradendubois/pytesseract-cli",
    author="Braden Dubois",
    author_email="braden.dubois@usask.ca",
    packages=["pytesseract_cli"],
    keywords="pytesseract tesseract ocr cli",
    include_package_data=True,
    install_requires=dependencies,
    entry_points={
        'console_scripts': ["pytesseract-cli=pytesseract_cli.main:run"],
    }
)