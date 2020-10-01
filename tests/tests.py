# -*- coding:utf-8 -*-

"""Tests for gendiff."""

from vcd2pwl.converter.converter import converter


def test_converter():
    """Check converter for json files."""
    converter(
        'tests/fixtures/test.vcd',
        'tests/fixtures/test.pwl',
        '.SUBCKT VDD_source VDD_port VDD_zero\nV0 VDD_port VDD_zero PWL(',
        '+)\n.ENDS'
    )
    file_w_answer = open('tests/fixtures/test.true.pwl', 'r')
    file_4_check = open('tests/fixtures/test.pwl', 'r')
    true_list = file_w_answer.readlines()
    list4check = file_4_check.readlines()

    assert set(true_list) == set(list4check)