# This Python file uses the following encoding: utf-8

"""Pattern finders module."""
import re

TIMESCALE = re.compile(r'\$timescale')
END = re.compile(r'\$end')
TIME_FULL = re.compile(r'(\d*)(\D*)')
TIME_POINT = re.compile(r'^#\d*')
DATA_POINT = re.compile(r'^r(\d*\.?\d*)')
NANO = -9
PICO = -12
FENTO = -15


def time_units():
    """Generate time units dictionary.

    Returns:
        time units dictionary
    """
    return {
        'ns': 10**(NANO),
        'ps': 10**(PICO),
        'fs': 10**(FENTO),
    }


def find_time_step(path):
    """Find time step in .vcd file.

    Args:
        path(str): path to .vcd file,

    Returns:
        time step of pwl in integer format,
    """
    with open(path, 'r') as data_file:
        time_flag = 0
        for line in data_file:
            time = TIMESCALE.search(line)
            end = END.search(line)
            if end:
                time_flag = 0
            if time_flag:
                time_step_full = line.strip()
            if time:
                time_flag = 1
        time_f = TIME_FULL.search(time_step_full)
        time_scale = float(time_units()[time_f.group(2)])
        time_base = float(time_f.group(1))
    return time_base * time_scale


def find_points(path):
    """Find time step in .vcd file.

    Args:
        path(str): path to .vcd file,

    Returns:
        time_data_dict(dict): dictionary of time(data) of .vcd file,
    """
    with open(path, 'r') as data_file:
        num = -1
        time_data_dict = {}
        for line in data_file:
            time_point = TIME_POINT.search(line)
            data_point = DATA_POINT.search(line)
            if time_point:
                num += 1
            if data_point:
                time_data_dict[num] = data_point.group(1)
    return time_data_dict
