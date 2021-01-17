import datetime
import array
from config import VALUE_SIZE, SEGMENT_SIZE
import re

def byte_to_double(new_bytearr: bytearray) -> float:
    """
    Wrapper for array.array()

    :param new_bytearr: 8 byte chunck representing Double
    :return: float
    """
    return array.array('d', new_bytearr)[0]


def bytes_to_datetime(new_bytearr: bytearray):
    """
    Converts eight bytes to datetime

    :param new_bytearr: 8 byte chunck representing Double
    :return: datetime object
    """
    doubles_sequence = byte_to_double(new_bytearr)
    seconds = (doubles_sequence - 25569) * 86400.0
    dt_obj = datetime.datetime.utcfromtimestamp(seconds)

    return dt_obj


def process_sgement(raw_bytes):
    return bytes_to_datetime(raw_bytes[:VALUE_SIZE]), byte_to_double(raw_bytes[VALUE_SIZE:])


def zfile_iterator(zfilehandle):
    while True:
        data = zfilehandle.read(SEGMENT_SIZE)
        if len(data) == 0:
            break
        yield data

def zfile_read_sain(zfilehandle):
    for segment in zfile_iterator(zfilehandle):
        ts, val = process_sgement(segment)
        yield ts, val

def filter_namelist(archnamelist):
    return [archfile for archfile in archnamelist if re.match(r".*Pen.*",archfile)]

def get_sensor_number(filename):
    file_format = r".*Pen(?P<sensor_number>\d+).*"
    match = re.match(file_format, str(filename))
    return match.group("sensor_number")

def get_sensor_date(filehandle):
    it = zfile_read_sain(filehandle)
    ts , _ = it.__next__()
    return ts