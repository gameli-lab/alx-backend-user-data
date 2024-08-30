#!/usr/bin/env python3
"""
    Module containing filtered_logger function
"""

import logging
import re


def filter_datum(fields: list,
                 redaction: str, message: str, separator: str) -> str:
    """
        Returns the log message obfuscated

    pattern = f'({"|".join([f"{field}=[^{separator}]*"
                            for field in fields])})'
    return re.sub(pattern,
                  lambda m: f'{m.group(0).split("=")[0]}={redaction}', message)
    """
    return (re.sub(f'({"|".join(fields)})=[^{separator}]*', lambda m:
                   f'{m.group(1)}={redaction}', message))


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError
