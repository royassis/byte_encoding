import zipfile
import io
from pathlib import Path


zippath = Path(r'***REMOVED***\40bytes_from_original.zip')

archive = zipfile.ZipFile(zippath.resolve(), 'r')
filename = archive.namelist()[0]
items_file  = archive.open(filename, 'r')

items_file  = io.TextIOWrapper(items_file)

items_file.read(8)


