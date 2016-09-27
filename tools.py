# JN 2015-06-22

# tools for response viewer

import re

NAME_PATTERN =\
    re.compile(r'(\d{1,3})(\w{2,3})(\d{1})_CSC(\d{1,3})_(\w)_.*_(-?\d{1,3})')


def parse_name(name):
    """
    split an image name into experiment, patient, CSC, daytime, group
    """
    pat, paradigm, rep, csc, daytime, gid = NAME_PATTERN.match(name).groups()

    ret = {}
    try:
        ret['patient'] = int(pat)
    except ValueError:
        ret['patient'] = 0

    ret['paradigm'] = paradigm

    try:
        ret['repetition'] = int(rep)
    except ValueError:
        ret['repetition'] = None

    ret['csc'] = int(csc)  # if this fails, exception

    ret['daytime'] = daytime

    ret['gid'] = int(gid)  # dito

    return ret


if __name__ == "__main__":
    # run tests

    print(parse_name('010fn1_CSC52_m_cl_-01.png'))
