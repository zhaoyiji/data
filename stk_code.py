#!/bin/bash/python
# Filename: stk_code.py

""" STK code define

    STK Code store in 'leech.code' file.
    STK Code in file format is sh600000,sz000002,

"""

import config


STK_CODE_FILE = 'leech.code'


def get_stk_code():
    """ Get code list

    get stk code list from "leech.code" local file
    :rtype list
    """
    try:
        handle = file(STK_CODE_FILE, 'r')
        code_list = handle.read(-1)
        code_list = code_list.strip()
        handle.close()
        return code_list.split(',')
    except IOError:
        config.LOGGER.info("IOError, open 'leech.code' Error")
        return []
