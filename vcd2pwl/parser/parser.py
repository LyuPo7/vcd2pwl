# This Python file uses the following encoding: utf-8

"""Parser of project."""
import argparse


def create_parser():
    """Create parser.

    Returns:
        parser - parser.
    """
    parser = argparse.ArgumentParser(
        prog='vcd2pwl',
		description="""Description:
            The program converts .vcd file to .pwl file.""",
		epilog="""(c) September 2020.
            The developer isn't responsible for any problems
            which might result from work of this program.
            """,
    )
    parser.add_argument(
        'vcd_file',
        metavar='vcd_file',
        type=str,
        help='vcd file',
    )
    parser.add_argument(
        '-b',
        '--begin',
        metavar='begin',
        type=str,
        default='',
        help='string to write to begin of output .pwl file',
    )
    parser.add_argument(
        '-e',
        '--end',
        metavar='end',
        type=str,
        default='',
        help='string to write to end of output .pwl file',
    )
    parser.add_argument(
        '-o',
        '--out_file',
        type=str,
        default='',
        help='name for output file',
        metavar='out_file',
    )

    return parser
