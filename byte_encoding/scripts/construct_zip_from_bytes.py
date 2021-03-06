"""
Short script for reading a file from within a zip archive
"""

import zipfile
import io
from pathlib import Path

zippath = Path(r'Path to zip')

with open(zippath.resolve(), "rb") as fp:
    zbytes = fp.read()

archive = zipfile.ZipFile(io.BytesIO(zbytes), "r")

# Get first file from archive
filename = archive.namelist()[0]

# Open connection to file
file_handle_read_bytes = archive.open(filename, 'r')

# Read from file as text
file_hadnle_read_chars = io.TextIOWrapper(file_handle_read_bytes)