# This Python file uses the following encoding: utf-8

"""PWL creation module."""


def create_pwl(path_in, path_out, points, step, begin, end):
    """Create .pwl file.

    Creates .pwl file

    Args:
        path_in(str): path to .vcd file,
        path_out(str): path to .pwl generated file,
        points(dict): time(data) points dictionary from .vcd file,
        step(int): time step for points in .pwl file,
        begin(str): string to write to begin of .pwl file,
        end(str): string to write to end of .pwl file,
    """
    digits_num = 20
    if not path_out:
        path_out = path_in.replace('.vcd', '.pwl')
    with open(path_out, 'w') as file4write:
        for string_begin in begin.split('\\n'):
            file4write.write('{arg}\n'.format(arg=string_begin))
        for key, point in points.items():
            str4write = '+{arg1} {arg2}\n'.format(
                arg1=round(key * step, digits_num),
                arg2=point,
            )
            file4write.write(str4write)
        for string_end in end.split('\\n'):
            file4write.write('{arg}\n'.format(arg=string_end))
    print("'{arg}' file was successfully generated.".format(arg=path_out))
