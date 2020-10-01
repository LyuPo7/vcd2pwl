# This Python file uses the following encoding: utf-8

"""Converter module."""
from vcd2pwl.pattern_finders.pattern_finders import find_time_step
from vcd2pwl.pattern_finders.pattern_finders import find_points
from vcd2pwl.pwl_creator.pwl_creator import create_pwl


def converter(path_in, path_out, begin, end):
    """Convert .vcd file to .pwl file.

    Takes path to .vcd file and converts it to .pwl file

    Args:
        path_in(str): path to .vcd file,
        path_out(str): path to .pwl generated file,
        begin(str): string to write to begin of .pwl file,
        end(str): string to write to end of .pwl file,
    """
    time_step = find_time_step(path_in)
    time_data = find_points(path_in)
    create_pwl(path_in, path_out, time_data, time_step, begin, end)
