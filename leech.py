#!/bin/bash/python
# Filename: leech.py

import logging.config
import config
import raw_data


def main():
    logging.config.fileConfig("logger.conf")
    config.LOGGER.info('this is leech entry point.')

    raw_data.analyze()

if __name__ == "__main__":
    main()
