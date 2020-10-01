# This Python file uses the following encoding: utf-8

"""Main file of project."""
import sys

from vcd2pwl.parser.parser import create_parser
from vcd2pwl.converter.converter import converter


def main():
    """Run project."""
    print('Hi!')
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    converter(
        namespace.vcd_file,
        namespace.out_file,
        namespace.begin,
        namespace.end,
    )


if __name__ == '__main__':
    main()
